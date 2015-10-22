from collections import Counter

def compute_n_grams(n, input, output):
	f = open(input, 'r')
	output = open(output, 'w')
	lines = [line.rstrip('\n').lstrip('\t') for line in f]

	nGrams = []
	for line in lines:
		nGrams += getNgrams(line, n)

	counter = Counter(nGrams)

	for key in sorted(counter):
		output.write(key + '\t' + str(counter[key]) + '\n')

	f.close()
	output.close()


def getNgrams(line, n):
	tokens = line.split()
	nGrams = []
	for i in range(len(tokens) - n + 1):
		nGrams.append([tokens[i + j] for j in range(n)])

	for i in range(len(nGrams)):
		nGrams[i] = ' '.join(nGrams[i]).lower()

	return nGrams

if __name__ == '__main__':
	compute_n_grams(1, 'foiIrSer.txt', 'unigramas.txt')
	compute_n_grams(2, 'foiIrSer.txt', 'bigramas.txt')