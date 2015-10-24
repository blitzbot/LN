# -*- coding: utf-8 -*-

import sys

def computeLemaBigrams(word, classification1, classification2, test):
	d1 = readGrams(classification1 + ".bigramas")
	d2 = readGrams(classification2 + ".bigramas")

	#for word count
	unigrams1 = readGrams(classification1 + ".unigramas")
	unigrams2 = readGrams(classification2 + ".unigramas")

	t = open(test)
	for line in t:
		l = line.rstrip()
		w = l.split(" ")
		bigram1 = ""
		bigram2 = ""
		for i in range(len(w)):
			if (w[i] == word):
				bigram1 = w[i-1] + " " + w[i]
				bigram2 = w[i] + " " + w[i+1]
				break
		if bigram1 != "" and bigram2 != "":
			#w1 w2 w3 where bigram1=w1 w2 and bigram2=w2 w3
			w1 = bigram1.split(" ")[0]
			w2 = bigram1.split(" ")[1]
			w1Count = 0
			w2Count = 0

			if w1 in unigrams1:
				w1Count += unigrams1[w1]
			if w1 in unigrams2:
				w1Count += unigrams2[w1]
			if w2 in unigrams1:
				w2Count += unigrams1[w2]
			if w2 in unigrams2:
				w2Count += unigrams2[w2]

			c1Count = getBigramProbability(d1, bigram1, bigram2, w1Count, w2Count)
			c2Count = getBigramProbability(d2, bigram1, bigram2, w1Count, w2Count)

			writeResult(test+"-out", l, classification1, c1Count, classification2, c2Count)
	t.close()

def getBigramProbability(dictionary, bigram1, bigram2, w1Count, w2Count):
	bigram1Count = 0
	bigram2Count = 0

	if bigram1 in dictionary:
		bigram1Count += dictionary[bigram1]

	if bigram2 in dictionary:
		bigram2Count += dictionary[bigram2]

	return (bigram1Count/w1Count) * (bigram2Count/w2Count)

def writeResult(fileName, line, c1, c1Count, c2, c2Count):
	result = ""
	if c1Count > c2Count:
		result = " || Classification = " + c1
	else:
		result = " || Classification = " + c2

	with open(fileName, "a") as f:
		f.write(line + " || P(" + c1 + ")=" + str(c1Count) + ", P(" + c2 + ")=" + str(c2Count) + result + "\n")
		f.close

def computeLemaUnigrams(unigramas1, unigramas2, test):
	return


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
			s = line.rstrip().split(" ")
			break
	f.close()
	#s.remove("n-é-verbo")

	computeLemaBigrams(word, s[0], s[1], test)

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
