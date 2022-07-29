# Rodrigo - 496016
# Sabrina - 494013
# MN2 - Tarefa 13

def F1(v_velho, k, m, g):

    v_novo = -g - ((k/m)*v_velho)
    y_novo = v_velho

    return v_novo, y_novo


def F2(v_velho, k, m, g, delta):
    f1_v, _ = F1(v_velho, k, m, g)

    v_aux = v_velho + (delta/2)*f1_v
    
    f1_v, f1_y = F1(v_aux, k, m, g) 

    return f1_v, f1_y


def F3(v_velho, k, m, g, delta):
    f1_v, _ = F1(v_velho, k, m, g)
    f2_v, _ = F2(v_velho, k, m, g, delta)

    v_aux = v_velho + delta*(-f1_v + 2*f2_v)

    f1_v, f1_y = F1(v_aux, k, m, g)

    return f1_v, f1_y


def aproximacaoDerivada(v_velho, y_velho, k, m, g, delta):
    f1_v, f1_y = F1(v_velho, k, m, g)
    f2_v, f2_y = F2(v_velho, k, m, g, delta)
    f3_v, f3_y = F3(v_velho, k, m, g, delta)

    v_novo = v_velho + delta*((f1_v + 4*f2_v + f3_v)/6)
    y_novo = y_velho + delta*((f1_y + 4*f2_y + f3_y)/6)
    
    return v_novo, y_novo

def rungeKutta3Ordem(v0, y0, k, m, g, delta):

    t = 0
    v_velho = v0
    y_velho = y0
    
    y_novo = y_velho
    y_max = y0

    while y_novo > 0:
        v_novo, y_novo = aproximacaoDerivada(v_velho, y_velho, k, m, g, delta)

        v_final = v_velho
        t_final = t

        v_velho = v_novo
        y_velho = y_novo

        t += delta

        if y_novo > y_max:
            y_max = y_novo
            t_max = t

    return y_max, t_max, v_final, t_final

def main():
    print("\nPVI-2 com Runge-Kutta de 3ª ordem\n")

    v0 = 5.0
    y0 = 200.0
    k = 0.25
    m = 2
    g = 10.0

    for delta in [0.1, 0.01, 0.001, 0.0001]:
        y_max, t_max, v_final, t_final = rungeKutta3Ordem(v0, y0, k, m, g, delta)
        print("Para Δt="+str(delta))
        print("Altura máxima:", y_max)
        print("Tempo até altura máxima:", t_max)
        print("Tempo até o mar:", t_final)
        print("Velocidade impacto com o mar:", v_final)
        print()

main()