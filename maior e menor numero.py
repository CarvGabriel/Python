import random

numeros = (random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9));
maiorNum = 0;
menorNum = 9;

for cont in numeros:
    if cont > maiorNum:
        maiorNum = cont;
    if cont < menorNum:
        menorNum = cont;

print(f'Os números sorteados foram: ', end='');
for n in numeros:
    print(f'{n} ',end='');

print(f'\nO menor numero é {menorNum}');
print(f'O maior numero é {maiorNum}');

# forma mais simples:
# print(f'O menor numero é {max(numeros)}');
# print(f'O maior numero é {min(numeros)}');