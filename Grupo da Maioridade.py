import datetime

contMaior = 0;
contMenor = 0;
anoNascimento = 0;
idade = 0;
hoje = datetime.date.today().year;

for cont in range(0, 7):
    anoNascimento = int(input(f'Digite o ano de nascimento da {cont+1}° pessoa: '))
    idade = hoje - anoNascimento
    if idade < 18:
        contMenor += 1;
    else:
        contMaior += 1;

print(f'\n{contMaior} pessoas são maiores de idade.');
print(f'{contMenor} pessoas são menores de idade.');
