#Estrutura enquanto em Python

##SINTAXE
#while condição:
# comando1
# comando2 

soma = 0

x = int(input("Digite o primeiro numero: "))

while x != 0:
 soma = soma + x
 x = int(input("Digite outro numero: "))

print("SOMA = ", soma) 