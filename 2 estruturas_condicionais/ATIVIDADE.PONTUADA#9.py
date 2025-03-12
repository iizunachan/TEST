import os
os.system("clear")

#solicitando dados
renda_mensal = float(input("Digite sua renda mensal: "))
valor_emprestimo = float(input("Digite o valor total do empréstimo solicitado: "))
numero_prestacoes = int(input("Digite o número de prestações: "))

limite_emprestimo = renda_mensal * 10
prestacao_maxima = renda_mensal * 0.30

valor_prestacao = valor_emprestimo / numero_prestacoes

tem_limite_emprestimo = valor_emprestimo <= limite_emprestimo
tem_limite_prestacao = valor_prestacao <= prestacao_maxima
print ("----------------------------------------------------------|")
if tem_limite_emprestimo and tem_limite_prestacao:
    print("Empréstimo concedido!")
else:
    print("Empréstimo negado!")
