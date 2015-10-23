from collections import Counter

# def compute_n_grams(n, inputF, parametrizacao, output):
#     """
#         recebe tamanho do n-grama (n), o nome do ficheiro com o corpus anotado,
#         o ficheiro de parametrizacao e a extensao dos ficheiros que irao ser 
#         escritos. O resultado serao os ficheiros escritos com os n-gramas e a 
#         contagem para cada um dos lemas em parametrizacao (caso tenham sido 
#         usados durante a anotacao)
#     """
#     f = open(inputF, 'r')
#     param = open(parametrizacao, 'r')

#     # lemas[0] tem o primeiro lema, lemas[1] o segundo...
#     lemas = param.readlines()[1].split()
#     param.close()

#     # cada celula em lines tem uma linha do corpus e respectivo lema
#     # (OLD) lines = [line.rstrip('\n').lstrip('\t') for line in f]
#     lines = []
#     for line in f:
#         lema = line.split('\t')[0]
#         # retira o new line do fim e o lema no inicio
#         sentence = line.rstrip('\n').lstrip('\t')
#         lines.append([lema, sentence])

#     nGrams = {}
#     for lema in lemas:
#         # cada lema tera uma lista de tokens diferente
#         nGrams[lema] = []

#     for line in lines:
#         if line[0] in lemas:
#             # adiciona a lista de ngramas do lema da frase os que encontrou
#             nGrams[line[0]] += getNgrams(line[1], n)
    
#     # para cada lema escrevemos num ficheiro os ngramas
#     for lema in lemas:
#         writeNgrams(nGrams, lema, output)

#     f.close()

def compute_n_grams(inputF, parametrizacao):
    """
        recebe tamanho do n-grama (n), o nome do ficheiro com o corpus anotado,
        o ficheiro de parametrizacao e a extensao dos ficheiros que irao ser 
        escritos. O resultado serao os ficheiros escritos com os n-gramas e a 
        contagem para cada um dos lemas em parametrizacao (caso tenham sido 
        usados durante a anotacao)
    """
    f = open(inputF, 'r')
    param = open(parametrizacao, 'r')

    # lemas[0] tem o primeiro lema, lemas[1] o segundo...
    lemas = param.readlines()[1].split()
    param.close()

    # cada celula em lines tem uma linha do corpus e respectivo lema
    # (OLD) lines = [line.rstrip('\n').lstrip('\t') for line in f]
    lines = []
    for line in f:
        lema = line.split('\t')[0]
        # retira o new line do fim e o lema no inicio
        sentence = line.rstrip('\n').lstrip('\t')
        lines.append([lema, sentence])

    unigrams = {}
    bigrams = {}
    for lema in lemas:
        # cada lema tera uma lista de tokens diferente
        unigrams[lema] = []
        bigrams[lema] = []

    for line in lines:
        if line[0] in lemas:
            # adiciona a lista de ngramas do lema da frase os que encontrou
            unigrams[line[0]] += getNgrams(line[1], 1)
            bigrams[line[0]] += getNgrams(line[1], 2)
    
    # para cada lema escrevemos num ficheiro os ngramas
    for lema in lemas:
        # so vale a pena escrever os ngramas e a contagem se existirem para esse lema
        if unigrams[lema] != []:
            # N - n tokens
            n = len(unigrams[lema])

            counterUnigrams = Counter(unigrams[lema])
            counterBigrams = Counter(bigrams[lema])
            # v vocabulario
            v = len(counterUnigrams)

            writeNgrams(counterUnigrams, lema, '.unigramas')
            writeNgrams(counterBigrams, lema, '.bigramas')

            for key in counterBigrams:
                counterBigrams[key] = laPlace(counterBigrams[key], n, v)
                print counterBigrams[key]
            writeNgrams(counterBigrams, lema, 'Alisamento.bigramas')

    f.close()


def writeNgrams(counter, lema, output):
    """
        recebe a lista de ngramas (nGrams), o lema e a 
        extensao do ficheiro de output. Escreve os ngramas
        e a respectiva contagem num ficheiro com o nome lema+output
    """
    f = open(lema + output, 'w')
    # transforma a lista num dicionario em que a chave e' o elemento
    # o valor e' o numero de vezes que ocorre

    for key in sorted(counter):
        f.write(key + '\t' + str(counter[key]) + '\n')

    f.close()



def getNgrams(line, n):
    """
        recebe uma frase, e n (de n-gram) e devolve uma lista de todos os n-gram nessa frase
    """
    tokens = line.split()
    nGrams = []
    for i in range(len(tokens) - n + 1):
        nGrams.append([tokens[i + j] for j in range(n)])

    for i in range(len(nGrams)):
        nGrams[i] = ' '.join(nGrams[i]).lower()

    return nGrams

def laPlace(count, N, vocabulary):
    return (count + 1.0) * N / (N + vocabulary)

if __name__ == '__main__':
    compute_n_grams('foramIrSer-3-fred.out', 'foramParametrizacao.txt')
    #compute_n_grams(2, 'foramIrSer-3-fred.out', 'foramParametrizacao.txt','.bigramas')
