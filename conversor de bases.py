num = int(input('Digite um número: '));
print('Deseja converte-lo para binário [1]');
print('Deseja converte-lo para octal [2]');
print('Deseja converte-lo para haxadecimal [3]');
aux = 0;

while aux == 0:
    aux = 1;
    numBase = int(input('Escolha: '));

    if numBase == 1:
        numConvert = bin(num)[2:];
        base = 'bínario';
    else:
        if numBase == 2:
            numConvert = oct(num)[2:];
            base = 'octal';
        else:
            if numBase == 3:
                numConvert = hex(num)[2:];
                base = 'hexadecimal';
            else:
                print('Escolha inválida, tente de novo: ');
                aux = 0;

print(f'O numero em {base} é {numConvert}');