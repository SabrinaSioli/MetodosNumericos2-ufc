import math

def produtoEscalar(v1, v2):
    res = 0.0
    for i in range(len(v1)):
        res += v1[i]*v2[i]
    return res

def normaVetor(v):
    return math.sqrt(produtoEscalar(v, v))

def normalizarVetor(v):
    norm = normaVetor(v)
    vn = v.copy()

    for i in range(len(v)):
        vn[i] = v[i] / norm

    return vn

def multiplicarMatrizVetor(A, v):
    t = len(A)

    vet = [0] * t
    for i in range(t):
        for j in range(t):
            vet[i] += A[i][j] * v[j]
    
    return vet

def MultiplicarMatrizesNxN(A, B):
    n = len(A)
    C = [[0 for x in range(n)] for y in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
    
def MatrizIdentidade(n, val=1):
    A = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        A[i][i] = val
    return A

def subtrairMatrizes(A, B):
    n = len(A)
    C = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def printarMatriz(A):
    for l in A:
        lout = "[ "
        for c in l:
            lout += str(c) + " "
        lout += "]"
        print(lout)
    print()