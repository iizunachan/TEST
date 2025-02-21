#1 - limpando terminal
import os
os.system ("clear")


#2 - solicitando dados ao usuario

primeiro_numero = int(input("Digite o Primeiro Número: "))
segundo_numero = int(input("Digite o Segundo Núemero: "))
terceiro_numero = int(input("Digite o Terceiro Núemero: "))

#3 - verificando o maior e o menor.

maior = max(primeiro_numero, segundo_numero, terceiro_numero)
menor = min(primeiro_numero, segundo_numero, terceiro_numero)

#4 - exibindo resultados
print("------------------------------------------")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
