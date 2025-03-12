import os
os.system("clear")


preco_gasolina = 6.59
preco_alcool = 3.79

litros = float(input("Digite o número de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A - Álcool, G - Gasolina): ").strip().upper()


if tipo == "A":
    preco_litro = preco_alcool
    desconto = 0.02 if litros <= 25 else 0.04
elif tipo == "G":
    preco_litro = preco_gasolina
    desconto = 0.03 if litros <= 25 else 0.05
else:
    print("Tipo de combustível inválido.")
    exit()

valor_bruto = litros * preco_litro
valor_desconto = valor_bruto * desconto
valor_final = valor_bruto - valor_desconto
print ("----------------------------------------------------------")
print(f"Valor a ser pago: R$ {valor_final:.2f}") 