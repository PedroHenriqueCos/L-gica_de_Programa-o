#Vetores em Python 

##SINTAXE 
#meu_vetor: [tipo] = [0 for x in range(numero_de_elementos)]
#Vale ressaltar que o tipo é opcional

N = int(input("Quantos numeros voce vai digitar? "))

vet: [float] = [0 for x in range(N)] # type: ignore
for i in range(0, N):
 vet[i] = float(input("Digite um numero: "))
print()

print("NUMEROS DIGITADOS:")
for i in range(0, N):
 print(f"{vet[i]:.1f}") 

