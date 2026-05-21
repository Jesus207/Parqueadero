## Gestión de Parqueadero
## Descripción
Este proyecto simula el funcionamiento de un parqueadero mediante un sistema distribuido que utiliza comunicación cliente-servidor con sockets en C++ y un visualizador en Python.
El sistema permite gestionar la entrada y salida de vehículos mediante la generación automática de placas, asignación de celdas y liberación de espacios cuando una placa se repite.

## Tecnologías utilizadas
•	C++
•	Python
•	Sockets TCP/IP
•	Librerías dinámicas (.so)
•	SWIG (para conexión C++ ↔ Python)
## Arquitectura del sistema
El sistema está compuesto por varios módulos:
1.	Generador (C++)
-	Genera placas aleatorias cada cierto tiempo.
2.	Cliente (C++)
-	Envía las placas al servidor mediante sockets.
3.	Servidor (C++)
-	Recibe placas
-	Gestiona la lógica del parqueadero
-	Asigna o libera celdas
4.	Librería dinámica
-	Permite conectar C++ con Python
5.	Visualizador (Python)
-	Muestra el estado del parqueadero

## Estructuras de datos utilizadas
Se utiliza una estructura tipo HashMap (diccionario) para almacenar:
•	Placa del vehículo
•	Hora de entrada
•	Celda asignada
¿Por qué?
•	Búsqueda rápida O(1)
•	Inserción eficiente
•	Eliminación rápida
Esto permite detectar rápidamente si una placa ya existe (salida del vehículo).
Funcionamiento del sistema
1.	Se genera una placa automáticamente
2.	Se envía al servidor
3.	El servidor:
-	Si la placa no existe → asigna celda
-	Si la placa ya existe → libera celda
4.	El visualizador muestra los cambios en tiempo real

## Ejecución del proyecto

Servidor:

cd Servidor

./servidor

Cliente:

cd Cliente

./cliente

Visualizador:

cd Visualizador

python3 visualizador.py

## UML
El diagrama UML del sistema se encuentra en la carpeta docs o en el archivo correspondiente del repositorio.


## Jesus Reino – Miguelangel Ramirez