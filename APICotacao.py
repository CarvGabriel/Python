import requests
import json

cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacao = cotacao.json()
cotacaoDolar = cotacao["USDBRL"]["bid"]
cotacaoEuro = cotacao["EURBRL"]["bid"]
cotacaoBTC = cotacao["BTCBRL"]["bid"]

valor = float(input("Digite um valor em reais: "))

print(f'O valor em dolar é de {valor / float(cotacaoDolar)}')
print(f'O valor em euro é de {valor / float(cotacaoEuro)}')
print(f'O valor em bitcoin é de {valor / float(cotacaoBTC)}')