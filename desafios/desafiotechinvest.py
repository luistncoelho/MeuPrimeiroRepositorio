#DESAFIO TECHINVEST - PRIME

print('DESAFIO TECHINVEST - PRIME')

nome = str(input('Digite o seu nome: '))
renda_mensal = float(input('Qual a sua renda mensal: '))
gasto_mensal = float(input("Qual o seu gasto mensal: "))
coragem = int(input('Qual o seu nível de coragem para investir (de 1 a 10): '))
reserva = gasto_mensal * 6
seguranca = 0

if gasto_mensal > renda_mensal:
    print('Emergência Financeira!')
elif gasto_mensal < renda_mensal:
    seguranca = reserva - (renda_mensal - gasto_mensal)
    print(f'Falta R${seguranca} para você completar a sua reserva de segurança.')
    if coragem < 4:
        print('Você deve investir em Tesouro Direto.')
    elif coragem >= 4 and coragem <=7:
        print('Você deve investir em Fundos Imobiliários.')
    else:
        print('Você deve investir em Ações de Tecnologia.')
    print('Quantos anos você pretende investir?')