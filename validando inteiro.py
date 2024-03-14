def validarInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric() == True:
            n= float(n)
            if n%1 == 0:
                n= int(n)
                break
        else:
            print('Resposta Inválida!')
    return n


numero = validarInt('Digite um inteiro: ')
print(f'você digitou {numero}')