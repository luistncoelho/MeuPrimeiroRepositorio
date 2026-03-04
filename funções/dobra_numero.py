#FUNÇÃO DOBRA NÚMERO

print('FUNÇÃO DOBRA NÚMERO')

def dobra(n):
    lista_dobra = []
    for r in n:
        r *= 2
        lista_dobra.append(r)
    return lista_dobra


lista = []
qtd = int(input('Digite quantos números deseja dobrar: '))
for i in range(0, qtd):
    num = int(input(f"Digite o {i + 1}° número: "))
    lista.append(num)
    num = 0

print(dobra(lista))