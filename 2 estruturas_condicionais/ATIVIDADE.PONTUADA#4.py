#limpando terminal
import os
os.system ("clear")


#solicitando dados ao usuario

preco_morango = 2.50
preco_maca = 1.80

morango_kg = float(input("Digite a Quantidade de Morangos em (KG) : "))
maca_kg = float(input("Digite a Quantidade de Maças em (KG) : "))

#verificando o maior e o menor.

print("-----------------------------------------")
if morango_kg > 5:
    preco_morango = 2.20
if maca_kg > 5:
    preco_maca = 1.50

#-------------------------------------
valor_total = (morango_kg * preco_morango) + (maca_kg * preco_maca)

peso_total = morango_kg + maca_kg

if peso_total > 10 or valor_total > 15:
    valor_total *= 0.90
 
#exibindo resultados
print("-------------------------------------------------")
print(f"Valor Total Da Compra R$ {valor_total:.2f}") 
