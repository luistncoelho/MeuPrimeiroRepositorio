#EXERCÍCIOS DE FIXAÇÃO - LISTA 1

print("EXERCÍCIOS DE FIXAÇÃO - LISTA 1")

print('-'*100)
print('-'*100)

#EXERCÍCIO 1 - ARITMÉTICOS

print("ARITMÉTICOS")

n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
soma = n1 + n2
dif = n1 - n2
prod = n1 * n2
div = n1 / n2
parteint = n1 // n2
resto = n1 % n2

print(f'Soma: {soma}')
print(f'Diferença: {dif}')
print(f'Produto: {prod}')
print(f'Divisão: {div:.2f}')
print(f'Inteiro: {parteint}')
print(f'Resto: {resto}')

print('-'*100)
print('-'*100)

#EXERCÍCIO 2 - ATRIBUIÇÃO

print("ATRIBUIÇÃO")

saldo = float(input("Digite o valor do Saldo: "))
dep = float(input("Digite o valor do depósito: "))
saque = float(input("Digite o valor do saque: "))
saldo += dep
saldo -= saque 
rend = saldo * 2

print(f'O valor atual é de: R$ {rend:.2f}')

print('-'*100)
print('-'*100)

#EXERCÍCIO 3 - COMPARAÇÃO

print("EXERCÍCIO 3 - COMPARAÇÃO")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print(f'Os números são iguais? {n1 == n2}')
print(f'O primeiro é maior do que o segundo? {n1 > n2}')
print(f'Os números são diferentes? {n1 != n2}')

print('-'*100)
print('-'*100)

#EXERCÍCIO 4 - LÓGICOS

print("EXERCÍCIO 4 - LÓGICOS")

presenca = int(input("Digite a presença do aluno: "))
media = float(input("Digite a media do aluno: "))

aprov = presenca >= 75 and media >= 7 #True (1) ; False (0)

reprov = presenca <=75 or media <=7

print(f'Aluno(a) está {aprov * "APROVADO"}{reprov * "REPROVADO"}')

print('-'*100)
print('-'*100)

#EXERCÍCIO 5 - IDENTIDADE

print("EXERCÍCIO 5 - IDENTIDADE")

list1 = [1, 2]
list2 = [1, 2]
c = list1

print(f'A lista 1 é igual a Lista 2? {list1 is list2}')
print(f'A lista c é igual a Lista 1? {c is list1}')
print(f'A lista c é igual a Lista 2? {c is list2}')

print('-'*100)
print('-'*100)

#EXERCÍCIO 6 - IDENTIDADE

print("EXERCÍCIO 6 - ASSOCIAÇÃO")

frase = "Ciência de Dados Python"
contido = "d" in frase
naocontido = "Python" not in frase 
print(contido)
print(naocontido)

print(f'{contido * "A letra 'D' está contina na frase."}')

print(f'{naocontido * "A palavra 'Python' não está contida na frase."}')

print('-'*100)
print('-'*100)

#EXERCÍCIO 7 - CONDICIONAL (IF - ELIF - ELSE)

print("EXERCÍCIO 7 - CONDICIONAL")

idade = int(input("Digite a sua idade: "))

if idade >= 5 and idade <= 12: 
    print("Categoria INFANTIL")
if idade >=13 and idade <= 17:
    print("Categoria JUVENIL")
if idade >= 18: 
    print("Categoria ADULTO")
else:
    print("INVÁLIDO")

print('-'*100)
print('-'*100)

#EXERCÍCIO 8 - REPETIÇÃO FOR

print("EXERCÍCIO 8 - FOR")

n = int(input("Digite um número inteiro: "))

for c in range(0, 11):
    print(f'{n} x {c} = {c*n}')

print('-'*100)
print('-'*100)

#EXERCÍCIO 9 - REPETIÇÃO WHILE

print("EXERCÍCIO 9 - REPETIÇÃO WHILE")

senha = str(input("Digite a sua senha: "))

while senha != "python123":
    print("Senha Inválida.")
    senha = str(input("Digite a sua senha: "))
print("Acesso Permitido.")

print('-'*100)
print('-'*100)