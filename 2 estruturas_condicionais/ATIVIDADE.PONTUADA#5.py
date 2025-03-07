#1 - limpando terminal
import os
os.system ("clear")


#2 - solicitando dados ao usuario

sinal = (input("Digite o Sinal +, -, *, / ou % : "))
A = int(input("Digite o Valor A: "))
B = int(input("Digite o Valor B: "))


#3 - verificando o maior e o menor.
print("---------------------------------------------------------------")
match sinal:
    case "+":
        print (A + B)
    case "-":
        print (A - B)
    case "*":
        print (A * B)
    case "/":
        print (A / B)
    case "%":
        print (A % B)