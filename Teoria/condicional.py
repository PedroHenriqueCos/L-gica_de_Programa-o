#Estrutura condicional em Python

# "if (se)", "else (senao)" e "elif"

##SIMPLES - sintaxe
# if condição:
#  comando1
#  comando2 

##COMPOSTA - sintaxe
# if condição:
#  comando1
#  comando2
# else:
#  comando3
#  comando4 

##ENCADEAMENTO - sintaxe
# if condição1:
#  comando1
#  comando2
# elif condição2:
#  comando3
#  comando4
# else:
#  comando5
#  comando6 

print("Exercício")
print()

hora = int(input("Digite uma hora do dia: "))

if hora < 12:
 print("Bom dia!")
elif hora < 18:
 print("Boa tarde!") 
else:
 print("Boa noite!") 