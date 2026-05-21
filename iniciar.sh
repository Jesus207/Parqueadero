#!/bin/bash

echo "=================================="
echo " SISTEMA DE PARQUEADERO "
echo "=================================="

echo ""
echo "Compilando SWIG..."

cd Libreria || exit

swig -python -c++ ParqueaderoLib.i

g++ -fPIC -c \
ParqueaderoLib.cpp \
ParqueaderoLib_wrap.cxx \
-I/usr/include/python3.12

g++ -shared \
ParqueaderoLib.o \
ParqueaderoLib_wrap.o \
-o _ParqueaderoLib.so

g++ -shared -fPIC \
ParqueaderoLib.cpp \
-o libparqueadero.so

cd ..

echo ""
echo "Compilando servidor..."

cd Servidor || exit

g++ Servidor.cpp \
Parqueadero.cpp \
../Libreria/ParqueaderoLib.cpp \
-o servidor

cd ..

echo ""
echo "Compilando cliente..."

cd Cliente || exit

g++ Cliente.cpp \
GeneradorPlacas.cpp \
-o cliente

cd ..

echo ""
echo "Iniciando sistema..."

(
cd Servidor
./servidor
) &

sleep 2

(
cd Cliente
./cliente
) &

sleep 2

(
cd Visualizador
python3 visualizador.py
)

wait