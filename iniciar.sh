#!/bin/bash

echo "Compilando libreria..."

cd Libreria

g++ -shared -fPIC \
ParqueaderoLib.cpp \
-o libparqueadero.so

cd ../Servidor

g++ Servidor.cpp \
Parqueadero.cpp \
../Libreria/ParqueaderoLib.cpp \
-o servidor

cd ../Cliente

g++ Cliente.cpp \
GeneradorPlacas.cpp \
-o cliente

cd ..

echo "Iniciando..."

(
cd Servidor
./servidor
)&

sleep 2

(
cd Cliente
./cliente
)&

sleep 2

(
cd Visualizador
python3 visualizador.py
)