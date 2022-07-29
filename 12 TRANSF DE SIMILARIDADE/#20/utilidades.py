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

def MultiplicarMatrizVetor(A, v):
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

def Transposta(A):
    return list(zip(*A))

def subtrairVetores(v1, v2):
    n = len(v1)
    v3 = [0]*n
    for i in range(n):
        v3[i] = v1[i] - v2[i]
    return v3

def subtrairMatrizes(A, B):
    n = len(A)
    C = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def multiplicarMatrizEscalar(A, esc):
    n = len(A)
    C = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] * esc
    return C

def MultiplicarVetoresMatriz(v1, v2):
    n = len(v1)
    A = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            A[i][j] = v1[i] * v2[j]
    return A


def printarMatriz(A):
    for l in A:
        lout = "[ "
        for c in l:
            lout += "{:.4f}".format(c) + " "
        lout += "]"
        print(lout)
    print()

def printarVetor(v):
    lout = "( "
    for c in v:
        lout += str(c) + " "
    lout += ")"
    print(lout)
    print()


