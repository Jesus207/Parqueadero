#include <iostream>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <winsock2.h>
#include <ws2tcpip.h>
#include "GeneradorPlacas.h"

#pragma comment(lib, "ws2_32.lib")

using namespace std;

int main() {

    srand(time(NULL));

    WSADATA wsa;
    WSAStartup(MAKEWORD(2,2), &wsa);

    SOCKET sock = socket(AF_INET, SOCK_STREAM, 0);

    if (sock == INVALID_SOCKET) {
        cout << "Error creando socket cliente" << endl;
        return 1;
    }

    sockaddr_in servidor;
    servidor.sin_family = AF_INET;
    servidor.sin_port = htons(8080);
    servidor.sin_addr.s_addr = inet_addr("127.0.0.1"); // IP del servidor

    while (connect(sock, (sockaddr*)&servidor, sizeof(servidor)) < 0) {
        cout << "Reintentando conexión..." << endl;
        Sleep(2000);
    }

    cout << "Conectado al servidor" << endl;

    GeneradorPlacas gen;

    // Generar pool de 20 placas únicas
    vector<string> pool;
    while (pool.size() < 20) {
        string p = gen.generar();
        if (find(pool.begin(), pool.end(), p) == pool.end()) {
            pool.push_back(p);
        }
    }

    vector<string> placasEnviadas;

    while (true) {

        string placa;

        // 30% probabilidad de sacar un carro parqueado
        if (!placasEnviadas.empty() && rand() % 10 < 3) {
            placa = placasEnviadas[rand() % placasEnviadas.size()];
            placasEnviadas.erase(
                remove(placasEnviadas.begin(), placasEnviadas.end(), placa),
                placasEnviadas.end()
            );
        } else {
            placa = pool[rand() % pool.size()];
            if (find(placasEnviadas.begin(), placasEnviadas.end(), placa) == placasEnviadas.end()) {
                placasEnviadas.push_back(placa);
            }
        }

        send(sock, placa.c_str(), placa.size(), 0);
        cout << "Enviado: " << placa << endl;
        Sleep((2 + rand() % 4) * 1000);
    }

    closesocket(sock);
    WSACleanup();

    return 0;
}