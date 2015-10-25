import sys
import os

def computeLema(unigramsC1Path, unigramsC2Path, bigramsC1Path, bigramsC2Path, word, classification1, classification2, test):
	out = word + "Resultado.txt"

	if os.path.exists(out):
		os.remove(out)
	
	bigramsC1 = readGrams(bigramsC1Path)
	bigramsC2 = readGrams(bigramsC2Path)

	#for word count
	unigrams1 = readGrams(unigramsC1Path)
	unigrams2 = readGrams(unigramsC2Path)

	t = open(test)
	for line in t:
		l = "^ " + line.rstrip() + " $"
		w = l.split()
		bigram1 = ""
		bigram2 = ""
		for i in range(len(w)):
			if (w[i] == word):
				bigram1 = w[i-1] + " " + w[i]
				bigram2 = w[i] + " " + w[i+1]
				break
		if bigram1 != "" and bigram2 != "":
			#w1 w2 w3 where bigram1=w1 w2 and bigram2=w2 w3
			w1 = bigram1.split()[0]
			w2 = bigram1.split()[1]
			w1C1Count = 0
			w1C2Count = 0
			w2C1Count = 0
			w2C2Count = 0

			if w1 in unigrams1:
				w1C1Count = unigrams1[w1]
			else:
				w1C1Count = unigrams1["UNK"]

			if w1 in unigrams2:
				w1C2Count = unigrams2[w1]
			else:
				w1C2Count = unigrams2["UNK"]

			if w2 in unigrams1:
				w2C1Count = unigrams1[w2]
			else:
				w2C1Count = unigrams1["UNK"]

			if w2 in unigrams2:
				w2C2Count = unigrams2[w2]
			else:
				w2C2Count = unigrams2["UNK"]

			c1P = getBigramProbabilitySmoothing(bigramsC1, bigram1, bigram2, w1C1Count, w2C1Count, len(unigrams1))
			c2P = getBigramProbabilitySmoothing(bigramsC2, bigram1, bigram2, w1C2Count, w2C2Count, len(unigrams2))

			writeResult(out, line.rstrip(), classification1, c1P, classification2, c2P)

	t.close()

def getBigramProbabilitySmoothing(dictionary, bigram1, bigram2, w1Count, w2Count, vocabularyCount):
	bigram1Count = dictionary[bigram1] if bigram1 in dictionary else 0
	bigram2Count = dictionary[bigram2] if bigram2 in dictionary else 0

	return (bigram1Count + 1/(w1Count + vocabularyCount)) * (bigram2Count + 1/(w2Count + vocabularyCount))

def writeResult(fileName, line, c1, c1Count, c2, c2Count):
	result = ""
	if c1Count == c2Count:
		result = " || Classification = ?"
	elif c1Count > c2Count:
		result = " || Classification = " + c1
	else:
		result = " || Classification = " + c2

	with open(fileName, "a") as f:
		f.write(line + " || P(" + c1 + ")=" + str(c1Count) + ", P(" + c2 + ")=" + str(c2Count) + result + "\n")
		f.close

def readGrams(gramsFile):
	f = open(gramsFile)
	d = dict()
	for line in f:
		tokens = line.split('\t')
		d[tokens[0]] = float(tokens[1])
	f.close()
	return d

def main(unigramsC1Path, unigramsC2Path, bigramsC1Path, bigramsC2Path, param, test):
	f = open(param)
	s = []
	word = ""
	for i, line in enumerate(f):
		if i == 0:
			word = line.rstrip()
		elif i == 1:
			s = line.rstrip().split()
			break
	f.close()

	computeLema(unigramsC1Path, unigramsC2Path, bigramsC1Path, bigramsC2Path, word, s[0], s[1], test)

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
