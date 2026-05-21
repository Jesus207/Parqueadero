#ifndef PARQUEADERO_H
#define PARQUEADERO_H

#include <string>
#include <map>

class Parqueadero {

private:

std::map<std::string,int> placas;

int siguienteCelda;

public:

Parqueadero();

void procesarPlaca(
std::string placa
);

};

#endif