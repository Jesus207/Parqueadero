#include "Parqueadero.h"

#include <iostream>

#include <ctime>

using namespace std;

Parqueadero::
Parqueadero(){

siguienteCelda=1;

}

void Parqueadero::
procesarPlaca(
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

cout<<endl;

cout
<<"SALIDA -> "
<<placa
<<" | Celda "
<<celda
<<" liberada | "
<<hora
<<endl;

placas.erase(
placa
);

}
else{

placas[placa]=
siguienteCelda;

cout<<endl;

cout
<<"ENTRADA -> "
<<placa
<<" | Celda "
<<siguienteCelda
<<" ocupada | "
<<hora
<<endl;

siguienteCelda++;

}

}