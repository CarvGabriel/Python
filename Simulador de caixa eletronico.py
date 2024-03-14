saldo = 0;
while True:
    escolha = str(input('\n\nDeseja sacar ou depositar? [S/D] '))

    if escolha in 'Dd':
        while True:
            valDep = float(input('\nDigite o valor a ser depositado: '))
            saldo = saldo + valDep
            print(f'Foram depositados R${valDep} em sua conta.')
            print(f'Seu saldo é de R${saldo}.')
            if valDep == 0:
                break;
    else:
        if escolha in 'Ss':
            while True:
                valSac = 0;
                cont100 = 0;
                cont50 = 0;
                cont20 = 0;
                cont10 = 0;
                cont5 = 0;
                cont2 = 0;
                cont1 = 0;
                valSac = int(input('\nDigite o valor a ser sacado: '))
                if valSac == 0:
                    break;
                if valSac > saldo:
                    print('Saldo insuficiente.')
                    print(f'Seu saldo é de R${saldo}');
                else:
                    saldo = saldo - valSac
                    while valSac >= 100:
                        cont100 += 1
                        valSac = valSac - 100;
                    while valSac >= 50:
                        cont50 += 1
                        valSac = valSac - 50;
                    while valSac >= 20:
                        cont20 += 1
                        valSac = valSac - 20;
                    while valSac >= 10:
                        cont10 += 1
                        valSac = valSac - 10;
                    while valSac >= 5:
                        cont5 += 1
                        valSac = valSac - 5;
                    while valSac >= 2:
                        cont2 += 1
                        valSac = valSac - 2;
                    while valSac >= 1:
                        cont1 += 1
                        valSac = valSac - 1;
                if cont100 > 0:
                    print(f'{cont100} notas de R$100.');
                if cont50 > 0:
                    print(f'{cont50} notas de R$50.');
                if cont20 > 0:
                    print(f'{cont20} notas de R$20.');
                if cont10 > 0:
                    print(f'{cont10} notas de R$10.');
                if cont5 > 0:
                    print(f'{cont5} notas de R$5.');
                if cont2 > 0:
                    print(f'{cont2} notas de R$2.');
                if cont1 > 0:
                    print(f'{cont1} notas de R$1.');
        else:
            print('Opção inválida')