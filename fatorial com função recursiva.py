def fatorial(n):
    if n == 1:
        n = 1
    else:
        n = n*fatorial(n-1)
    return n;


numero = int(input('Digite um número inteiro: '))
print(f'o seu fatorial é {fatorial(numero)}.')