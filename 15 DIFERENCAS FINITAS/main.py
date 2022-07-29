# Rodrigo - 496016
# Sabrina - 494013
# MN2 - Tarefa 15

import numpy as np
import sys

def solucaoExataPVC1(pontos, N):
    solucao = [0] * (N-1)
    for i in range(N-1):
        x = pontos[i]
        solucao[i] = (np.exp(-x) - np.exp(x)) / (np.exp(-1)-np.exp(1))

    return solucao

def diferencasFinitasPVC1(N):

    delta_x = 1.0/N
    tamanho = N-1

    # N = 8 => 7 incógnitas
    pontos = [delta_x*x for x in range(1, N)]
    exata = solucaoExataPVC1(pontos, N)

    lateral = 1/(delta_x**2)
    centro = -((2/(delta_x**2)) + 1)
       
    coeficientes = np.zeros((tamanho, tamanho))

    for i in range(tamanho):
        if i > 0:
            coeficientes[i][i-1] = lateral
        
        coeficientes[i][i] = centro
        
        if i < tamanho-1:
            coeficientes[i][i+1] = lateral

    termos_indep = [0] * tamanho
    termos_indep[tamanho-1] = -lateral

    aproximacao = np.linalg.solve(coeficientes, termos_indep)

    return aproximacao, exata


def diferencasFinitasPVC2(N, f_xy):

    delta_x = 1.0/N
    delta_y = 1.0/N
    tamanho = (N-1)**2

    lateral_x = 1/(delta_x**2)
    centro = -2 * (1/(delta_x**2) + 1/(delta_y**2))
    lateral_y = 1/(delta_y**2)

    coeficientes = np.zeros((tamanho, tamanho), dtype=float)

    k = 0
    y = 0
    for i in range(tamanho):
        if i > 0:
            k += 1
            if k % (N-1) != 0: 
                coeficientes[i][i-1] = lateral_y
            else:
                coeficientes[i][i-1] = 0

        if i > (N-2):
            coeficientes[i][i-(N-1)] = lateral_x

        coeficientes[i][i] = centro

        if i < tamanho-(N-1):
            coeficientes[i][i+(N-1)] = lateral_x

        if i < tamanho-1:
            y += 1
            if y % (N-1) !=0: 
                coeficientes[i][i+1] = lateral_y
            else:
                coeficientes[i][i+1] = 0

    termos_indep = np.empty((tamanho), dtype=float)
    termos_indep.fill(f_xy)

    aproximacao = np.linalg.solve(coeficientes, termos_indep)

    return aproximacao

def erro(aprox, exata):
    return '{0:.4f}'.format(((aprox-exata)/exata)*100) + '%'

def main():

    pvc = sys.argv
    N = 8

    if 'PVC1' in pvc or len(sys.argv)==1:

        aproximacaoPVC1, exataPVC1 = diferencasFinitasPVC1(N)
        
        print("Método das Diferenças Finitas - PVC1")
        print("      Aproximação         |   Exata             |  Erro    ")
        print("-----------------------------------------------------------------------------")
        for i in range(N-1):
            print(" y"+str(i+1), "|", aproximacaoPVC1[i], "|" , exataPVC1[i], "|", erro(aproximacaoPVC1[i], exataPVC1[i]))       

    if 'PVC2' in pvc:

        aproximacaoPVC2 = diferencasFinitasPVC2(N, 4)
        
        print("Método das Diferenças Finitas - PVC2")
        print("      Aproximação")
        print("-------------------------------")
        for i in range((N-1)**2):
            print(" y"+str(i+1), "|", aproximacaoPVC2[i]) 

    print()

main()    