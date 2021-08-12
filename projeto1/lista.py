nome = 'Samanta' #STRING
idade = 28 #VALOR

minha_lista = ['azul', 'amarelo', 'vermelho', 'rosa', 'cinza', 'verde'] # LISTA DE CORES

minha_lista[1] = 'branco' #SUBSTITUIR UM ELEMNTO DA LISTA, NESTE CASO O 1 (AZUL)
minha_lista.append('roxo') #ADICIONA ITENS NA LISTA
minha_lista.remove('azul') #REMOVE ITENS DA LISTA

for cor in minha_lista:
    print(cor) #MOSTRA A LISTA POR LINHAS

print(minha_lista[1:3]) #MOSTRA ITENS ESPECIFICOS DA LISTA
for letra in nome:
    print(letra) #MOSTRA AS LETRAS POR LINHA

