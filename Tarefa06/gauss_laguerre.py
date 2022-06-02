import math

def gauss_Laguerre():
    resposta = [gauss_Laguerre_2(), gauss_Laguerre_3(), gauss_Laguerre_4()]
    return resposta

def f(x): 
  return math.pow( math.sin(2*x) + 4*math.pow(x, 2) + 3*x, 2)

# 2 Pontos
def gauss_Laguerre_2(): 
    s = 0.5857864376
    s_2 = 3.414213562

    raizes_s = [s, s_2]
    w = 0.8535533905
    w_2 = 0.1464466094
    pesos_w = [w, w_2]

    return funcao_geral_integracao(2, pesos_w, raizes_s)

# 3 Pontos
def gauss_Laguerre_3():
    raizes_s = [0.4157745568, 2.2942803603, 6.2899450829]
 
    pesos_w = [0.7110930099, 0.2785177336, 0.0103892565]

    return funcao_geral_integracao(3, pesos_w, raizes_s)

# 4 Pontos
def gauss_Laguerre_4():
    raizes_s = [0.32254, 1.74576, 4.53662, 9.39507]
 
    pesos_w = [0.60335, 0.35742, 0.03888, 0.00053]

    return funcao_geral_integracao(4, pesos_w, raizes_s)

def funcao_geral_integracao(grau, pesos_w, raizes_s):
    somatorio = 0
    for k in range(grau):
        somatorio += (pesos_w[k] * f(raizes_s[k]))
    return somatorio