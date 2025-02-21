#1 - limpando terminal
import os
os.system ("clear")


#2 - solicitando dados ao usuario

primeiro_numero = int(input("Digite o Primeiro Número: "))
segundo_numero = int(input("Digite o Segundo Núemero: "))
sinal = (input("Digite o Sinal +, -, *, / ou % : "))


#3 - verificando o maior e o menor.

match sinal:
    case "+":
        print (primeiro_numero + segundo_numero)
    case "-":
        print (primeiro_numero - segundo_numero)
    case "*":
        print (primeiro_numero * segundo_numero)
    case "/":
        print (primeiro_numero / segundo_numero)
    case "%":
        print (primeiro_numero % segundo_numero)


#4 - exibindo resultados