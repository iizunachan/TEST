#limpando terminal
import os
os.system ("clear")


#solicitando dados ao usuario

primeiro_numero = int(input("Digite o Primeiro Número: "))
segundo_numero = int(input("Digite o Segundo Núemero: "))

#verificando o maior e o menor.

maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)

#exibindo resultados
print()
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
