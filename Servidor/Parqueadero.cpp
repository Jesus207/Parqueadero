#include "Parqueadero.h"

#include <iostream>
#include <fstream>
#include <ctime>

#include "../Libreria/ParqueaderoLib.h"

using namespace std;

Parqueadero::Parqueadero(){

    siguienteCelda=1;

}

void Parqueadero::procesarPlaca(
    string placa
){

    time_t ahora=time(0);

    string hora=
    ctime(&ahora);

    hora.pop_back();

    if(
        placas.count(
            placa
        )
    ){

        int celda=
        placas[placa];

        string evento=

        "SALIDA -> "
        +placa+
        " | Celda "
        +to_string(celda)+
        " liberada | "
        +hora;

        cout
        <<evento
        <<endl;

        guardarEvento(
            evento.c_str()
        );

        ofstream archivo(
            "/workspaces/Parqueadero/historial.txt",
            ios::app
        );

        archivo
        <<evento
        <<endl;

        archivo.close();

        placas.erase(
            placa
        );

        celdasLibres.push(
            celda
        );

    }

    else{

        int celda;

        if(
            !celdasLibres.empty()
        ){

            celda=
            celdasLibres.front();

            celdasLibres.pop();

        }

        else{

            celda=
            siguienteCelda;

            siguienteCelda++;

        }

        placas[
            placa
        ]=celda;

        string evento=

        "ENTRADA -> "
        +placa+
        " | Celda "
        +to_string(celda)+
        " ocupada | "
        +hora;

        cout
        <<evento
        <<endl;

        guardarEvento(
            evento.c_str()
        );

        ofstream archivo(
            "/workspaces/Parqueadero/historial.txt",
            ios::app
        );

        archivo
        <<evento
        <<endl;

        archivo.close();

    }

}