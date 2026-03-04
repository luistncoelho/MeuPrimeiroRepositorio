#Exercícios com Operadores

#POSITIVO - NEGATIVO - ZERO

n = float(input("Digite um número qualquer: "))

resultado = ("Negativo" * (n < 0)) or ("Positivo" * (n > 0)) or ("Zero" * (n == 0))

print("Classificação", resultado)

print("-"*50)
print("-"*50)

#POSITIVO - NEGATIVO - ZERO

n = float(input("Digite um número qualquer: "))

resultado = ("Par" * (n % 2 == 0)) or ("Ímpar" * (n % 2 != 0))

print("Classificação", resultado)