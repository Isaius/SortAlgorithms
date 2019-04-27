import time
import timeit

# CONSTANTES
RANDOM = "aleatorios"
CRESC  = "crescentes"
DECRES = "decrescentes"

N_10   = "10.txt" 
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
	entry = []

	for i in range(0, len(auxVet)-1):
		entry.append((int(auxVet[i])))

	return entry

def merge(array, first, mid, last):
	# calculando a primeira metade do sub array
	half1 = (mid-first)+1
	# calculando a segunda metade
	half2 = last-mid
	# arrays temporarios para armazenar as duas metades
	L = []
	R = []
	# zerando os valores, para efeitos de clareza no codigo
	for i in range(half1):
		L.append(0)
	for i in range(half2):
		R.append(0)
	# preenchendo os elementos da metade esquerda do array
	for i in range(half1):
		# o elmento i na lista L recebe o elemento do sub array
		# igual ao primeiro + i, pois o sub array é falso, sendo
		# delimitado apenas pelos indices recebidos como inicio e fim
		L[i] = array[first+i]
	# preenchendo os elementos da metade direita do array
	for j in range(half2):
		# mesma explicação acima
		R[j] = array[mid+j+1]
	'''
	Agora vamos "criar" um novo array ordenado, intercalando os 
	elementos das duas metades criadas, L e R, de forma crescente.
	Na pratica, vamos estar apenas sobrescrevendo no array original
	com os elementos dos dois sub arrays escolhendo o menor dos dois
	e passando adiante, até que todos tenham sido escrevidos no array.
	'''
	# variaveis de controle do indice atual do sub array
	lft = 0 # controle do sub array esquerdo
	rgt = 0 # controle do sub array direito
	# for para percorrer todo o array recebido do inicio ao fim
	for k in range(first, last+1):
		# verificando se a variavel de controle do array esquerdo
		# é maior que o tamanho so sub array esquerdo. Caso seja,
		# significa que todos os elementos do sub array ja foram
		# selecionado e escrito no array orignial.
		if lft>=half1:
			# portanto, inserir apenas os elementos restantes do array direito
			# não é necessario verificar tamanhos, pois o algoritmo garante
			# que os dois sub arrays ja estejam ordenados antes de chegarem aqui
			# então, se os elementos da esquerda ja foram todos selecionados,
			# significa que todos os elementos restantes ja estão em ordem.
			array[k] = R[rgt]
			# incrementando a variavel de controle da direita
			rgt = rgt+1
		# verificando se a variavel de controle do array direito
		# a explicação é a mesma acima
		elif rgt>=half2:
			# inserindo apenas os elementos restantes do array esquerdo
			array[k] = L[lft]
			# incrementando a variavel de controle da esquerda
			lft = lft+1
		# caso ainda reste elementos nos dois sub arrays
		else:
			# se o da esquerda for menor ou igual ao da direita (atuais)
			if (L[lft] <= R[rgt]):
				# o elemento da esquerda é escrito no array original
				array[k] = L[lft]
				# e incrementa-se a variavel de controle da esquerda
				lft = lft+1
			# senão, o da direita é maior
			else:
				# o elemento da direita é escrito no array original
				array[k] = R[rgt]
				# e incrementa-se a variavel de controle da direita
				rgt = rgt+1
	# fim do algortimo, os dois sub arrays foram combinados em um só

def MergeSort(array, first, last):
	# enquanto houver mais de 1 elemento no sub array
	# continua dividindo em 2
	if first<last:
		# calculando o ponto onde dividir o array atual (metade)
		mid = int((first+last)/2)
		# chamando recursivamente o algoritmo para os 2 novos sub arrays

		# sub array esquerdo
		MergeSort(array, first, mid)
		# sub array direito
		MergeSort(array, mid+1, last)
		# realizando a combinação dos dois sub arrays, agora ja ordenados
		# e gerando um unico sub array ordenado contendo os elementos
		# de ambos o sub arrays
		merge(array, first, mid, last)

########### code ##############
array = loadEntry(RANDOM, N_1k)

print("Tamanho da entrada: " + str(len(array)))
print("Entrada: " + str(array))
print("\n")
# guardando o tempo de inicio do algoritmo
start = timeit.default_timer()
# executando o algoritmo
MergeSort(array, 0, len(array)-1)
# gurdando o tempo de término do algoritmo
end = timeit.default_timer()
print("\n\n")
print(array)
print("\nTempo de execução: %f\n" % (end - start))