nome=[];
peso=[]
cont = 0;
maiorPeso = 0;
menorPeso = 1000;
pessoaMaior = [];
pessoaMenor = [];
while True:
    n = str(input('Nome: '))
    p = float(input('Peso: '))
    nome.append(n)
    peso.append(p)
    condicao = str(input('Quer continuar? [S/N] '))
    cont += 1

    if peso[cont-1] > maiorPeso:
        maiorPeso = peso[cont-1]
        pessoaMaior.clear()
        pessoaMaior.append(nome[cont-1])
    else:
        if maiorPeso == peso[cont-1]:
            pessoaMaior.append(nome[cont-1])

    if peso[cont-1] < menorPeso:
        menorPeso = peso[cont-1]
        pessoaMenor.clear()
        pessoaMenor.append(nome[cont-1])
    else:
        if menorPeso == peso[cont-1]:
            pessoaMenor.append(nome[cont-1])

    if condicao in 'Nn':
        break;
print(f'Foram cadastradas {cont} pessoas.')
print(f'As pessoas com maior peso é ', end='')
for c in pessoaMaior:
    print(f'{c}, ', end='');
print(f'\nAs pessoas com menor peso é ', end='')
for c in pessoaMenor:
    print(f'{c}, ', end='')