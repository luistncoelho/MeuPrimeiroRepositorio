
print('EXERCÍCIO COM FOR')

inicio = int(input('Digite o número inicial: '))
fim = int(input('Digite o número final: '))

for i in range(inicio, fim+1):
    if(i % 11 == 2):
        print(i)

print("-"*100)
print("-"*100)

#EXERCÍCIO COM FOR - SALÁRIO

print("EXERCÍCIO COM FOR - SALÁRIO")

salario = 1000
final = 5000
aumento = 0

print(f'Salário Inicial: {salario}')

for i in range(salario, final, 100):
    aumento += 1
    print(f'Aumento {aumento}:', end = ' ')
    salario += 100
    print(salario)


print("-"*100)
print("-"*100)

#EXERCÍCIO COM WHILE

print("EXERCÍCIO COM WHILE")

c = 0

while c < 100:
    if(c % 11 == 2):
        print(c, end=", ")
    c += 1
print("FIM")

print("-"*100)
print("-"*100)

#EXERCÍCIO COM WHILE - SALÁRIO

print("EXERCÍCIO COM WHILE - SALÁRIO")

salario = 1000
aumento = 0

print(f'Salário Inicial: {salario}')

while salario < 5000:
    aumento += 1
    print(f'Aumento {aumento}:', end = ' ')
    salario += 100
    print(salario)

print("-"*100)
print("-"*100)

#EXERCÍCIO COM WHILE - AUMENTO PROGRESSIVO DO SALÁRIO

print('EXERCÍCIO COM WHILE - AUMENTO PROGRESSIVO DO SALÁRIO')

ano_inicial = int(input("Digite o ano inicial: "))
ano_final = int(input("Digite o ano final: "))
salario = float(input("Digite o salário inicial: "))
aumento = float(input("Digite o valor do primeiro aumento: "))/100
salario_atual = 0
porcent = 0

print(f'Em {ano_inicial}, o salário inicial era de R$ {salario:.2f}')

while ano_inicial < ano_final:
    salario_atual = salario + (salario*aumento)
    porcent = aumento*100
    print(f'Ano {ano_inicial+1} - Aumento de {porcent:.3f}% = R$ {salario_atual:.2f}')
    salario = salario_atual
    aumento *= 1.1
    ano_inicial += 1

print("-"*100)
print("-"*100)
print("-"*100)
print("-"*100)

#EXERCÍCIO COM WHILE - CAIXA DE SUPERMERCADO

print("CAIXA DE SUPERMERCADO")

qtd = 0
total = 0
preco = 0
media = 0
pag = 0
desc = 0
novovalor = 0

while True:
    preco = float(input(f'Digite o valor do item {qtd+1} (ZERO PARA SAIR): '))
    if preco == 0:
        break
    while preco < 0:
            print("ERRO! Preço digitado menor do que ZERO.")
            preco = float(input(f'Digite novamente o preço do item {qtd+1}'
                                f'\nOu Digite ZERO para sair: '))
            if preco == 0:
                qtd -= 1
                break
    total += preco
    qtd += 1

pag = int(input("Escolha a forma de pagamento (Digite o Respectivo Número): \
                \n1 - Dinheiro (5% desconto)\
                \n2 - Cartão \
                \n"))
if pag == 2:
    print(f'Você comprou {qtd} produtos\nValor total: R$ {total:.2f}\nMédia: R$ {total/qtd:.2f}')
else:
    desc = total*0.05
    novovalor = total-desc
    print(f'Você comprou {qtd} produtos\nValor total: R$ {total:.2f}\nValor com Desconto: {novovalor:.2f}\nMédia: R$ {total/qtd:.2f}')
print("Finalizado")