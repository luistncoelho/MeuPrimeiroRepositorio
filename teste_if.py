# TESTE IF

idade = int(input("Digite a sua idade: "))

if idade > 60:
    print("Idoso")
elif idade >=18:
    print("Adulto")
elif idade >=12:
    print("Adolescente")
else:
    print("Criança")