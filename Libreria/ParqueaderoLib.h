#ifndef PARQUEADEROLIB_H
#define PARQUEADEROLIB_H

#include <string>
#include <vector>
#include <map>

using namespace std;

struct Celda {
    string nombre;   // "A1", "A2", etc.
    string placa;    // "LIBRE" o la placa
};

struct Evento {
    string hora;
    string placa;
    string celda;
    string tipo;     // "ENTRADA" o "SALIDA"
};

class Parqueadero {
private:
    vector<Celda> celdas;
    vector<Evento> eventos;

public:
    Parqueadero();                          // inicializa las 12 celdas
    string procesarPlaca(string placa);     // asigna o libera, retorna evento como string
    string obtenerEstado();                 // retorna todas las celdas serializadas
    string obtenerUltimoEvento();           // retorna el último evento como string
    int obtenerTotal();                     // celdas totales
    int obtenerLibres();                    // celdas libres
};

#endif