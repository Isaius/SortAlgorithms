import time
import timeit

# CONSTANTES
RANDOM = "aleatorios"
CRESC  = "crescentes"
DECRES = "decrescentes"

N_100  = "100.txt"
N_500  = "500.txt"
N_1k   = "1k.txt"
N_5k   = "5k.txt"
N_30k  = "30k.txt"
N_80k  = "80k.txt"
N_100k = "100k.txt"
N_150k = "150k.txt"
N_200k = "200k.txt"
# FIM DAS CONSTANTES

# carrega a entrada especificada de um arquivo
def loadEntry(type_entry, quantity):
	file = open(str(type_entry) + '/' + str(quantity), 'r')
	text = file.read()
	auxVet = []
	auxVet = text.split(" ")
	numbers = []

	for i in range(0, len(auxVet)-1):
		numbers.append((int(auxVet[i])))

	return numbers

# recebe um array contendo números e retorna em ordem crescente
def BubbleSort(numbers):
	# guardando o tamanho do array -1 para usar no for
    num_elementos = len(numbers)-1
    # variavel booleana para controle
    isOrdened = False
    # enquanto não estiver ordenado, repetir
    while not isOrdened:
    	# aqui torna a variavel de controle True por padrão
    	# para caso detecte que não está ordenado, mude
        isOrdened = True
        # for percorrendo todo o array
        for i in range(num_elementos):
        	# se o elemento atual for maior que o proximo
            if numbers[i] > numbers[i+1]:
            	# então troca-se os dois elementos de lugar
                numbers[i], numbers[i+1] = numbers[i+1],numbers[i]
                # e colca-se a variavel com falso, para refazer a
                # verificação se está ordenado ou não
                isOrdened = False 
    # array ordenado
    return numbers

########### MAIN CODE #############
# recebendo o array com o tipo e tamanho especificados
numbers = loadEntry(RANDOM, N_1k)

# guardando o tempo de inicio do algoritmo
start = timeit.default_timer()
# executando o algoritmo
numbers = BubbleSort(numbers)
# gurdando o tempo de término do algoritmo
end = timeit.default_timer()
# imprimindo o vetor ordenado
print(numbers)
# e o tempo de execução
print("\nTempo de execução: %f\n" % (end - start))