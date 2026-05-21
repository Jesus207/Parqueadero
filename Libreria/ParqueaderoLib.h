#ifndef PARQUEADEROLIB_H
#define PARQUEADEROLIB_H

extern "C" {

void guardarEvento(
const char* evento
);

const char* obtenerEvento();

}

#endif