import estrategiaExponencial
import math

def f1(x):
    return 1/(math.pow(x, 2) ** (1/3))


def funcao1Derivada(f, a_origin, b_origin):
    x_s = lambda s: ((a_origin+b_origin)/2)+(((b_origin-a_origin)/2)*math.tanh(s)) 
    dx_s = lambda s: (((b_origin-a_origin) / 2) * (1/(math.pow(math.cosh(s), 2))))
    return lambda s: f(x_s(s))*dx_s(s)
    
def f2(x):
    return 1/math.sqrt(4-math.pow(x,2))


def funcao2Derivdada(f, a_origin, b_origin):
    x_s = lambda s: (((a_origin+b_origin)/2)+((b_origin-a_origin)/2)*math.tanh(math.pi/2*math.sinh(s))) 
    dx_s = lambda s: ((b_origin-a_origin)/2) * ((math.pi * math.cosh(s)) / (2*(math.cosh(math.pi/2 * math.sinh(s))**2)))
    return lambda s: f(x_s(s))*dx_s(s)


problema_1 = estrategiaExponencial.calcula(-1, 0, 0.000001, f1,funcao1Derivada )
problema_2 = estrategiaExponencial.calcula(-2, 0, 0.000001, f2, funcao2Derivdada )
print("**********Tarefa 07**********")
print("Problema 1", problema_1[1]*2)
print("Problema 2", problema_2[1])