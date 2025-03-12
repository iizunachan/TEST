#1 - limpando terminal
import os
os.system ("clear")


#2 - solicitando dados ao usuario

nome_produto = input("Digite o Nome do Produto: ")
quantidade_produto = int(input("Digite a Quantidade do Produto: "))
preco_produto = float(input("Digite o Preço do Produto: "))

total = preco_produto * quantidade_produto

#3 - verificando o maior e o menor.
print("---------------------------------------------------------------")
if quantidade_produto <= 5:
    desconto = 0.02
elif quantidade_produto <=10:
    desconto = 0.03
else:
    desconto = 0.05

desconto_total = desconto * total
total_pagar = total - desconto_total      

 #4 - exibindo
 
print(f"Produto: {nome_produto}")
print(f"Total: R$ {total:.2f}")
print(f"Desconto: R$ {desconto_total:.2f}")
print(f"Total a pagar: R$ {total_pagar:.2f}")