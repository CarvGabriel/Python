valCasa = float(input("Valor da casa: "));
salario = float(input("Sálario do comprador: "));
parcelas = int(input("Parcelas para pagar: "));

valParcela = valCasa/parcelas;

if valParcela <= salario * 0.3:
    print(f'Emprestimo APROVADO, vc pagará {valParcela:.2f}R$ durante {parcelas} meses');

else:
    print(f'Emprestimo NEGADO, vc teria que pagar {valParcela:.2f}R$ durante {parcelas} meses');