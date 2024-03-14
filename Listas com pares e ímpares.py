num = [[],[]];
valor = 0;
for c in range(0,7):
    valor = int(input(f'Digite o {c+1}° número: '))
    if valor%2 == 0:
        num[0].append(valor);
    else:
        num[1].append(valor);

num[0].sort();
num[1].sort();
print(f'os numeros pares são: {num[0]}');
print(f'os numeros impares são: {num[1]}');