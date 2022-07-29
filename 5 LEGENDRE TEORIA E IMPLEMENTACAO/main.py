# Rodrigo - 496016
# Sabrina - 494013
# MN2 - Tarefa 5

import math

def f(x):
    return (math.sin(2*x) + 4*(x**2) + 3*x)**2

def x_s (ini, fim, s):
    return ( ( fim + ini ) / 2.0 ) + ( ( ( fim - ini ) / 2.0 ) * s )

def GaussLegendre (ini, fim, qtdPontos):

    if qtdPontos == 2:
        w1 = w2 = 1.0
        resultado = ( ( fim - ini ) / 2.0 ) * ( f( x_s( ini, fim, -(1.0 / math.sqrt( 3.0 ) ) ) ) * w1
                                                + f( x_s( ini, fim, +(1.0 / math.sqrt( 3.0 ) ) ) ) * w2 )

    elif qtdPontos == 3:
        w1 = w3 = 5.0 / 9.0
        w2 = 8.0 / 9.0

        resultado = ( ( fim - ini ) / 2.0 ) * ( f( x_s( ini, fim, -(math.sqrt( 3.0 / 5.0 ) ) ) ) * w1
                                                + f( x_s( ini, fim,  (0.0               ) ) ) * w2
                                                + f( x_s( ini, fim, +(math.sqrt( 3.0 / 5.0 ) ) ) ) * w3 )

    elif qtdPontos == 4:
        w1 = w2 = 0.652145
        w3 = w4 = 0.347855

        resultado = ( ( fim - ini ) / 2.0 ) * ( f( x_s( ini, fim, -math.sqrt((3.0/7.0) - ((2.0*math.sqrt(6.0/5.0)) / 7.0)))) * w1
                                                + f( x_s( ini, fim, math.sqrt((3.0/7.0) - ((2.0*math.sqrt(6.0/5.0)) / 7.0)))) * w2
                                                + f( x_s( ini, fim,  -math.sqrt((3.0/7.0) + ((2.0*math.sqrt(6.0/5.0)) / 7.0)))) * w3
                                                + f( x_s( ini, fim, math.sqrt((3.0/7.0) + ((2.0*math.sqrt(6.0/5.0)) / 7.0)))) * w4)
            
    return resultado



def main():

  print("Função: (sen(2x) + 4x^2 + 3x)^2\n")
              
  print("Integração de Gauss Legendre")

  # Intervalo
  a = 0.0
  b = 1.0
  qtdPontos = 4   # Número de pontos de Legendre
  eps = 0.000001  # Tolerância

  integralNova = float('inf')
  N = 1

  while True:
    integralVelha = integralNova

    deltaX = ( b - a ) / N

    integralNova = 0.0

    for i in range(N):
      xIn = a + ( i * deltaX )
      xFin = xIn + deltaX
      integralNova += GaussLegendre( xIn, xFin, qtdPontos )
    

    N *= 2
    if abs( ( integralNova - integralVelha ) / integralNova ) <= eps :
        break

    print(integralNova)
    print("N: ", N)
    print()

main()