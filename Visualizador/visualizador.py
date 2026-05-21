import sys
import tkinter as tk

sys.path.append(
    "/workspaces/Parqueadero/Libreria"
)

import ParqueaderoLib

parqueadero = {}

ventana = tk.Tk()

ventana.title(
    "Parqueadero"
)

ventana.geometry(
    "700x500"
)

titulo = tk.Label(
    ventana,
    text="VISUALIZADOR DEL PARQUEADERO",
    font=("Arial", 16, "bold")
)

titulo.pack(
    pady=10
)

frame = tk.Frame(
    ventana
)

frame.pack()

estado = tk.Label(
    ventana,
    text="Esperando..."
)

estado.pack(
    pady=20
)

celdas = []

for i in range(10):

    lbl = tk.Label(
        frame,

        text=f"Celda {i+1}\nLIBRE",

        width=15,

        height=5,

        bg="green",

        fg="white",

        relief="raised"
    )

    lbl.grid(
        row=i//5,
        column=i%5,
        padx=10,
        pady=10
    )

    celdas.append(
        lbl
    )

ultimo = ""


def actualizar():

    global ultimo

    evento = ParqueaderoLib.obtenerEvento()

    if (
        evento
        and
        evento != ultimo
    ):

        partes = evento.split(
            "|"
        )

        placa = (
            partes[0]
            .split("->")[1]
            .strip()
        )

        texto = partes[1]

        numero = int(
            ''.join(
                filter(
                    str.isdigit,
                    texto
                )
            )
        )

        celda = numero - 1

        if (
            "ENTRADA"
            in evento
        ):

            parqueadero[
                celda
            ] = placa

            celdas[
                celda
            ].config(

                text=f"Celda {celda+1}\n{placa}",

                bg="red"
            )

        else:

            if (
                celda
                in parqueadero
            ):

                del parqueadero[
                    celda
                ]

            celdas[
                celda
            ].config(

                text=f"Celda {celda+1}\nLIBRE",

                bg="green"
            )

        estado.config(
            text=evento
        )

        ultimo = evento

    ventana.after(
        1000,
        actualizar
    )


actualizar()

ventana.mainloop()