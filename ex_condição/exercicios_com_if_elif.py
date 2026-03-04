#Média Aritmética com IF

print("EXERCÍCIO - MÉDIA ARITMÉTICA COM IF")

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

media = (n1+n2)/2

if media >= 7:
    print(f'A nota 1 foi {n1}, a nota 2 foi {n2}, e a média foi {media:.2f}. "Aluno Aprovado"')
else:
    print(f'A nota 1 foi {n1}, a nota 2 foi {n2}, e a média foi {media:.2f}. "Aluno Reprovado"')

print("-"*100)
print("-"*100)

#COMPRA COM DESCONTOS IF + CONDIÇÃO ANINHADA (ELIF)

print("EXERCÍCIO - COMPRA COM DESCONTOS")

compra = float(input("Digite o valor da compra: "))

if compra > 500:
    print(f'O valor do desconto é 30% e você pagará somente R$ {(compra*0.7):.2f}.')
elif compra > 200:
    print(f'O valor do desconto é 20% e você pagará somente R$ {(compra*0.8):.2f}.')
elif compra > 100:
    print(f'O valor do desconto é 10% e você pagará somente R$ {(compra*0.9):.2f}.')
else:
    print(f'O valor da sua compra é R$ {compra:.2f}.')

print("-"*100)
print("-"*100)

#CRIME / TELEFONEMA - IF e ELIF

print('CRIME / TELEFONEMA - IF e ELIF')

cont = 0
perg1 = str(input("Telefonou para a vítima? "))
perg2 = str(input("Esteve no local do crime? "))
perg3 = str(input("Mora perto da vítima? "))
perg4 = str(input("Devia para a vítima? "))
perg5 = str(input("Já trabalhou para a vítima? "))

if perg1 == "SIM":
    cont += 1
if perg2 == "SIM":
    cont += 1
if perg3 == "SIM":
    cont += 1
if perg4 == "SIM":
    cont += 1
if perg5 == "SIM":
    cont += 1
if cont == 2:
    print("Suspeito")
elif cont == 3 or cont == 4:
    print("Cúmplice")
elif cont == 5:
    print("Culpado")
else:
    print("Inocente")