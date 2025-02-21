#1 - limpando terminal
import os
os.system ("clear")


#2 - solicitando dados ao usuario
print("""
------------- Menu -------------
|Código|  \t|Prato \t\t\t|Valor
1|   \t\t|Picanha  \t\t|25,00
2|   \t\t|Lasanha  \t\t|20,00
3|   \t\t|Strogonoff \t\t|18,00
4|   \t\t|Bide Acebolado  \t|15,00
5|   \t\t|Pão com ovo  \t\t|5,00
--------------------------------          
""")  

opcao = (input("Digite o Código do pedido: "))

print("------------- Pedido -------------")

match opcao:
    case "1":
        print("Picanha R$25,00")
    case "2":
        print("Lasanha R$20,00")
    case "3":
        print("Strogonoff R$18,00")
    case "4":
        print("Bife Acebolado R$15,00")
    case "5":
        print("Pão com ovo R$5,00")

#3 - verificando o maior e o menor.



#4 - exibindo resultados