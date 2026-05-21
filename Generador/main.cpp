#include <iostream>
#include <thread>
#include <chrono>

#include "GeneradorPlacas.h"

using namespace std;

int main() {

    srand(time(NULL));

    GeneradorPlacas g;

    while(true) {

        string placa = g.generar();

        cout<<"Placa generada: "<<placa<<endl;

        int espera;

        if(rand()%2==0)
            espera=2;
        else
            espera=5;

        this_thread::sleep_for(
            chrono::seconds(espera)
        );
    }

    return 0;
}