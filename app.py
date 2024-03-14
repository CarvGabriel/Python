import random

numAdiv = int(input('Adivinhe o numero que caiu no dado: '));
numDado = random.randint(1, 6);

if (numAdiv == numDado):
    print('\nAcertou o numero, parabén!');
else:
    print('\nVOCÊ PERDEU!!!');
    print(f'O numero que caiu foi {numDado}');