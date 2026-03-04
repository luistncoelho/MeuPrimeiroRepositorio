#TESTE LISTAS

lista_nomes = []
lista_idades = []

for i in range(0, 2):
    nome = str(input('Digite o seu nome: '))
    lista_nomes.append(nome)
    idade = int(input('Qual a sua idade? '))
    lista_idades.append(idade)

print(f'Lista de nomes: {lista_nomes}')
print(f'Lista de idades: {lista_idades}')

print('-'*100)
print('-'*100)

for i in lista_nomes:
    print(f'Nome: {i}')