#include "Parqueadero.h"
#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

vector<string> celdas(12, "");

Parqueadero::Parqueadero(){}

string Parqueadero::procesarPlaca(string placa){

    // Si ya existe -> salida
    for(int i=0; i<12; i++){

        if(celdas[i] == placa){

            celdas[i] = "";

            return "SALIDA -> " +
                   placa +
                   " | Celda " +
                   to_string(i+1) +
                   " liberada";
        }
    }

    // Entrada
    vector<int> libres;

    for(int i=0; i<12; i++){

        if(celdas[i] == "")
            libres.push_back(i);
    }

    if(libres.empty())
        return "PARQUEADERO LLENO";

    int pos =
        libres[rand()%libres.size()];

    celdas[pos] = placa;

    return "ENTRADA -> " +
           placa +
           " | Celda " +
           to_string(pos+1) +
           " ocupada";
}