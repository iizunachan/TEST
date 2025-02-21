#limpando terminal
import os
os.system ("clear")


#solicitando dados ao usuario

primeiro_numero = int(input("Digite o Primeiro Número: "))
segundo_numero = int(input("Digite o Segundo Núemero: "))

#verificando o maior e o menor.

if primeiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero

#exibindo resultados
print()
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
