#Cinthia 471317
#Daniele 473257
import gauss_chebyshev
import gauss_hermite
import gauss_laguerre

def menuResposta(resposta):
  print("\n--------------------------------")
  print("Resultados: " )
  print("Grau 2: ", resposta[0])
  print("Grau 3: ", resposta[1])
  print("Grau 4: ", resposta[2])
  print("--------------------------------")

stopProgram = False
print( "-"*60)
print( "        fórmula base: f(x)=(sen(2x) + 4x^2 + 3x)^2")
print( "-"*60)
while (not stopProgram):
    print()
    print("1 - Gauss-Hermite")
    print("2 - Gauss-Laguerre")
    print("3 - Gauss-Chebyshev")
    metodo = input('Escolha um método: ')
    metodo = int(metodo)

    if(metodo==0):
          break

    elif(metodo==1):
        resposta = gauss_hermite.gauss_Hermite()
        menuResposta(resposta)
       
    elif(metodo==2):
        resposta = gauss_laguerre.gauss_Laguerre()
        menuResposta(resposta)

    elif(metodo==3):
        resposta = gauss_chebyshev.gauss_chebyshev()
        menuResposta(resposta)
    else:
      continue
    
        
    print("1 - Calcular novamente")
    print("0 - Sair do programa")
    calcularNovamente = input('Escolha uma opção: ')
    if( int(calcularNovamente) == 1):
        print( "-"*60)
        print( "        fórmula base: f(x)=(sen(2x) + 4x^2 + 3x)^2")
        print( "-"*60)
    else:
        stopProgram = True