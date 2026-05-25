import pandas as pd
import random
import time
import os

ARCHIVO = "evento.txt"

# Parqueadero 3x4 = 12 puestos
filas = 3
columnas = 4

parqueadero = pd.DataFrame(
    [["LIBRE" for _ in range(columnas)] for _ in range(filas)],
    index=["F1", "F2", "F3"],
    columns=["C1", "C2", "C3", "C4"]
)

ultima_linea = ""

def obtener_placa():

    global ultima_linea

    try:
        with open(ARCHIVO, "r") as f:
            lineas = f.readlines()

        if not lineas:
            return None

        ultima = lineas[-1].strip()

        # Evita procesar la misma línea varias veces
        if ultima == ultima_linea:
            return None

        ultima_linea = ultima

        # Ej:
        # ENTRADA -> ABC123 | Celda 5 ocupada | ...
        # SALIDA -> ABC123 | Celda 5 liberada | ...

        if "->" in ultima:
            placa = ultima.split("->")[1].split("|")[0].strip()
            return placa

    except:
        return None

    return None


def buscar_placa(placa):

    for fila in parqueadero.index:
        for col in parqueadero.columns:

            if parqueadero.loc[fila, col] == placa:
                return (fila, col)

    return None


def celdas_libres():

    libres = []

    for fila in parqueadero.index:
        for col in parqueadero.columns:

            if parqueadero.loc[fila, col] == "LIBRE":
                libres.append((fila, col))

    return libres

def actualizar(placa):

    # Revisar si la placa YA está parqueada
    for fila in parqueadero.index:
        for col in parqueadero.columns:

            valor = parqueadero.loc[fila, col]

            if valor == placa:

                # El carro salió
                parqueadero.loc[fila, col] = "LIBRE"

                print(
                    f"SALIDA -> {placa}"
                )

                return


    # Si NO existe -> entrada
    libres = []

    for fila in parqueadero.index:
        for col in parqueadero.columns:

            if parqueadero.loc[fila, col] == "LIBRE":

                libres.append((fila, col))


    # Si no hay espacio
    if len(libres) == 0:

        print("PARQUEADERO LLENO")

        return


    # Elegir celda aleatoria
    lugar = random.choice(libres)

    f, c = lugar

    parqueadero.loc[f, c] = placa

    print(
        f"ENTRADA -> {placa}"
    )
    
def puesto(nombre, placa):

    if placa == "LIBRE":

        carro = "░░░░░"
        texto = "LIBRE"

    else:

        carro = "🚘"
        texto = placa[:6]

    return f"[{nombre}] {carro:<5} {texto:<6}"


def dibujar():

    os.system("clear")
    # Windows:
    # os.system("cls")

    print("""
_________________________________________
| [ENTRADA]                             |
|    ===[/]=== (Barrera)                |
|_______   _____________________________|
        | |
________| |_____________________________|
|                                       |
""")

    print(
        f"| {puesto('A1', parqueadero.loc['F1','C1'])}   "
        f"{puesto('A2', parqueadero.loc['F1','C2'])} |"
    )

    print(
        f"| {puesto('A3', parqueadero.loc['F1','C3'])}   "
        f"{puesto('A4', parqueadero.loc['F1','C4'])} |"
    )

    print("|                                       |")

    print(
        f"| {puesto('B1', parqueadero.loc['F2','C1'])}   "
        f"{puesto('B2', parqueadero.loc['F2','C2'])} |"
    )

    print(
        f"| {puesto('B3', parqueadero.loc['F2','C3'])}   "
        f"{puesto('B4', parqueadero.loc['F2','C4'])} |"
    )

    print("|                                       |")

    print(
        f"| {puesto('C1', parqueadero.loc['F3','C1'])}   "
        f"{puesto('C2', parqueadero.loc['F3','C2'])} |"
    )

    print(
        f"| {puesto('C3', parqueadero.loc['F3','C3'])}   "
        f"{puesto('C4', parqueadero.loc['F3','C4'])} |"
    )

    print("""
|_______________________________________|
| [ SALIDA ]                            |
|    ===[\\]===                          |
|_______________________________________|
""")


print("Visualizador iniciado...\n")

while True:

    placa = obtener_placa()

    if placa:
        actualizar(placa)

    dibujar()

    time.sleep(2)