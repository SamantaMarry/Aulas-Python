# Erros em tempo de compilação - quando vai executar o código e ele nem executa ou o erro aparece no decorrer da execução
# Erros em tempo de execução - erro quando o código está executando
# Erros de Lógica -  falou que a função faria uma coisa e ela ta fazendo outra

def divisao(a, b):
    try:
        print(a/b)
    except Exception as e:
        print('Divisão inválida')
        print(e)

divisao(30, 0)


