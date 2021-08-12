try:
    a = float(input("Digite o primeiro número ")) #ValueError
    b = float(input("Digite o segundo número "))  #ValueError

    print(a/b) #ZeroDivisionError
except ValueError as error:
    print('Digite apenas números')
except ZeroDivisionError as error:
    print('Não pode ser feita divisão por zero')
except Exception as error:
    print('Algum erro ocorreu')
    print(error)
finally:
    print('Fim do programa')