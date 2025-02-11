import math
#Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor da área, perímetro e diagonal deste retângulo, com quatro casas decimais, conforme exemplos.

base = float(input("Base do retangulo: "))
altura = float(input("Altura do retangulo: "))

area = base * altura 
perimetro = 2 * (base + altura)
diagonal = math.sqrt(base ** 2 + altura ** 2)

print(f"AREA = {area:.2f}")
print(f"PERIMETRO = {perimetro:.2f}")
print(f"DIAGONAL = {diagonal:.2f}")
