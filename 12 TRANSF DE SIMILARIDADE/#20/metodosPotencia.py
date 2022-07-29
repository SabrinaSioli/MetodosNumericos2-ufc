# Rodrigo - 496016
# Sabrina - 494013

from utilidades import *
from LU import *

def metodoPotenciaRegular(A, v_cop, erro):
    l0 = 0.0
    l1 = 0.0

    v = v_cop.copy()

    while True:
        l0 = l1

        v_norm = normalizarVetor(v)

        v = MultiplicarMatrizVetor(A, v_norm)

        l1 = produtoEscalar(v_norm, v)

        e = abs( (l1 - l0) / l1 )

        if e <= erro:
            break
    
    v_norm = normalizarVetor(v)

    return l1, v_norm

def metodoPotenciaInverso(A, v, erro):
    # Alternativa 2
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
