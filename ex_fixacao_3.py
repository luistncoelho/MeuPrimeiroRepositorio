#EXERCÍCIO 1 - CASE

print("EXERCÍCIO 5 - CASE")

saldo_inicial = 1000
checkpoint = saldo_inicial
nome = str(input('Digite o seu nome: ')).replace(" ", "")
caractere = not nome.isalpha()

if checkpoint is not saldo_inicial:
    print("Programa Finalizado")
else:
    while caractere == True:
        nome = str(input("Digite o seu nome novamente. Não utilize caracteres especiais: ")).replace(" ", "")
        caractere = not nome.isalpha()
    for i in range(0, 4):
        operacao = float(input('Efetue a operação: '))
        if operacao > 500:
            print("Transação de alto valor")
        elif operacao < 0:
            if (operacao*-1) > saldo_inicial:
                print("Saldo insuficiente")
                operacao = 0
        saldo_inicial += operacao
print(f'O saldo final é: {saldo_inicial}')
if checkpoint is not saldo_inicial:
    print('Programa Finalizado')