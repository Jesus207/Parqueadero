#ifndef PARQUEADERO_H
#define PARQUEADERO_H

#include <string>
#include <map>
#include <queue>

class Parqueadero{

private:

std::map<
std::string,
int
> placas;

std::queue<int>
celdasLibres;

int siguienteCelda;

public:

Parqueadero();

void procesarPlaca(
std::string placa
);

};

#endif