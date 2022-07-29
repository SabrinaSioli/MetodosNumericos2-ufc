# Rodrigo - 496016
# Sabrina - 494013
# MN2 - Tarefa 14

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
    f2_v, _ = F2(v_velho, k, m, g, delta)

    v_aux = v_velho + (delta/2)*f2_v

    f1_v, f1_y = F1(v_aux, k, m, g)

    return f1_v, f1_y

def F4(v_velho, k, m, g, delta):
    f3_v, _ = F3(v_velho, k, m, g, delta)

    v_aux = v_velho + delta*f3_v

    f1_v, f1_y = F1(v_aux, k, m, g)

    return f1_v, f1_y
    
def aproximacaoDerivada(v_velho, y_velho, k, m, g, delta):

    solucoes_v = [0]*4
    solucoes_y = [0]*4

    solucoes_v[0] = v_velho
    solucoes_y[0] = y_velho
    
    for i in range(1,4):
        f1_v, f1_y = F1(v_velho, k, m, g)
        f2_v, f2_y = F2(v_velho, k, m, g, delta)
        f3_v, f3_y = F3(v_velho, k, m, g, delta)
        f4_v, f4_y = F4(v_velho, k, m, g, delta)

        v_novo = v_velho + (delta/6)*(f1_v + 2*f2_v + 2*f3_v + f4_v)
        y_novo = y_velho + (delta/6)*(f1_y + 2*f2_y + 2*f3_y + f4_y)
    
        solucoes_v[i] = v_velho = v_novo
        solucoes_y[i] = y_velho = y_novo

    return solucoes_v, solucoes_y

def predicaoCorrecao(solucoes_v, solucoes_y, k, m, g, delta):
    f1_v, _ = F1(solucoes_v[0], k, m, g)
    f2_v, f2_y = F1(solucoes_v[1], k, m, g)
    f3_v, f3_y = F1(solucoes_v[2], k, m, g)
    f4_v, f4_y = F1(solucoes_v[3], k, m, g)
    
    # Predição
    predicao_v = solucoes_v[3] + (delta/24)*(-9*f1_v + 33*f2_v - 59*f3_v + 55*f4_v)
    
    # Correção
    f1_v_pred, f1_y_pred = F1(predicao_v, k, m, g)

    correcao_v = solucoes_v[3] + (delta/24)*(f2_v - 5*f3_v + 19*f4_v + 9*f1_v_pred)
    correcao_y = solucoes_y[3] + (delta/24)*(f2_y - 5*f3_y + 19*f4_y + 9*f1_y_pred)

    return correcao_v, correcao_y


def preditorCorretor(v0, y0, k, m, g, delta):

    t = 0
    solucoes_v, solucoes_y = aproximacaoDerivada(v0, y0, k, m, g, delta)
    
    y_novo = y0
    y_max = y0
    
    while y_novo > 0:
        v_novo, y_novo = predicaoCorrecao(solucoes_v, solucoes_y, k, m, g, delta)
        
        v_final = solucoes_v[-1]
        t_final = t

        solucoes_v = [*solucoes_v[1:],*[v_novo]]
        solucoes_y = [*solucoes_y[1:],*[y_novo]]

        t += delta

        if y_novo > y_max:
            y_max = y_novo
            t_max = t


    return y_max, t_max, v_final, t_final

def main():
    print("\nPVI-2 com Preditor Corretor de 4ª ordem\n")

    v0 = 5.0
    y0 = 200.0
    k = 0.25
    m = 2
    g = 10.0

    for delta in [0.1, 0.01, 0.001, 0.0001]:
        y_max, t_max, v_final, t_final = preditorCorretor(v0, y0, k, m, g, delta)
        print("Para Δt="+str(delta))
        print("Altura máxima:", y_max)
        print("Tempo até altura máxima:", t_max)
        print("Tempo até o mar:", t_final)
        print("Velocidade impacto com o mar:", v_final)
        print()

main()