
iniciar = 0
obstaculo = 0
esca_contor = 0
escalada = 0
descoberta = 0
pontos = 0
dados = 0

def passo_2(obst):
    while True:
        if obst == 0:
            print('Você continuará a exploração.')
            obst = int(input('Encontrou um obstáculo?\nDigite 1 para SIM ou 0 para Não. '))
        else:
            break


def passo_4(sucesso):
    sucesso = int(input('Conseguiram escalar a montanha? Digite 1 para SIM ou 0 para NÃO. '))
    return sucesso


def passo_7(coleta):
    continuar = 1
    while continuar == 1:
        dados = int(input('Quais dados científicos vocês coletaram:\n' \
                        '1) - Minerais (1 ponto)\n' \
                        '2) - Vida (2 pontos)\n'))
        if dados == 1:
            coleta += 1
        elif dados == 2:
            coleta += 2
        continuar = int(input('Deseja continuar?\n1) SIM\n2) NÃO\n'))
    return coleta


iniciar = int(input('Deseja iniciar a exploração?\nDigite 1 para SIM ou 0 para Não. '))
if iniciar == 1:
    print('Você iniciou a sua exploração.')
    while descoberta == 0:
        obstaculo = int(input('Encontrou um obstáculo?\nDigite 1 para SIM ou 0 para Não. '))
        passo_2(obstaculo)
        while escalada == 0:
            esca_contor = int(input("Digite 1 para ESCALAR ou 2 para CONTORNAR. "))
            if esca_contor == 1:
                escalada = passo_4(escalada)                
            elif esca_contor == 2: 
                break       
        descoberta = int(input('Encontraram minerais ou sinais de vida? Digite 1 para SIM ou 0 para NÃO. '))
        if descoberta == 1:
            break
    pontos = passo_7(pontos)
    print(f'Parabéns, vocês coletaram {pontos} pontos.')
           
    