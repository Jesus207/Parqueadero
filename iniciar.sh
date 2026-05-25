#!/bin/bash

echo "=================================="
echo "   INICIANDO SISTEMA PARQUEADERO"
echo "=================================="

# Limpiar archivo de eventos
> evento.txt

echo "Compilando servidor..."

g++ \
Servidor/Servidor.cpp \
Servidor/Parqueadero.cpp \
-o servidor

if [ $? -ne 0 ]; then
    echo "ERROR compilando servidor"
    exit 1
fi

echo "Compilando cliente..."

g++ \
Cliente/Cliente.cpp \
Cliente/GeneradorPlacas.cpp \
-o cliente

if [ $? -ne 0 ]; then
    echo "ERROR compilando cliente"
    exit 1
fi

echo "Servidor compilado"
echo "Cliente compilado"

# Iniciar servidor
echo "Iniciando servidor..."

./servidor &
SERVER_PID=$!

sleep 2

# Iniciar cliente
echo "Iniciando cliente..."

./cliente &
CLIENT_PID=$!

sleep 2

# Iniciar visualizador
echo "Iniciando visualizador..."

python3 visualizador.py &
VISUAL_PID=$!

echo "=================================="
echo "Sistema corriendo"
echo "Servidor PID: $SERVER_PID"
echo "Cliente PID: $CLIENT_PID"
echo "Visualizador PID: $VISUAL_PID"
echo "=================================="

trap "
echo ''
echo 'Cerrando sistema...'

kill $SERVER_PID 2>/dev/null
kill $CLIENT_PID 2>/dev/null
kill $VISUAL_PID 2>/dev/null

rm -f servidor
rm -f cliente

exit
" INT

wait