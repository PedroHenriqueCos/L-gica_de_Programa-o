#Matriz em Python 

##SINTAXE
# minha_matriz: [[tipo]] = [[0 for x in range(numero_de_colunas)] for x in range(numero_de_linhas)]

M = int(input("Quantas linhas vai ter a matriz? "))
N = int(input("Quantas colunas vai ter a matriz? "))

mat = [[0 for x in range(N)] for x in range(M)]
for i in range(0, M):
 for j in range(0, N):
  mat[i][j] = int(input(f"Elemento [{i},{j}]: "))
print()

print("MATRIZ DIGITADA:")
for i in range(0, M):
 for j in range(0, N):
    print(f"{mat[i][j]} ", end="")
 print()
