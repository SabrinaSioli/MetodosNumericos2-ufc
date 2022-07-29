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


def SomaQuadradosAbaixoDiagonal(A):
    n = len(A)
    soma = 0
    for i in range(n):
        for j in range(i):
            soma += A[i][j]**2
    return soma

def imprimirPares(P, lamb):
    n = len(lamb)
    for i in range(n):
        out = str(lamb[i])
        out += ": ( "
        for j in range(n):
            out += str(P[j][i]) + " "
        out += ")"
        print(out)
    print()

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