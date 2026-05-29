#include <iostream>
#include <cstring>
#include <winsock2.h>
#include <ws2tcpip.h>

#pragma comment(lib, "ws2_32.lib")

using namespace std;

int main() {

    WSADATA wsa;
    if (WSAStartup(MAKEWORD(2,2), &wsa) != 0) {
        cout << "Error iniciando Winsock" << endl;
        return 1;
    }

    // ── Socket para el cliente (puerto 8080) ──
    SOCKET srv_cliente = socket(AF_INET, SOCK_STREAM, 0);
    sockaddr_in dir_cliente;
    dir_cliente.sin_family = AF_INET;
    dir_cliente.sin_addr.s_addr = INADDR_ANY;
    dir_cliente.sin_port = htons(8080);

    bind(srv_cliente, (sockaddr*)&dir_cliente, sizeof(dir_cliente));
    listen(srv_cliente, 1);

    // ── Socket para el visualizador (puerto 9090) ──
    SOCKET srv_visual = socket(AF_INET, SOCK_STREAM, 0);
    sockaddr_in dir_visual;
    dir_visual.sin_family = AF_INET;
    dir_visual.sin_addr.s_addr = INADDR_ANY;
    dir_visual.sin_port = htons(9090);

    bind(srv_visual, (sockaddr*)&dir_visual, sizeof(dir_visual));
    listen(srv_visual, 1);

    cout << "Esperando visualizador en puerto 9090..." << endl;
    int tam = sizeof(dir_visual);
    SOCKET visual_fd = accept(srv_visual, (sockaddr*)&dir_visual, &tam);
    cout << "Visualizador conectado" << endl;

    cout << "Esperando cliente en puerto 8080..." << endl;
    tam = sizeof(dir_cliente);
    SOCKET cliente_fd = accept(srv_cliente, (sockaddr*)&dir_cliente, &tam);
    cout << "Cliente conectado" << endl;

    char buffer[1024];

    while (true) {

        memset(buffer, 0, sizeof(buffer));
        int n = recv(cliente_fd, buffer, sizeof(buffer) - 1, 0);

        if (n <= 0) {
            cout << "Cliente desconectado" << endl;
            break;
        }

        string placa(buffer);
        cout << "Placa recibida: " << placa << endl;

        // Reenviar placa al visualizador
        send(visual_fd, placa.c_str(), placa.size(), 0);
    }

    closesocket(cliente_fd);
    closesocket(visual_fd);
    closesocket(srv_cliente);
    closesocket(srv_visual);
    WSACleanup();

    return 0;
}