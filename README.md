## Gestión de Parqueadero

El presente proyecto consiste en el desarrollo de un sistema de parqueadero simulado que representa de manera dinámica la gestión de vehículos en un entorno controlado. A través de una arquitectura cliente-servidor, el sistema permite la generación, envío y procesamiento de placas vehiculares en tiempo real, simulando el comportamiento de entrada y salida de automóviles en un estacionamiento con capacidad limitada.

El proyecto integra tecnologías como C++ para la lógica principal y la comunicación mediante sockets TCP/IP, y Python para la visualización del estado del sistema. La comunicación entre módulos se complementa mediante un archivo de eventos que permite sincronizar la información entre los procesos del sistema.

Más allá de su implementación técnica, el proyecto busca aplicar conceptos fundamentales como la comunicación entre procesos, el uso de estructuras de datos y la integración de distintos lenguajes de programación en una solución funcional y visualmente comprensible.

## Características principales

• Sistema basado en arquitectura cliente-servidor con comunicación mediante sockets TCP/IP.
• Simulación de un parqueadero con 12 celdas organizadas en una matriz 3x4.
• Generación automática de placas vehiculares de forma aleatoria.
• Detección de entrada y salida de vehículos mediante verificación de placas repetidas.
• Asignación dinámica de espacios disponibles.
• Registro de eventos en un archivo de texto como mecanismo de sincronización.
• Visualización del estado del parqueadero en tiempo real mediante Python.
• Automatización del sistema mediante un script de ejecución.

## Arquitectura del sistema

El sistema está compuesto por los siguientes módulos:

• Cliente (C++)
Genera placas vehiculares aleatorias y las envía al servidor mediante sockets TCP/IP.

• Servidor (C++)
Recibe las placas enviadas por el cliente, procesa la información y gestiona el estado del parqueadero.

• Parqueadero (C++)
Contiene la lógica principal del sistema y administra la asignación y liberación de celdas.

• Archivo de eventos (evento.txt)
Almacena los registros generados por el servidor, incluyendo placas, tipo de evento y celdas asignadas.

• Librería dinámica (C++ / SWIG)
Facilita la integración entre componentes en C++ y Python (uso auxiliar dentro del sistema).

• Visualizador (Python)
Lee el archivo de eventos y muestra el estado del parqueadero mediante una interfaz ASCII.

## Funcionamiento del sistema

El sistema opera bajo una arquitectura cliente-servidor. El cliente genera placas vehiculares aleatorias en intervalos de tiempo y las envía al servidor mediante una conexión TCP/IP.

El servidor recibe cada placa y verifica su estado dentro del sistema. Si la placa no se encuentra registrada, se interpreta como una entrada y se asigna una celda disponible de forma aleatoria. Si la placa ya existe, se interpreta como una salida y se libera la celda correspondiente.

Cada evento es registrado en el archivo evento.txt, el cual actúa como mecanismo de comunicación entre el servidor y el visualizador. Este último consulta periódicamente el archivo para actualizar en tiempo real el estado del parqueadero, representado como una matriz de 12 espacios.

El sistema completo se ejecuta mediante un script automatizado que compila y lanza todos los módulos.

## Estructuras de datos utilizadas

El sistema emplea diferentes estructuras de datos para la gestión de la información:

La estructura principal es una matriz bidimensional, implementada mediante un DataFrame en Python, que representa el parqueadero con 12 celdas organizadas en 3 filas por 4 columnas.

En C++ se utiliza un vector dinámico (vector<string>) para el manejo de las placas vehiculares, permitiendo almacenar y consultar el estado de cada vehículo.

Adicionalmente, se emplean estructuras dinámicas auxiliares para el manejo de posiciones disponibles durante la asignación de celdas.

Finalmente, el sistema utiliza un archivo secuencial (evento.txt) como mecanismo de persistencia y comunicación entre procesos.

## Ejecución del proyecto
Abrir una terminal en la raíz del proyecto
Dar permisos al script (solo primera vez):
chmod +x iniciar.sh
Ejecutar el sistema:
./iniciar.sh
## Estructura del proyecto
Parqueadero/
│
├── Cliente/
│   ├── Cliente.cpp
│   ├── GeneradorPlacas.cpp
│   └── GeneradorPlacas.h
│
├── Servidor/
│   ├── Servidor.cpp
│   ├── Parqueadero.cpp
│   └── Parqueadero.h
│
├── Libreria/
│   ├── ParqueaderoLib.cpp
│   ├── ParqueaderoLib.h
│   ├── ParqueaderoLib.i
│   ├── ParqueaderoLib_wrap.cxx
│   └── _ParqueaderoLib.so
│
├── visualizador.py
├── iniciar.sh
├── evento.txt
├── README.md
└── uml.txt
## Tecnologías utilizadas

• C++
• Python
• Sockets TCP/IP
• SWIG
• Pandas
• Bash
• Git
• Linux (entorno de ejecución)

## Autores

Jesus Reino – Miguel Ángel Ramírez