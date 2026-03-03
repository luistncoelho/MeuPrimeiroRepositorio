# Área e Perímetro do Retângulo

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

# Cálculando a área e o perímetro

area = base*altura
perimetro = 2*(base+altura)

# Exibição dos resultados

print(f"A área do retângulo é: {area:.2f}\n"
      f"O Perímetro do retângulo é: {perimetro:.2f}")