import math

def gauss_Hermite():
    resposta = [gauss_Hermite_2(), gauss_Hermite_3(), gauss_Hermite_4()]
    return resposta

def f(x):
    e = math.pow(math.e,-math.pow(x, 2))
    formula= (math.sin(2*x) + 4*math.pow(x, 2) + 3*x)
    return math.pow(formula, 2)

# 2 Pontos
def gauss_Hermite_2():
    s = (1/math.sqrt(2))
    raizes_s = [-s, s]
    w = math.sqrt(math.pi)/2
    pesos_w = [w, w]
    return funcao_geral_integracao(2, pesos_w, raizes_s)

# 3 Pontos
def gauss_Hermite_3(): 
    s = math.sqrt(3/2)
    raizes_s = [-s, 0, s]
    w = math.sqrt(math.pi)/6
    w_2 = 1.1816359
    pesos_w = [w, w_2, w]
    return funcao_geral_integracao(3, pesos_w, raizes_s)

# 4 Pontos
def gauss_Hermite_4(): 
    s = math.sqrt(3+math.sqrt(6))/math.sqrt(2)
    s_2 = math.sqrt(3-math.sqrt(6))/math.sqrt(2)
    raizes_s = [-s, -s_2, s_2, s]
    w = 0.08131283545
    w_2 = 0.80491409
    pesos_w = [w, w_2, w_2, w]

    return funcao_geral_integracao(4, pesos_w, raizes_s)

def funcao_geral_integracao(qtd_grau, pesos_w, raizes_s):
    somatorio = 0
    for k in range(qtd_grau):
        somatorio += (pesos_w[k] * f(raizes_s[k]))
  
    return somatorio