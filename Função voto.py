def voto(ano):
    import datetime

    hoje = datetime.date.today().year
    idade = hoje - ano
    if idade < 16:
        print(f'você tem {idade} anos, voto NEGADO!')
    elif idade >= 18 and idade < 65:
        print(f'você tem {idade} anos, voto OBRIGATÓRIO!')
    else:
        print(f'você tem {idade} anos, voto OPCIONAL!')


anoNascimento = int(input('Digite seu ano de nascimento: '))
voto(anoNascimento)