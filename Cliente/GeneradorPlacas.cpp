#include "GeneradorPlacas.h"

#include <vector>
#include <cstdlib>

using namespace std;

string GeneradorPlacas::generar(){

static vector<string> placas={
"ABC123",
"XYZ999",
"JKL456",
"ABC123",
"MNO888",
"XYZ999",
"PQR777"
};

static int indice=0;

string placa=
placas[indice];

indice++;

if(
indice>=placas.size()
)
indice=0;

return placa;

}