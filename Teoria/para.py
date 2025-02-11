#Estrutura "para" em Python 

#É representado pelo "for"

##REGRA 
#Primeira vez: variavel assume o valor_inicial
#Repetição: se a variavel for menor que valor_final, executa e repete, senão pula fora
# Na volta: incrementa a variavel de 1 ou do valor do passo se houver

##SINTAXE
# for variavel in range(valor_inicial, valor_final, [passo]):
#  comando1
#  comando2 

N = int(input("Quantos numeros serao digitados? "))

soma = 0
for i in range(0, N):
 x = int(input("Digite um numero: "))
 soma = soma + x
print("SOMA = ", soma) 