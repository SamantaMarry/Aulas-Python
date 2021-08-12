#sempre que for abrir um arquivo colocar um try e except para caso coloque a exteção do arquivo errado

try:
    arquivo = open('emails.txt', 'w') #sempre abre o arquivo em mode de leitura, para abrir em modo escrita colocar o 'W' se for arquivo executavel, JPG, DOC, PDF, etc abrir com 'b' pq é um binário
except FileNotFoundError:
    print('Arquivo não encontrado')
except:
    print('Algum erro encontrado')
finally:
    arquivo.close() #sempre que abre um arquivo tem que fechar ele


try:# coloca dentro de um try no caso de arquivo errado
    with open('emails.txt') as arquivo: # abre o arquivo dentro do with e automaticamente já fecha ele
        print(arquivo.readline())
except FileNotFoundError:
    print('Arquivo não encontrado')



conteudo = arquivo.readline() #le as linhas e transforma em uma lista

print(conteudo)

print('Samanta\n''Britto') #mostra sem os espacos

for linha in conteudo:
    print(linha.strip()) #tira os espaços