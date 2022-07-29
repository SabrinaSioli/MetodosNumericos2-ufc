# Rodrigo - 496016
# Sabrina - 494013
# MN2 - Tarefa 11

from utilidades import *
from LU import *

def metodoPotenciaRegular(A, v, erro):
    l0 = 0.0
    l1 = 0.0

    while True:
        l0 = l1

        v_norm = normalizarVetor(v)

        v = multiplicarMatrizVetor(A, v_norm)

        l1 = produtoEscalar(v_norm, v)

        e = abs( (l1 - l0) / l1 )

        if e <= erro:
            break
    
    v_norm = normalizarVetor(v)

    return l1, v_norm

def metodoPotenciaInverso(A, v, erro):
    
    n = len(v)

    L, U = DecomposicaoLU(A)
    
    AValNovo = 0

    v1 = v.copy()

    while True:
        AValVelho = AValNovo
        v0 = v1.copy()

        x = normalizarVetor(v0)

        v1 = ResolucaoLU(L, U, x)

        AValNovo = produtoEscalar(x, v1)

        e = abs( (AValNovo - AValVelho) / AValNovo )

        if e <= erro:
            break
    
    AValNovo = 1.0 / AValNovo

    return AValNovo, x.copy()

def metodoPotenciaDeslocamento(A, v, erro, valor):
    n = len(A)

    A1 = subtrairMatrizes(A, MatrizIdentidade(n, valor))

    aVal, aVet = metodoPotenciaInverso(A1, v, erro)

    aVal = aVal + valor

    return aVal, aVet.copy()

def main():

    erro = 0.000001

    mA = [[0 for x in range(3)] for y in range(3)] 
    mA[0] = [5, 2, 1]
    mA[1] = [2, 3, 1]
    mA[2] = [1, 1, 2]
    vA = [1, 1, 1]
    val_deslocA = 3

    autovalorReg, autovetorReg = metodoPotenciaRegular(mA, vA, erro)
    autovalorInv, autovetorInv = metodoPotenciaInverso(mA, vA, erro)
    autovalorDes, autovetorDes = metodoPotenciaDeslocamento(mA, vA, erro, val_deslocA)

    print("Para a matriz A1:")
    printarMatriz(mA)
    print("Regular")
    print("Autovalor dominante: ", autovalorReg)
    print("Autovetor: ", autovetorReg)
    print("\nInversa")
    print("Autovalor dominante: ", autovalorInv)
    print("Autovetor: ", autovetorInv)
    print("\nDeslocamento v =", val_deslocA)
    print("Autovalor dominante: ", autovalorDes)
    print("Autovetor: ", autovetorDes)
    print("\n")


    mB = [[0 for x in range(3)] for y in range(3)] 
    mB[0] = [-14, 1, -2]
    mB[1] = [1, -1, 1]
    mB[2] = [-2, 1, -11]
    vB = [1, 1, 1]
    val_deslocB = -7

    autovalorReg, autovetorReg = metodoPotenciaRegular(mB, vB, erro)
    autovalorInv, autovetorInv = metodoPotenciaInverso(mB, vB, erro)
    autovalorDes, autovetorDes = metodoPotenciaDeslocamento(mB, vB, erro, val_deslocB)

    print("Para a matriz A2:")
    printarMatriz(mB)
    print("Regular")
    print("Autovalor dominante: ", autovalorReg)
    print("Autovetor: ", autovetorReg)
    print("\nInversa")
    print("Autovalor dominante: ", autovalorInv)
    print("Autovetor: ", autovetorInv)
    print("\nDeslocamento v =", val_deslocB)
    print("Autovalor dominante: ", autovalorDes)
    print("Autovetor: ", autovetorDes)
    print("\n")


    mC = [[0 for x in range(5)] for y in range(5)] 
    mC[0] = [40, 8, 4, 2, 1]
    mC[1] = [8, 30, 12, 6, 2]
    mC[2] = [4, 12, 20, 1, 2]
    mC[3] = [2, 6, 1, 25, 4]
    mC[4] = [1, 2, 2, 4, 5]
    vC = [1, 1, 1, 1, 1]
    val_deslocC_1 = 30
    val_deslocC_2 = 20
    val_deslocC_3 = 10

    autovalorReg, autovetorReg = metodoPotenciaRegular(mC, vC, erro)
    autovalorInv, autovetorInv = metodoPotenciaInverso(mC, vC, erro)
    autovalorDes1, autovetorDes1 = metodoPotenciaDeslocamento(mC, vC, erro, val_deslocC_1)
    autovalorDes2, autovetorDes2 = metodoPotenciaDeslocamento(mC, vC, erro, val_deslocC_2)
    autovalorDes3, autovetorDes3 = metodoPotenciaDeslocamento(mC, vC, erro, val_deslocC_3)

    print("Para a matriz A3:")
    printarMatriz(mC)
    print("Regular")
    print("Autovalor dominante: ", autovalorReg)
    print("Autovetor: ", autovetorReg)
    print("\nInversa")
    print("Autovalor dominante: ", autovalorInv)
    print("Autovetor: ", autovetorInv)
    print("\nDeslocamento v =", val_deslocC_1)
    print("Autovalor dominante: ", autovalorDes1)
    print("Autovetor: ", autovetorDes1)
    print("\nDeslocamento v =", val_deslocC_2)
    print("Autovalor dominante: ", autovalorDes2)
    print("Autovetor: ", autovetorDes2)
    print("\nDeslocamento v =", val_deslocC_3)
    print("Autovalor dominante: ", autovalorDes3)
    print("Autovetor: ", autovetorDes3)
    print("\n")



main()