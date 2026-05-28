#ifndef PARQUEADEROLIB_H
#define PARQUEADEROLIB_H

#include <string>
#include <vector>

using namespace std;

class Parqueadero {
private:
    vector<string> eventos;   // 🔴 obligatorio

public:
    string procesarPlaca(string placa);
    void guardarEvento(string evento);
    string obtenerUltimoEvento();
    string obtenerEstado();
};

#endif