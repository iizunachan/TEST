#limpando terminal
import os
os.system ("clear")


#solicitando dados ao usuario

quantidade_maca = float(input("Quantas Maçãs vc Comprou? : "))

#verificando o maior e o menor.

print("-----------------------------------------")
if quantidade_maca < 12:
    preco_maca = 1.30
else:
    preco_maca = 1.00

valor_total = quantidade_maca * preco_maca

    
#exibindo resultados
print("-------------------------------------------------")
print(f"Valor Total Da Compra R$ {valor_total:.2f}")    