#ifndef PARQUEADERO_H
#define PARQUEADERO_H

#include <string>
#include <map>
#include <queue>

using namespace std;

class Parqueadero {
public:
    Parqueadero();
    string procesarPlaca(string placa);

private:
    map<string, int> placas;
    queue<int> celdasLibres;

    int siguienteCelda;

    // ESTADÍSTICAS DEL SISTEMA
    int capacidadMax;
    int totalEntradas;
    int totalSalidas;
    int ocupacion;
};

#endif