#!/bin/bash

echo "=================================="
echo "   INICIANDO SISTEMA PARQUEADERO"
echo "=================================="

# Verificar archivos
if [ ! -f "./servidor" ]; then
    echo "ERROR: servidor no encontrado"
    exit 1
fi

if [ ! -f "./cliente" ]; then
    echo "ERROR: cliente no encontrado"
    exit 1
fi

if [ ! -f "./visualizador.py" ]; then
    echo "ERROR: visualizador.py no encontrado"
    exit 1
fi

# Crear archivo de eventos si no existe
touch evento.txt

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

# Cerrar todo al salir
trap "
echo 'Cerrando sistema...'
kill $SERVER_PID
kill $CLIENT_PID
kill $VISUAL_PID
exit
" INT

wait