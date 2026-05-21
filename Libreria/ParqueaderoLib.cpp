#include "ParqueaderoLib.h"

#include <fstream>
#include <string>

using namespace std;

void guardarEvento(
const char* evento
){

ofstream archivo(
"/workspaces/Parqueadero/evento.txt"
);

archivo<<evento;

archivo.close();

}

const char*
obtenerEvento(){

static string texto;

ifstream archivo(
"/workspaces/Parqueadero/evento.txt"
);

getline(
archivo,
texto
);

archivo.close();

return texto.c_str();

}