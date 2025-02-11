#Saída de dados em Python

#Comando: "print"

print("Olá mundo!")

##Placeholde de formatação - não é muito usual e atualmente não é recomendada
# int : %d
# float : %f
# str : %s

x = "Maria"
y = 19

print("%s tem %d anos" %(x,y))

#Exemplo

idade: int
salario: float
nome: str
sexo: str

idade = 32
salario = 4560.9
nome = "Maria Silva"
sexo = "F" 

print(f"A funcionaria {nome}, sexo {sexo}, ganha {salario:.2f} e tem {idade} anos")