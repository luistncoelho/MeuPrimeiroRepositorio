# DESAFIO FUNÇÕES

print('DESAFIO FUNÇÕES')


def limpar_vendas(limpa):
    for c in limpa:
        if c > 0 and c < 10000:
            lista_limpa.append(c)
    return lista_limpa


def analisar_dados(dados):
    media = 0
    total = 0
    for c in dados:
        total += c
    media = total / len(dados)
    return total, media


def definir_status(status):
    if status[1] > 5000:
        return 'Alta Performance'
    elif status[1] >= 2000 and status[1] < 5000:
        return 'Performance Estável'
    elif status[1] < 2000:
        return 'Performance Crítica'


lista_limpa = list()
filial = str(input('Digite o nome da filial: '))
vendas = list()
atualizar = 0
c = 0

while True:
    atualizar = float(input('Digite o valor da venda (digite 0 para sair): '))
    if atualizar == 0:
        break
    vendas.append(atualizar)


vendas_validas = limpar_vendas(vendas)
total_media = analisar_dados(lista_limpa)
performance = definir_status(total_media)
print('-'*20)
print(filial)
print('-'*20)
print(f'Total = {total_media[0]:.2f}')
print(performance)
print(f'Media = {total_media[1]:.2f}')
print('Vendas:')
for i in vendas_validas:
    print(f'{c+1} - {i:.2f}')
    c += 1