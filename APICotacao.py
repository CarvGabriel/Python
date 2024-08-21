import requests
import json

cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacao = cotacao.json()
cotacaoDolar = cotacao["USDBRL"]["bid"]
cotacaoEuro = cotacao["EURBRL"]["bid"]
cotacaoBTC = cotacao["BTCBRL"]["bid"]

while True:

    print("Escolha um conversor:\n")
    print("1- Real para dolar")
    print("2- Real para euro")
    print("3- Real para bitcoin")
    print("0- Encerrar")

    escolha = input("\nDigite o número escolhido: ")

    if escolha in ("123"):
        valor = float(input("\nDigite um valor em reais: "))

        if escolha == "1":
            print(f'\nO valor em dolar é de {valor / float(cotacaoDolar)}')
        elif escolha == "2":
            print(f'\nO valor em euro é de {valor / float(cotacaoEuro)}')
        else:
            print(f'\nO valor em bitcoin é de {valor / float(cotacaoBTC)}')

    else:
        if escolha =="0":
            break
        else:
            print("\nEntrada inválida")
    
    x = input("\nPressione ENTER para continuar")
    print("\n" * 30)