#1 - limpando terminal
import os
os.system ("clear")


#2 - solicitando dados ao usuario

nome_produto = input("Digite o Nome do Produto")
quantidade_produto = int(input("Digite a Quantidade do Produto: "))
preco_produto = float(input("Digite o Preço do Produto: "))


#3 - verificando o maior e o menor.
print("---------------------------------------------------------------")
valor = (quantidade_produto * preco_produto)
if valor < 5:
    resultado = (valor - 2%)


 #4 - exibindo
 
    print(f"Resultado: {resultado}")  if