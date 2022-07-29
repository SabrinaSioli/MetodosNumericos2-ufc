# Rodrigo - 496016
# Sabrina - 494013
# MN2 - Tarefa 12 Aula#20

import math
from utilidades import *
from metodosPotencia import *

ERRO = 0.000001


def MatrizHouseholder(A, i):
    n = len(A)

    w = [0]*n
    wb = [0]*n

    AT = Transposta(A)

    w[i+1:n] = AT[i][i+1:n]
    
    Lw = normaVetor(w)

    wb[i+1] = Lw

    N = subtrairVetores(w, wb)

    Nc = normalizarVetor(N)

    H = subtrairMatrizes(MatrizIdentidade(n), multiplicarMatrizEscalar(MultiplicarVetoresMatriz(Nc,Nc), 2))
    return H

def Householder(A):
    n = len(A)
    H = MatrizIdentidade(n)

    Avelha = A.copy()

    for i in range(n-2):
        Hi = MatrizHouseholder(Avelha, i)
        
        Anova = MultiplicarMatrizesNxN(Transposta(Hi), MultiplicarMatrizesNxN(Avelha, Hi))
        
        Avelha = Anova.copy()

        H = MultiplicarMatrizesNxN(H, Hi)
    
    return Anova, H

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

    Ai, H = Householder(A)

    print("\nMatriz tridiagonal A_barra")
    printarMatriz(Ai)
    
    print("Matriz acumulada H")
    printarMatriz(H)

    v = [1,1,1,1,1]
    autovalor1, autovetor1 = metodoPotenciaRegular(Ai, v, ERRO)
    autovalor2, autovetor2 = metodoPotenciaDeslocamento(Ai, v, ERRO, 30)
    autovalor3, autovetor3 = metodoPotenciaDeslocamento(Ai, v, ERRO, 20)
    autovalor4, autovetor4 = metodoPotenciaDeslocamento(Ai, v, ERRO, 10)
    autovalor5, autovetor5 = metodoPotenciaInverso(Ai, v, ERRO)

    print("Autovalores e autovetores de A_barra")
    print("Autovalor 1: ", autovalor1)
    print("Autovetor: ", autovetor1)
    print("Autovalor 2: ", autovalor2)
    print("Autovetor: ", autovetor2)
    print("Autovalor 3: ", autovalor3)
    print("Autovetor: ", autovetor3)
    print("Autovalor 4: ", autovalor4)
    print("Autovetor: ", autovetor4)
    print("Autovalor 5: ", autovalor5)
    print("Autovetor: ", autovetor5)
    print("\n")

    autovetor1_A = MultiplicarMatrizVetor(H, autovetor1)
    autovetor2_A = MultiplicarMatrizVetor(H, autovetor2)
    autovetor3_A = MultiplicarMatrizVetor(H, autovetor3)
    autovetor4_A = MultiplicarMatrizVetor(H, autovetor4)
    autovetor5_A = MultiplicarMatrizVetor(H, autovetor5)

    print("Autovalores e autovetores de A")
    print("Autovalor 1: ", autovalor1)
    print("Autovetor: ", autovetor1_A)
    print("Autovalor 2: ", autovalor2)
    print("Autovetor: ", autovetor2_A)
    print("Autovalor 3: ", autovalor3)
    print("Autovetor: ", autovetor3_A)
    print("Autovalor 4: ", autovalor4)
    print("Autovetor: ", autovetor4_A)
    print("Autovalor 5: ", autovalor5)
    print("Autovetor: ", autovetor5_A)
    print("\n")



main()
