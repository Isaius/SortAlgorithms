# SortAlgorithms

Implementação dos mais conhecidos algoritmos de ordenação para um trabalho de univerisdade, para a disciplina de Projeto e Análise
Algoritmos. 
Os algoritmos são:
  1. Insertion Sort
  2. Bubble Sort
  3. Merge Sort
  4. Heap Sort
  5. Quick Sort

Os códigos recebem as entradas de arquivos de texto contendo 100, 500, 1k, 5k, 30k, 80k, 100k, 150k e 200k de entradas, sendo elas
números gerados por um outro programa feito apenas de suporte.

Há três tipos de entradas, classificadas pelo tipo de ordenação em que estão: Crescente, Decrescente e Randômicas. Todas tem um
exemplo de cada tamanho citado anteriormente. Vale notar que foi estipulado um intervalo do dobro do tamanho da entrada para a geração
randômica dos números a serem inseridos nos arquivos. A escolha foi feita para possibilitar uma maior variedade de números e reduzir
a quantidade de repetidos e tentar impossibilitar o acontecimento de um pior caso, que seria a entrada já estar ordenada, o que é bem
improvável, mas na computação não deve se contar com incertezas. Porém a possibilidade ainda existe, a estatística prova. Também vale
dizer que sim, não se deve manipular as entradas, mas como o pior caso ja seria testado com o tipo de entrada específico, é mais desejável
que ele não aconteça aqui, no teste de valores aleatórios.

O objetivo do trabalho é realizar a comparação prática entre os algoritmos e após a análise criar um Algoritmo de Ordenação Híbrido
que júlgasse melhor para atender às entradas e justificar a escolha.

Optei por utilizar as mesmas entradas em todos eles para obter um resultado mais consistente entre eles. No caso das entradas do tipo
randômico, foram gerados e testados com vários arquivos, no mínimo 3 arquivos diferentes para cada tamanho.
