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
def InsertionSort(numbers):
	# for do segundo elemento até o último
	for i in range(1, len(numbers)):
		# guardando o valor do elemento atual
		x = numbers[i]
		# pegando o índice do elemento anterior
		j = i-1
		# se o elmento anteior for maior que o atual, 
		# troca-se os dois de lugar até que j = 0 e array[j]
		# ainda seja maior que x, que significa que está desordenado
		while j>=0 and x < numbers[j]:
			# o elemento à frente de j assume o valor de array[j]
			numbers[j+1] = numbers[j]
			# e decrementa-se o j para refazer a comparação
			# até que chegue ao ponto em que o vetor até ali
			# esteja ordenado e a condição vire falsa
			j = j - 1
		# então agora o algoritmo encontrou o lugar onde
		# deve inserir o elemento x
		numbers[j+1] = x
		# repte-se o processo até todo array estar ordenado
	return numbers

############# MAIN CODE ##############

# recebendo o array com o tipo e tamanho especificados
numbers = loadEntry(RANDOM, N_1k)

# guardando o tempo de inicio do algoritmo
start = timeit.default_timer()
# executando o algoritmo
ordened = InsertionSort(numbers)
# gurdando o tempo de término do algoritmo
end = timeit.default_timer()
# imprimindo o vetor ordenado
print(ordened)
# e o tempo de execução
print("\nTempo de execução: %f\n" % (end - start))