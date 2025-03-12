import os
os.system("clear")

#solicitando dados
cor = input("Digite a cor do CD: ").strip().lower()
#verificicando (processamento)
precos = {
    "verde": 10.00,
    "azul": 20.00,
    "amarelo": 30.00,
    "vermelho": 40.00
}

print("-----------------------------------------")

if cor in precos:
    print(f"O preço do CD {cor} é R$ {precos[cor]:.2f}")
else:
    print("Cor inválida. Por favor, escolha entre verde, azul, amarelo ou vermelho.")

#exibindo dados

