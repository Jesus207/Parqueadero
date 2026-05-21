#include <iostream>

#include <thread>

#include <chrono>

#include <cstring>

#include <unistd.h>

#include <arpa/inet.h>

#include "GeneradorPlacas.h"

using namespace std;

int main(){

srand(time(NULL));

GeneradorPlacas g;

int socket_cliente;

sockaddr_in servidor;

socket_cliente=
socket(
AF_INET,
SOCK_STREAM,
0
);

servidor.sin_family=
AF_INET;

servidor.sin_port=
htons(8080);

inet_pton(
AF_INET,
"127.0.0.1",
&servidor.sin_addr
);

connect(
socket_cliente,
(sockaddr*)&servidor,
sizeof(servidor)
);

while(true){

string placa=
g.generar();

send(
socket_cliente,
placa.c_str(),
placa.size(),
0
);

cout
<<"Enviada: "
<<placa
<<endl;

int espera;

if(rand()%2==0)
espera=2;

else
espera=5;

this_thread::sleep_for(
chrono::seconds(
espera
)
);

}

return 0;

}