pessoas = {
    'samanta': 28, #CHAVE E VALOR - STRING E INTEIRO
    'maria': 25, #CHAVE E VALOR - STRING E INTEIRO
    'joão': 17, #CHAVE E VALOR - STRING E INTEIRO
}

print(pessoas) #MOSTRA OS ELEMENTOS

print(pessoas['samanta']) #MOSTRA O VALOR DAQUELA PESSOA

for pessoa in pessoas: #MOSTRA AS CHAVES
    print(pessoa)

for pessoa in pessoas.values(): #MOSTRA OS VALORES
    print(pessoa)


