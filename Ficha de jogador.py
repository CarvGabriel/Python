def ficha(n, g):
    if  not g.isnumeric():
        g = 0
    if len(n) < 1:
        n = "<desconhecido>"
    
    print(f'O jogador {n} fez {g} gols.')


nome = str(input('nome do jogador: '))
gols = str(input('Qunatidade de gols: '))
ficha(nome, gols)