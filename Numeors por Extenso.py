numExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 
              'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
                'dezoito', 'dezenove', 'vinte');

while True:
    num = int(input('Digite um número de 0 a 20: '));
    if num < 0 or num > 20:
        print('Número inválido, tente novamente\n');
    else:
        print(f'Você digitou {numExtenso[num]}')
        break;