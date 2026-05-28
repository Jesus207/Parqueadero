#include <iostream>
#include <cstring>
#include <winsock2.h>
#include <ws2tcpip.h>

#include "ParqueaderoLib.h"

using namespace std;

Parqueadero p;

int main() {

    WSADATA wsa;
    if (WSAStartup(MAKEWORD(2,2), &wsa) != 0) {
        cout << "Error iniciando Winsock" << endl;
        return 1;
    }

    SOCKET servidor_fd, cliente_fd;
    sockaddr_in direccion;
    char buffer[1024];

    servidor_fd = socket(AF_INET, SOCK_STREAM, 0);

    if (servidor_fd == INVALID_SOCKET) {
        cout << "Error creando socket: " << WSAGetLastError() << endl;
        return 1;
    }

    direccion.sin_family = AF_INET;
    direccion.sin_addr.s_addr = INADDR_ANY;
    direccion.sin_port = htons(8080);

    if (bind(servidor_fd, (sockaddr*)&direccion, sizeof(direccion)) < 0) {
        cout << "Error en bind: " << WSAGetLastError() << endl;
        return 1;
    }

    listen(servidor_fd, 3);

    cout << "Servidor esperando..." << endl;

    int tam = sizeof(direccion);

    cliente_fd = accept(servidor_fd, (sockaddr*)&direccion, &tam);

    if (cliente_fd == INVALID_SOCKET) {
        cout << "Error en accept: " << WSAGetLastError() << endl;
        return 1;
    }

    cout << "Cliente conectado" << endl;

    while (true) {

        memset(buffer, 0, sizeof(buffer));

        int n = recv(cliente_fd, buffer, sizeof(buffer) - 1, 0);

        if (n <= 0) {
            cout << "Cliente desconectado" << endl;
            break;
        }

        string placa(buffer);

        cout << "Placa recibida: " << placa << endl;

        string respuesta = p.procesarPlaca(placa);

        cout << respuesta << endl;

        send(cliente_fd, respuesta.c_str(), respuesta.size(), 0);
    }

    closesocket(cliente_fd);
    closesocket(servidor_fd);
    WSACleanup();

    return 0;
}