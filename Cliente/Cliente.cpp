#include <iostream>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <winsock2.h>
#include <ws2tcpip.h>

#pragma comment(lib, "ws2_32.lib")

using namespace std;

string generarPlaca() {
    string letras = "ABCDEFGHI";
    string numeros = "0123456789";

    string placa = "";

    placa += letras[rand() % letras.size()];
    placa += letras[rand() % letras.size()];
    placa += letras[rand() % letras.size()];
    placa += numeros[rand() % 10];
    placa += numeros[rand() % 10];
    placa += numeros[rand() % 10];

    return placa;
}

int main() {

    srand(time(NULL));

    // Inicializar Winsock
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
    servidor.sin_addr.s_addr = inet_addr("127.0.0.1");

    while (connect(sock, (sockaddr*)&servidor, sizeof(servidor)) < 0) {
        cout << "Reintentando conexión..." << endl;
        Sleep(2000); // Windows usa Sleep(ms)
    }

    cout << "Conectado al servidor" << endl;

    while (true) {

        string placa = generarPlaca();

        send(sock, placa.c_str(), placa.size(), 0);

        cout << "Enviado: " << placa << endl;

        Sleep((2 + rand() % 4) * 1000);
    }

    closesocket(sock);
    WSACleanup();

    return 0;
}