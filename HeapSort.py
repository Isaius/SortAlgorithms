'''
	Código implementado do algoritmo de Heap Sort
	Implementado usando Heap de Máximo ou Heap Máxima
	Os números vem de um arquivo txt gerado

	código feito por Isaias @Isaius
'''

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

# carrega a entrada escolhida do arquivo para o array
def loadEntry(type_entry, quantity):
	file = open(str(type_entry) + '/' + str(quantity), 'r')
	text = file.read()
	auxVet = []
	auxVet = text.split(" ")
	numbers = []

	for i in range(0, len(auxVet)-1):
		numbers.append((int(auxVet[i])))

	return numbers

# calcula e retorna o filho à esquerda do nó
def leftSon(array, i):
	return 2*i

# calcula e retorna o filho à direita do nó
def rightSon(array, i):
	return 2*i+1

# troca o elemento i com o bigger dentro do array
def swap(array, i, bigger):
	array[i], array[bigger] = array[bigger], array[i]

def remakeMaxHeap(array, i, sizeHeap):
	# calculando o indice do filho à esquerda
	left = leftSon(array, i)
	# calculando o indice do filho à direita
	right = rightSon(array, i)
	# considera-se o pai como o maior, para poder
	# seguir a definição da Heap de Maximo, onde
	# o pai deve ser sempre maior que os filhos
	bigger = i
	# se o filho à esquerda não for um nó folha, pois está
	# na primeira metade do array da Heap de Maximo
	# e seu valor for maior do que o pai
	if left <= sizeHeap and array[left] > array[bigger]:
		# então o maior passa a ser o filho à esquerda
		bigger = left
	# se o filho à direita não for nó folha e 
	# maior que o maior atual (filho ou pai)
	if right <= sizeHeap and array[right] > array[bigger]:
		# emtão o maior passa a ser o filho à direita
		bigger = right
	# caso o pai (i) não seja mais o maior valor, e por consequencia
	# não está na estrutura da Heap de Máximo, então devemos refaze-la
	if bigger != i:
		# primeiro troca-se o pai de lugar com o maior filho
		swap(array, i, bigger)
		# e passa a verificar para baixo deles se ainda está obedecendo
		# a definição da estrutura da Heap de Maximo para todos os filhos
		remakeMaxHeap(array, bigger, sizeHeap)

def makeMaxHeap(array, sizeHeap):
	# for da metade da Heap até o primeiro elemento
	for i in range((int(sizeHeap/2)), -1, -1):
		# reconstruindo a estrutura da Heap de Maximo
		remakeMaxHeap(array, i, sizeHeap)

def HeapSort(array):
	# guardando o tamanho maixmo do array (n)
	sizeArray = len(array)-1
	# gurdando o tamanho da nossa Heap maxima
	# que inicia com tamanho igual ao array (n)
	sizeHeap = sizeArray
	# construindo a estutura da nossa Heap maxima
	makeMaxHeap(array, sizeHeap)
	# for do ultimo elemento do array até o segundo (1)
	for i in range(len(array)-1, -1, -1):
		# troca o os dois elementos de lugar
		swap(array, 0, i)
		# decrementa o tamanho considerado da Heap
		# pois o ultimo ja é o maior, e por consequencia
		# ordenado e não precisa mais ser considerado
		sizeHeap = sizeHeap - 1
		# refaz a estrutura da Heap de maximo
		remakeMaxHeap(array, 0, sizeHeap)

########## MAIN CODE ###########

# recebendo o array de entrada, do tipo e tamanho especificados
array = loadEntry(CRESC, N_1k)

# gravando o tempo de inicio do algoritmo
start = timeit.default_timer()
# executando o algoritmo em si
HeapSort(array)
# guardando o tempo de término do algoritmo
end = timeit.default_timer()
# mostrando o array ordenado
print(array)
# e o tempo de execução
print("\nTempo de execução: %f" % (end - start))