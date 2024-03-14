import datetime

anoNascimento = int(input('Digite o ano de nascimento: '));
hoje = datetime.date.today().year;
idade = hoje - anoNascimento;
anosRestantes = 18 - idade;

print(f'\nVocê está com {idade} anos.');

if idade < 18:
    print(f'Realize o alistamento daqui {anosRestantes} anos, em {hoje + anosRestantes}');
else:
    if idade > 18:
        print(f'Deveria ter feito o alistamento a {anosRestantes*-1} anos, em {hoje + anosRestantes}');
    else:
        print(f'Você deverá realizar o alistamento esse ano, em {hoje}');