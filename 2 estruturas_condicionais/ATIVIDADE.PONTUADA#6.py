import os
os.system("clear")

numero1 = float(input("Digite a primeira nota: "))
numero2 = float(input("Digite a segunda nota: "))

media = (numero1 + numero2) /2

if media > 6:
    resultado = ("APROVADO! :)")
if media == 6:
    resultado = ("APROVADO! :)")    
if media < 4:
    resultado = ("REPROVADO! :(")
if media == 4:
    resultado = ("RECUPERAÇÃO! :(")    

print("------------------------------------------------")
print(f"Média: {media}")
print(f"Resultado: {resultado}")