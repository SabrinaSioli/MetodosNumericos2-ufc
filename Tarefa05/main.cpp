// Rodrigo - 496016
// Sabrina - 494013
// MN2 - Tarefa 5

#include <iostream>
#include <iomanip>
#include <string>
#include <limits>
#include <cmath>


// Gauss Legendre
double f(double x)
{
    return pow((sin(2*x) + 4*pow(x, 2) + 3*x), 2) ;
}

double x_s (double ini, double fim, double s)
{
    return ( ( fim + ini ) / 2.0 ) + ( ( ( fim - ini ) / 2.0 ) * s );
}

double GaussLegendre (double ini, double fim, int qtdPontos)
{
    double resultado;
    double w1, w2, w3, w4;

    switch (qtdPontos)
    {
        case 2:
            w1 = w2 = 1.0;
            resultado = ( ( fim - ini ) / 2.0 ) * ( f( x_s( ini, fim, -(1.0 / sqrt( 3.0 ) ) ) ) * w1
                                                    + f( x_s( ini, fim, +(1.0 / sqrt( 3.0 ) ) ) ) * w2 );
            break;
        case 3:
            w1 = w3 = 5.0 / 9.0;
            w2 = 8.0 / 9.0;

            resultado = ( ( fim - ini ) / 2.0 ) * ( f( x_s( ini, fim, -(sqrt( 3.0 / 5.0 ) ) ) ) * w1
                                                    + f( x_s( ini, fim,  (0.0               ) ) ) * w2
                                                    + f( x_s( ini, fim, +(sqrt( 3.0 / 5.0 ) ) ) ) * w3 );
            break;
        case 4:
            w1 = w2 = 0.652145;
            w3 = w4 = 0.347855;

            resultado = ( ( fim - ini ) / 2.0 ) * ( f( x_s( ini, fim, -sqrt((3.0/7.0) - ((2.0*sqrt(6.0/5.0)) / 7.0)))) * w1
                                                    + f( x_s( ini, fim, sqrt((3.0/7.0) - ((2.0*sqrt(6.0/5.0)) / 7.0)))) * w2
                                                    + f( x_s( ini, fim,  -sqrt((3.0/7.0) + ((2.0*sqrt(6.0/5.0)) / 7.0)))) * w3
                                                    + f( x_s( ini, fim, sqrt((3.0/7.0) + ((2.0*sqrt(6.0/5.0)) / 7.0)))) * w4);
            
    }

    return resultado;
}


int main()
{
  double a;
  double b;
  double eps;
  int qtdPontos;

  std::cout << "Função: (sen(2x) + 4x^2 + 3x)^2\n";
              
  std::cout << "Integração de Gauss Legendre" << std::endl;

  std::cout << "Início do intervalo: ";
  std::cin >> a;

  std::cout << "Fim do intervalo: ";
  std::cin >> b;

  std::cout << "Número de pontos de Legendre: ";
  std::cin >> qtdPontos;

  std::cout << "Tolerância: ";
  std::cin >> eps;

  double integralNova = std::numeric_limits<double>::infinity();
  double integralVelha;
  int N = 1;

  do
  {
    integralVelha = integralNova;

    double deltaX = ( b - a ) / N;

    integralNova = 0.0;

    for ( int i = 0; i < N; i++ )
    {
      double xIn = a + ( i * deltaX );
      double xFin = xIn + deltaX;
      integralNova += GaussLegendre( xIn, xFin, qtdPontos );
    }

    N *= 2;
  } while (fabs( ( integralNova - integralVelha ) / integralNova ) > eps );
  
  std::cout << std::setprecision(7)<< integralNova << "\nN: " << N << "\n";

  return 0;
}

//1.5707963268