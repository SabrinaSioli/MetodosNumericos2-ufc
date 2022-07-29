from utilidades import *

def DecomposicaoLU (A):
    n = len(A)

    L = MatrizIdentidade(n)
    U = MatrizIdentidade(n)

    for j in range(n):
        for i in range(j+1):
            valor = 0

            for k in range(i):
                valor = valor + (L[i][k] * U[k][j])

            U[i][j] = A[i][j] - valor

        for i in range(j+1, n):
            valor = 0

            for k in range(j):
                valor = valor + (L[i][k] * U[k][j])

            if U[j][j] == 0:
                return None, None

            L[i][j] = (A[i][j] - valor) / U[j][j]
    
    return L, U

def ResolucaoLU(L, U, b):
    n = len(b)
    x = [0]*n
    y = [0]*n
    
    for i in range(n):
        y[i] = b[i]

        for j in range(i):
            y[i] = y[i] - (L[i][j] * y[j])

    for i in range(n-1, -1, -1):
        x[i] = y[i]

        for j in range(n-1, i, -1):
            x[i] = x[i] - (U[i][j] * x[j])
            
        x[i] = x[i] / U[i][i]
  
    return x