# Rodrigo da Silva Freitas - 496016
# Sabrina Silveira Oliveira - 494013
# Tarefa 03 - MN2

import math

def f(x):
    return math.cos(x)

def NewtonCotes(xi, xf, fechada, grau):

    if fechada:
        if grau == 1:
            h = xf - xi
            return (h/2) * ( f(xi) + f(xf) )
        elif grau == 2:
            h = (xf - xi) / 2
            return (h/3) * ( f(xi) + 4*f(xi + h) + f(xf) )
        elif grau == 3:
            h = (xf - xi) / 3
            return (3*h/8) * ( f(xi) + 3*f(xi + h) + 3*f(xi + 2*h) + f(xf) )
        elif grau == 4:
            h = (xf - xi) / 4
            return (2*h/45) * ( 7*f(xi) + 32*f(xi + h) + 12*f(xi + 2*h) + 32*f(xi + 3*h) + 7*f(xf) )
    else:
        if grau == 1:
            h = (xf - xi) / 3
            return (3*h/2) * ( f(xi + h) + f(xf + 2*h) )
        elif grau == 2:
            h = (xf - xi) / 4
            return (4*h/3) * ( 2*f(xi + h) - f(xi + 2*h) + 2*f(xi + 3*h) )
        elif grau == 3:
            h = (xf - xi) / 5
            return (5*h/24) * ( 11*f(xi + h) + f(xi + 2*h) + f(xi + 3*h) + 11*f(xf + 4*h) )
        elif grau == 4:
            h = (xf - xi) / 6
            return (3*h/10) * ( 11*f(xi + h) - 14*f(xi + 2*h) + 26*f(xi + 3*h) - 14*f(xi + 4*h) + 11*f(xi + 5*h) )




print("Funcao: cos(x)")
print("Tolerancia: 10^-6\n")
a = float(input("Inicio intervalo: "))
b = float(input("Fim intervalo: "))
grau = int(input("Grau: "))
tipo = input("Aberta(0) ou Fechada(1)?: ")
fechada = True if tipo=="1" else False

iNova = float('inf')
iVelha = 0

erro = 0.000001

n = 1

while True:
    iVelha = iNova

    dx = (b - a) / n

    iNova = 0

    for i in range(n):
        xi = a + (i*dx)
        xf = xi + dx
        iNova += NewtonCotes(xi, xf, fechada, grau)
    
    n *= 2

    if abs((iNova - iVelha) / iNova) <= erro:
        break

print("resultado: " + str(iNova))
print(str(n) + " iteracoes")