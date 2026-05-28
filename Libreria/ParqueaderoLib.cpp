#include "ParqueaderoLib.h"

string Parqueadero::procesarPlaca(string placa) {
    guardarEvento("Procesando placa: " + placa);
    return "OK " + placa;
}

void Parqueadero::guardarEvento(string evento) {
    eventos.push_back(evento);
}

string Parqueadero::obtenerUltimoEvento() {
    if (eventos.empty()) return "Sin eventos";
    return eventos.back();
}

string Parqueadero::obtenerEstado() {
    return "Eventos registrados: " + to_string(eventos.size());
}