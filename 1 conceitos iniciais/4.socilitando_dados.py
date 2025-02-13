import os

# limpa o terminal.
os.system("clear")

print("Olá Mundo")

#solicitando dados do usuario
nome = input("Digite Seu Nome: ")
idade = int(input ("Digite sua idade: "))
altura = float(input ("Digite sua altura: "))
peso = float(input ("Digite seu peso: "))

print("")
print("-------------------------------------------------------------------")
print("")

#exibindo dados do usuario
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Alura: {altura}")
print(f"Peso: {peso}")
