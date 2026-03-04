#EXERCÍCIO 1  - OPERADORES + CONDICIONAIS

print("EXERCÍCIO 1  - OPERADORES + CONDICIONAIS")

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / altura **2
print(imc)

if imc < 18.5:
    print("Abaixo do peso.")
elif imc >= 18.5 and imc <=24.9:
    print("Peso normal.")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso.")
else:
    print("Obesidade.")

#EXERCÍCIO 2 - FOR + OPERADORES DE ASSOCIAÇÃO

print("EXERCÍCIO 2 - FOR + OPERADORES DE ASSOCIAÇÃO")

vogais = "aeiouáéíóúãõâêîôû"
frase = str(input("Digite uma frase ou o seu nome completo: ")).strip().lower()
cont = 0

for c in frase:
    if c in vogais:
        cont += 1
print(f"A frase/nome digitado contém {cont} vogais.")

#EXERCÍCIO 3 - WHILE + CONDICIONAIS + ATRIBUIÇÃO

print("EXERCÍCIO 3 - WHILE + CONDICIONAIS + ATRIBUIÇÃO")

option = 0
valor = 0
saldo = 500

while option != 3:
    print(f'O saldo atual é de R$ {saldo}')
    option = int(input("Digite a opção desejada:\n(1) Depositar\n(2) Sacar\n(3) Sair\n"))
    print("-"*50)
    if option == 1:
        valor = float(input("Digite o valor do depósito: "))
        saldo += valor
        print("-"*50)
    elif option == 2:
        valor = float(input("Digite o valor a sacar: "))
        if valor > saldo:
            print(f"Saldo Insuficiente. O saldo atual é de R$ {saldo}")
            print("-"*50)
        else:
            saldo -= valor
            print("-"*50)
    if option == 3:
        print(f"O saldo final é de R$ {saldo}")
        break
print("-"*50)
print("Você saiu do sistema")

#EXERCÍCIO 4 - IDENTIDADE + COLEÇÕES SIMPLES

print("EXERCÍCIO 4 - IDENTIDADE + OPERAÇÕES SIMPLES")

lista = [10, 20, 30]
ref = lista
copia = [10, 20, 30]

print(f'A referência é {(ref is lista)*"IGUAL"}')
print(f'A cópia é {(copia is not lista)*"DIFERENTE"}')