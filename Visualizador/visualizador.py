import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from datetime import datetime
import random



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")



TOTAL_CELDAS = 10


placas_activas = {}


celdas_disponibles = list(range(1, TOTAL_CELDAS + 1))


labels_celdas = {}


def generar_placa():

    letras = ''.join(
        random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        for _ in range(3)
    )

    numeros = ''.join(
        random.choice('0123456789')
        for _ in range(3)
    )

    return letras + numeros



def actualizar_reloj():

    hora_actual = datetime.now().strftime("%H:%M:%S")

    reloj_label.configure(text=hora_actual)

    ventana.after(1000, actualizar_reloj)



def actualizar_mapa():

    
    for i in range(1, TOTAL_CELDAS + 1):

        nombre = f"C{i}"

        labels_celdas[nombre].configure(
            text=nombre,
            fg_color="#14532d"  # verde
        )

    
    for placa, celda in placas_activas.items():

        nombre = f"C{celda}"

        labels_celdas[nombre].configure(
            text=placa,
            fg_color="#7f1d1d"  # rojo
        )



def actualizar_tabla():

    hora = datetime.now().strftime('%H:%M:%S')

    

    if placas_activas and random.random() < 0.5:

        placa = random.choice(
            list(placas_activas.keys())
        )

        celda = placas_activas[placa]

        del placas_activas[placa]

        celdas_disponibles.append(celda)

        tabla.insert(
            '',
            0,
            values=(
                placa,
                hora,
                f"C{celda}",
                'SALIDA'
            ),
            tags=('salida',)
        )

  

    else:

        if celdas_disponibles:

            placa = generar_placa()

            celda = celdas_disponibles.pop(0)

            placas_activas[placa] = celda

            tabla.insert(
                '',
                0,
                values=(
                    placa,
                    hora,
                    f"C{celda}",
                    'ENTRADA'
                ),
                tags=('entrada',)
            )

    

    ocupados = len(placas_activas)

    disponibles = TOTAL_CELDAS - ocupados

    ocupados_label.configure(
        text=f'Ocupadas: {ocupados}'
    )

    disponibles_label.configure(
        text=f'Disponibles: {disponibles}'
    )

    porcentaje = int((ocupados / TOTAL_CELDAS) * 100)

    porcentaje_label.configure(
        text=f'Ocupación: {porcentaje}%'
    )

    # Actualizar mapa visual
    actualizar_mapa()

    # Repetir simulación
    ventana.after(3000, actualizar_tabla)



ventana = ctk.CTk()

ventana.title("SMART PARKING SYSTEM")

ventana.geometry("1400x850")



titulo = ctk.CTkLabel(
    ventana,
    text="SMART PARKING SYSTEM",
    font=("Arial", 38, "bold")
)

titulo.pack(pady=20)

subtitulo = ctk.CTkLabel(
    ventana,
    text="Sistema Inteligente de Gestión de Parqueadero",
    font=("Arial", 18)
)

subtitulo.pack()



reloj_label = ctk.CTkLabel(
    ventana,
    text="",
    font=("Arial", 28, "bold"),
    text_color="#00FFFF"
)

reloj_label.pack(pady=10)



stats_frame = ctk.CTkFrame(
    ventana,
    corner_radius=20
)

stats_frame.pack(
    fill="x",
    padx=20,
    pady=20
)

ocupados_label = ctk.CTkLabel(
    stats_frame,
    text="Ocupadas: 0",
    font=("Arial", 22, "bold"),
    text_color="#ff5555"
)

ocupados_label.pack(
    side="left",
    padx=40,
    pady=20
)

disponibles_label = ctk.CTkLabel(
    stats_frame,
    text="Disponibles: 10",
    font=("Arial", 22, "bold"),
    text_color="#50fa7b"
)

disponibles_label.pack(
    side="left",
    padx=40
)

porcentaje_label = ctk.CTkLabel(
    stats_frame,
    text="Ocupación: 0%",
    font=("Arial", 22, "bold"),
    text_color="#f1fa8c"
)

porcentaje_label.pack(
    side="right",
    padx=40
)



main_frame = ctk.CTkFrame(
    ventana
)

main_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)



left_frame = ctk.CTkFrame(
    main_frame,
    corner_radius=20
)

left_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=10,
    pady=10
)



mapa_titulo = ctk.CTkLabel(
    left_frame,
    text="MAPA DEL PARQUEADERO",
    font=("Arial", 26, "bold")
)

mapa_titulo.pack(pady=20)



mapa_frame = ctk.CTkFrame(
    left_frame,
    corner_radius=20
)

mapa_frame.pack(
    padx=20,
    pady=20
)

fila = 0
columna = 0

for i in range(1, TOTAL_CELDAS + 1):

    nombre = f"C{i}"

    celda = ctk.CTkLabel(
        mapa_frame,
        text=nombre,
        width=150,
        height=100,
        corner_radius=15,
        fg_color="#14532d",
        font=("Arial", 24, "bold")
    )

    celda.grid(
        row=fila,
        column=columna,
        padx=15,
        pady=15
    )

    labels_celdas[nombre] = celda

    columna += 1

    if columna > 4:

        columna = 0

        fila += 1



leyenda = ctk.CTkLabel(
    left_frame,
    text="🟩 Disponible     🟥 Ocupada",
    font=("Arial", 18)
)

leyenda.pack(pady=10)



right_frame = ctk.CTkFrame(
    main_frame,
    corner_radius=20
)

right_frame.pack(
    side="right",
    fill="both",
    expand=True,
    padx=10,
    pady=10
)



tabla_titulo = ctk.CTkLabel(
    right_frame,
    text="REGISTRO DE ACTIVIDAD",
    font=("Arial", 24, "bold")
)

tabla_titulo.pack(pady=20)



style = ttk.Style()

style.theme_use("default")

style.configure(
    "Treeview",
    background="#1f2937",
    foreground="white",
    rowheight=35,
    fieldbackground="#1f2937",
    font=("Arial", 12)
)

style.configure(
    "Treeview.Heading",
    font=("Arial", 14, "bold")
)



tabla = ttk.Treeview(
    right_frame,
    columns=(
        "Placa",
        "Hora",
        "Celda",
        "Estado"
    ),
    show="headings",
    height=18
)

tabla.heading("Placa", text="PLACA")
tabla.heading("Hora", text="HORA")
tabla.heading("Celda", text="CELDA")
tabla.heading("Estado", text="ESTADO")

tabla.column("Placa", width=150)
tabla.column("Hora", width=130)
tabla.column("Celda", width=100)
tabla.column("Estado", width=120)

# Colores filas
tabla.tag_configure(
    'entrada',
    background='#166534'
)

tabla.tag_configure(
    'salida',
    background='#991b1b'
)

tabla.pack(
    padx=20,
    pady=20,
    fill="both",
    expand=True
)



footer = ctk.CTkLabel(
    ventana,
    text="Sistema Inteligente de Parqueadero - Estructura de Datos",
    font=("Arial", 16)
)

footer.pack(pady=10)



actualizar_reloj()

actualizar_mapa()

actualizar_tabla()



ventana.mainloop()