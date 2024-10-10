dic = {}
cont = 0

while True:
    print(f'Produto {cont + 1}')
    codigo = str(input('Digite o código: '))
    if codigo == '':
        print('\n')
        break
    if codigo in dic:
        print('Esse produto ja existe!\n')
        continue

    nome = str(input('Digite o nome: '))    
    preco = float(input('Digite o preço: '))
    print('')
    dic[codigo] = (nome, preco)
    cont += 1

for cod, desc in dic.items():
    print(f'Código: {cod}  Nome: {desc[0]}  Preço: R$ {desc[1]}')