#include <iostream>
#include <cstring>
#include <unistd.h>
#include <arpa/inet.h>
#include <fstream>
#include <ctime>

#include "Parqueadero.h"

using namespace std;

Parqueadero parqueadero;

int main() {

    int servidor_fd, cliente_fd;
    sockaddr_in direccion;
    char buffer[1024];

    servidor_fd = socket(AF_INET, SOCK_STREAM, 0);

    if (servidor_fd < 0) {
        cout << "Error creando socket" << endl;
        return 1;
    }

    direccion.sin_family = AF_INET;
    direccion.sin_addr.s_addr = INADDR_ANY;
    direccion.sin_port = htons(8080);

    if (bind(servidor_fd, (sockaddr*)&direccion, sizeof(direccion)) < 0) {
        cout << "Error en bind" << endl;
        return 1;
    }

    listen(servidor_fd, 3);

    cout << "Servidor esperando..." << endl;

    socklen_t tam = sizeof(direccion);

    cliente_fd = accept(servidor_fd, (sockaddr*)&direccion, &tam);

    if (cliente_fd < 0) {
        cout << "Error en accept" << endl;
        return 1;
    }

    cout << "Cliente conectado" << endl;

    while (true) {

        memset(buffer, 0, sizeof(buffer));

        int n = read(cliente_fd, buffer, sizeof(buffer) - 1);

        // Si el cliente se desconecta
        if (n <= 0) {
            cout << "Cliente desconectado" << endl;
            break;
        }

        buffer[n] = '\0';

        // Placa recibida
        string placa(buffer);

        cout << "Placa recibida: "
            << placa
            << endl;

        // Procesar entrada / salida
        string respuesta =
            parqueadero.procesarPlaca(placa);

        cout << respuesta << endl;

        // Guardar evento en archivo
        ofstream archivo(
            "evento.txt",
            ios::app
        );

        if (archivo.is_open()) {

            time_t ahora = time(0);

            archivo << respuesta
                    << " | "
                    << ctime(&ahora);

            archivo.close();
        }

        // Respuesta al cliente
        send(
            cliente_fd,
            respuesta.c_str(),
            respuesta.size(),
            0
        );
    }
    close(cliente_fd);
    close(servidor_fd);
    return 0;
}