
try:
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite outro numero: '))

    divisao = n1 / n2

    print(f'\nO valor da divisao é {divisao}')

except ZeroDivisionError:
    print('\nO segundo número não pode ser 0')

except ValueError:
    print('\nDeve ser digitado um número inteiro')

except:
    print('\nNão foi possível calcular')