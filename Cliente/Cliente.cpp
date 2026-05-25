#include <iostream>
#include <cstring>
#include <unistd.h>
#include <arpa/inet.h>
#include <ctime>
#include <cstdlib>

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

    int sock = socket(AF_INET, SOCK_STREAM, 0);

    if (sock < 0) {
        cout << "Error creando socket cliente" << endl;
        return 1;
    }

    sockaddr_in servidor;
    servidor.sin_family = AF_INET;
    servidor.sin_port = htons(8080);
    servidor.sin_addr.s_addr = inet_addr("127.0.0.1");

    // 🔁 conexión con reintento
    while (connect(sock, (sockaddr*)&servidor, sizeof(servidor)) < 0) {
        cout << "Reintentando conexión..." << endl;
        sleep(2);
    }

    cout << "Conectado al servidor" << endl;

    while (true) {

        string placa = generarPlaca();

        send(sock, placa.c_str(), placa.size(), 0);

        cout << "Enviado: " << placa << endl;

        sleep(2 + rand() % 4); // 2 a 5 segundos
    }

    return 0;
}