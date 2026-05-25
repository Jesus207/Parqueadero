#include "GeneradorPlacas.h"
#include <cstdlib>

string GeneradorPlacas::generar() {

    string letras = "ABCDEF";
    string numeros = "0123456789";

    string placa = "";

    placa += letras[rand()%6];
    placa += letras[rand()%6];
    placa += letras[rand()%6];

    placa += numeros[rand()%10];
    placa += numeros[rand()%10];
    placa += numeros[rand()%10];

    return placa;
}