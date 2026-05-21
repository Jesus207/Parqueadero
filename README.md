## Gestión de Parqueadero
## Descripción
Este proyecto implementa un sistema distribuido para la gestión de un parqueadero, utilizando una arquitectura cliente-servidor en C++ con comunicación mediante sockets y un visualizador en Python.
El sistema simula la entrada y salida de vehículos mediante la generación automática de placas, asignación dinámica de celdas y actualización en tiempo real del estado del parqueadero.

## Características principales
•	Generación automática de placas vehiculares
•	Comunicación en tiempo real mediante sockets TCP/IP
•	Gestión eficiente de vehículos con estructuras de datos
•	Integración entre C++ y Python mediante librerías dinámicas
•	Visualización del estado del parqueadero
•	Detección automática de entrada y salida de vehículos

## Arquitectura del sistema
El sistema está compuesto por los siguientes módulos:
•	Generador (C++)
Genera placas aleatorias de vehículos.
•	Cliente (C++)
Envía las placas al servidor mediante sockets.
•	Servidor (C++)
Procesa las placas recibidas y gestiona el estado del parqueadero.
•	Librería Dinámica (C++)
Permite la comunicación entre el backend en C++ y el visualizador en Python.
•	Parqueadero (C++)
Contiene la lógica principal del sistema y administra las celdas.
•	Visualizador (Python)
Muestra el estado actual del parqueadero.

## Funcionamiento del sistema
1.	Se genera una placa aleatoria
2.	El cliente envía la placa al servidor
3.	El servidor procesa la información:
o	Si la placa no existe → el vehículo entra
o	Si la placa ya existe → el vehículo sale
4.	Se asigna o libera una celda
5.	El visualizador muestra los cambios

## Estructuras de datos utilizadas
El sistema utiliza:
unordered_map<string, int>
Esto permite:
•	Búsqueda en tiempo constante O(1)
•	Inserción eficiente
•	Eliminación rápida

## Diagrama UML
El diagrama UML del sistema se encuentra en la carpeta 

## Ejecución del proyecto
1. Compilar el servidor
g++ Servidor/Servidor.cpp Servidor/Parqueadero.cpp -o servidor
2. Compilar el cliente
g++ Cliente/Cliente.cpp -o cliente
3. Ejecutar el servidor
./servidor
4. Ejecutar el cliente
./cliente
5. Ejecutar el visualizador
python3 Visualizador/visualizador.py

## Estructura del proyecto
Parqueadero/
├── Cliente/
├── Generador/
├── Libreria/
├── Servidor/
├── Visualizador/
├── docs/
│   └── uml_clases.png
├── README.md

## Tecnologías utilizadas
•	C++
•	Python
•	Sockets TCP/IP
•	Librerías dinámicas (.so)
•	SWIG

## JESUS REINO – MIGUELANGEL RAMIREZ
