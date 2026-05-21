#include <iostream>
#include <cstring>

#include <unistd.h>
#include <arpa/inet.h>

#include "Parqueadero.h"

using namespace std;

Parqueadero parqueadero;

int main() {

    int servidor_fd, cliente_fd;

    sockaddr_in direccion;

    char buffer[1024]={0};

    servidor_fd = socket(
        AF_INET,
        SOCK_STREAM,
        0
    );

    direccion.sin_family = AF_INET;

    direccion.sin_addr.s_addr = INADDR_ANY;

    direccion.sin_port = htons(8080);

    bind(
        servidor_fd,
        (sockaddr*)&direccion,
        sizeof(direccion)
    );

    listen(
        servidor_fd,
        3
    );

    cout<<"Servidor esperando..."<<endl;

    int tam = sizeof(direccion);

    cliente_fd=
    accept(
        servidor_fd,
        (sockaddr*)&direccion,
        (socklen_t*)&tam
    );

    while(true){

        memset(buffer,0,1024);

        read(
            cliente_fd,
            buffer,
            1024
        );

        parqueadero.procesarPlaca(
        buffer
        );
    }

    return 0;
}