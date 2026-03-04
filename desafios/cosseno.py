def angulo_radiano(angulo):
    radiano = angulo * 3.1415 / 180
    return radiano

def fatorial(numero):
    valor = numero
    for _ in range(1, numero):
        valor *= numero - 1
        numero -= 1
    return valor

def exponencial(numero, x):
    resultado1 = numero ** x

    return resultado1 

def cosseno(grau):
    valor = angulo_radiano(grau)
    z = 1 - (exponencial(valor, 2) / fatorial2) + (exponencial(valor, 4) / fatorial4) - (exponencial(valor, 6) / fatorial6) + (exponencial(valor, 8) / fatorial8) - (exponencial(valor, 10) / fatorial10) + (exponencial(valor, 12) / fatorial12) - (exponencial(valor, 14) / fatorial14) + (exponencial(valor, 16) / fatorial16)
    return z
    

fatorial2 = fatorial(2)
fatorial4 = fatorial(4)
fatorial6 = fatorial(6)
fatorial8 = fatorial(8)
fatorial10 = fatorial(10)
fatorial11 = fatorial(11)
fatorial12 = fatorial(12)
fatorial13 = fatorial(13)
fatorial14 = fatorial(14)
fatorial15 = fatorial(15)
fatorial16 = fatorial(16)

cos = float(input("Informe um valor:"))
z = cosseno(cos)

print(f"{z}")