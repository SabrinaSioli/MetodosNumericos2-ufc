import math

def gauss_chebyshev(): 
  resposta = [gauss_Chebyshev_2(), gauss_Chebyshev_3(), gauss_Chebyshev_4()]
  return resposta

def f(x): 
    formula = math.sin(2*x) + 4*math.pow(x, 2) + 3*x
    return math.pow(formula, 2)

# 2 Pontos
def gauss_Chebyshev_2(): 
    s = math.sqrt(2)
    raizes_s = [-1/s, s]
    w = math.pi/2
    pesos_w = [w, w]

    return funcao_geral_integracao(2, pesos_w, raizes_s)

# 3 Pontos
def gauss_Chebyshev_3():
    s = math.sqrt(3)
    raizes_s = [-s/2, 0, s/2]
    w = math.pi/3
    pesos_w = [w, w, w]

    return funcao_geral_integracao(3, pesos_w, raizes_s)

# 4 Pontos
def gauss_Chebyshev_4():
    s = math.sqrt(0.14644)
    s_2 = math.sqrt(0.85355)

    raizes_s = [s, -s, s_2, -s_2]
    w = math.pi/4
    pesos_w = [w, w, w, w]

    return funcao_geral_integracao(4, pesos_w, raizes_s)

def funcao_geral_integracao(qtd_grau, pesos_w, raizes_s):
    somatorio = 0
    for k in range(qtd_grau):
        somatorio += (pesos_w[k] * f(raizes_s[k]))

    return somatorio