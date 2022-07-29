# Rodrigo - 496016
# Sabrina - 494013
# MN2 - Tarefa 12 Aula#22

import math
from utilidades import *

ERRO = 0.000001

MOSTRAR_ANOVA = True

def Jacobi_ij(A, i, j):
    theta = 0
    n = len(A)
    J = MatrizIdentidade(n)

    if abs(A[i][j]) <= ERRO:
        return J
    elif abs(A[j][j]) <= ERRO:
        if A[i][j] < 0:
            theta = math.pi / 2
        else:
            theta = - math.pi / 2
    else:
        theta = math.atan(-A[i][j] / A[j][j])

    J[i][i] = math.cos(theta)
    J[j][j] = math.cos(theta)
    J[i][j] = math.sin(theta)
    J[j][i] = -math.sin(theta)

    return J

def DecomposicaoQR(A):
    n = len(A)
    QT = MatrizIdentidade(n)
    Rvelha = A.copy()

    for j in range(n):
        for i in range(j+1,n):

            J = Jacobi_ij(Rvelha, i, j)

            Rnova = MultiplicarMatrizesNxN(J, Rvelha)

            Rvelha = Rnova.copy()

            QT = MultiplicarMatrizesNxN(J, QT)
    
    Q = Transposta(QT)
    return Q, Rnova

def QR(A):
    n = len(A)
    val = 100.0
    
    P = MatrizIdentidade(n)
    Avelha = A.copy()

    while val > ERRO:
        Q, R = DecomposicaoQR(Avelha)

        Anova = MultiplicarMatrizesNxN(R, Q)

        if MOSTRAR_ANOVA:
            print("Anova:")
            printarMatriz(Anova)
            print()

        Avelha = Anova.copy()

        P = MultiplicarMatrizesNxN(P, Q)

        val = SomaQuadradosAbaixoDiagonal(Anova)
    
    lamb = [0]*n
    for i in range(n):
        lamb[i] = Anova[i][i]

    return P, lamb


def main():
    """
    A = [[0 for x in range(3)] for y in range(3)] 
    A[0] = [5, 2, 1]
    A[1] = [2, 3, 1]
    A[2] = [1, 1, 2]
    """

    A = [[0 for x in range(5)] for y in range(5)] 
    A[0] = [40, 8, 4, 2, 1]
    A[1] = [8, 30, 12, 6, 2]
    A[2] = [4, 12, 20, 1, 2]
    A[3] = [2, 6, 1, 25, 4]
    A[4] = [1, 2, 2, 4, 5]
    

    print("QUESTÃO 1")
    P, lamb = QR(A)

    print("Pares:")
    imprimirPares(P, lamb)

    print("\n\n")

    print("QUESTÃO 2")
    Ai, H = Householder(A)

    P, lamb = QR(Ai)

    print("Pares:")
    imprimirPares(P, lamb)

    print("P = HP")
    P = MultiplicarMatrizesNxN(H, P)

    print("Pares:")
    imprimirPares(P, lamb)


main()
