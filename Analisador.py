# Algoritimo feito para analisar nome, idade e sexo de 4 pessoas e retornar:
# A média das idades
# O homem mais velho
# Quantas mulheres tem menos de 20 anos

idade = [0,1,2,3];
nome = ["0","1","2","3"];
sexo = ["0","1","2","3"];
somaIdade = 0;
contMulher = 0;
idadeHomemVelho = 0;
contHomemVelho = 0;
for cont in range(0, 4):
    print(f'\n-------- {cont+1}° PESSOA --------')
    nome[cont] = str(input('Digite seu nome:'))
    idade[cont] = int(input('Digite sua idade: '))
    sexo[cont] = str(input('Digite seu sexo [M/F]: '))
    somaIdade = somaIdade + idade[cont]

    if sexo[cont] in 'Ff' and idade[cont]<20:
        contMulher = contMulher + 1;
    if sexo[cont] in 'Mm' and idade[cont] > idadeHomemVelho:
        idadeHomemVelho = idade[cont]
        contHomemVelho = cont;

print(f'A média das idades é {somaIdade/4}');
print(f'O homem mais velho é {nome[contHomemVelho]}, com {idadeHomemVelho} anos');
print(f'{contMulher} mulheres tem menos de 20 anos');
