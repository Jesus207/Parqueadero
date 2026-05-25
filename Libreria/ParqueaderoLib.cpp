#include "ParqueaderoLib.h"
#include <fstream>
#include <string>

using namespace std;

void guardarEvento(const char* evento) {
    std::ofstream file("eventos.txt", std::ios::app);
    file << evento << std::endl;
}

const char* obtenerEvento() {
    static string texto;

    ifstream archivo("/workspaces/Parqueadero-V2.0/evento.txt");
    getline(archivo, texto);
    archivo.close();

    return texto.c_str();
}