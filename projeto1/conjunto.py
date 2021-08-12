conjunto_cores = {'vermelho', 'azul', 'verde'} #CONJUNTO NÃO É ORDENADO - NÃO É UMA LISTA ORDENADA - NÃO SUPORTA INDICE

conjunto_cores.add("branco") #ADICIONAR ITENS (NÃO ADICIONA ITENS REPETIDOS, ELE FILTRA PARA VOCÊ)
conjunto_cores.remove("azul") #REMOVER ITENS

#ACESSA PELO 'FOR'
for cor in conjunto_cores:
    print(cor) #MOSTRA POR LINHA

print(conjunto_cores)
