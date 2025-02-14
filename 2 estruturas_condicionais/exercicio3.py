import os
os.system("clear")

numero1 = float(input("Digite a primeira nota: "))
numero2 = float(input("Digite a segunda nota: "))
numero3 = float(input("Digite a terceira nota: "))

media = (numero1 + numero2 + numero3) /3

if media > 7:
    resultado = ("APROVADO! :)")
else:
    resultado = ("REPROVADO! :(")

print("------------------------------------------------")
print(f"Média: {media}")
print(f"Resultado: {resultado}")