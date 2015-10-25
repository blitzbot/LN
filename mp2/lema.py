import sys
import os

def computeLemaBigrams(word, classification1, classification2, test, smoothing):
	out = word + "ResultadoAlisamento.txt" if smoothing else word + "Resultado.txt"

	if os.path.exists(out):
		os.remove(out)

	c1BigramsPath = classification1 + "Alisamento.bigramas" if smoothing else classification1 + ".bigramas"
	c2BigramsPath = classification2 + "Alisamento.bigramas" if smoothing else classification2 + ".bigramas"
	
	bigrams1 = readGrams(c1BigramsPath)
	bigrams2 = readGrams(c2BigramsPath)

	#for word count
	c1UnigramsPath = classification1 + "Alisamento.unigramas" if smoothing else classification1 + ".unigramas"
	c2UnigramsPath = classification2 + "Alisamento.unigramas" if smoothing else classification2 + ".unigramas"
	unigrams1 = readGrams(c1UnigramsPath)
	unigrams2 = readGrams(c2UnigramsPath)

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

			c1P = 0
			c2P = 0

			if not smoothing:
				c1P = getBigramProbability(bigrams1, bigram1, bigram2, w1C1Count, w2C1Count)
				c2P = getBigramProbability(bigrams2, bigram1, bigram2, w1C2Count, w2C2Count)
			else:
				c1P = getBigramProbabilitySmoothing(bigrams1, bigram1, bigram2, w1C1Count, w2C1Count, len(unigrams1))
				c2P = getBigramProbabilitySmoothing(bigrams2, bigram1, bigram2, w1C2Count, w2C2Count, len(unigrams2))

			writeResult(out, line.rstrip(), classification1, c1P, classification2, c2P)

	t.close()

def getBigramProbability(dictionary, bigram1, bigram2, w1Count, w2Count):
	if w1Count == 0 or w2Count == 0: return 0 #error

	bigram1Count = dictionary[bigram1] if bigram1 in dictionary else 0
	bigram2Count = dictionary[bigram2] if bigram2 in dictionary else 0

	return (bigram1Count/w1Count) * (bigram2Count/w2Count)

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

def main(param, test):
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

	computeLemaBigrams(word, s[0], s[1], test, False)
	computeLemaBigrams(word, s[0], s[1], test, True)

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
