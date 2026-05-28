import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from datetime import datetime
import random



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")



placas_activas = {}

celdas_disponibles = list(range(1, 11))



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



def actualizar_tabla():

    hora = datetime.now().strftime('%H:%M:%S')

    

    # 50% probabilidad de que salga un vehículo
    if placas_activas and random.random() < 0.5:

        placa = random.choice(
            list(placas_activas.keys())
        )

        celda = placas_activas[placa]

        del placas_activas[placa]

        celdas_disponibles.append(celda)

        tabla.insert(
            '',
            tk.END,
            values=(
                placa,
                hora,
                celda,
                'SALIDA'
            )
        )

    

    else:

        # Solo entra si hay espacio
        if celdas_disponibles:

            placa = generar_placa()

            celda = celdas_disponibles.pop(0)

            placas_activas[placa] = celda

            tabla.insert(
                '',
                tk.END,
                values=(
                    placa,
                    hora,
                    celda,
                    'ENTRADA'
                )
            )

  

    total_label.configure(
        text=f'Vehículos en parqueadero: {len(placas_activas)}'
    )

    # Ejecutar nuevamente cada 3 segundos
    ventana.after(3000, actualizar_tabla)



ventana = ctk.CTk()

ventana.title(
    'Sistema Inteligente de Parqueadero'
)

ventana.geometry('900x600')



titulo = ctk.CTkLabel(
    ventana,
    text='VISUALIZADOR DEL PARQUEADERO',
    font=('Arial', 26, 'bold')
)

titulo.pack(pady=20)


tabla = ttk.Treeview(
    ventana,
    columns=(
        'Placa',
        'Hora',
        'Celda',
        'Estado'
    ),
    show='headings',
    height=15
)

# Encabezados
tabla.heading('Placa', text='Placa')
tabla.heading('Hora', text='Hora')
tabla.heading('Celda', text='Celda')
tabla.heading('Estado', text='Estado')

# Tamaño columnas
tabla.column('Placa', width=150)
tabla.column('Hora', width=150)
tabla.column('Celda', width=100)
tabla.column('Estado', width=150)

tabla.pack(pady=20)



total_label = ctk.CTkLabel(
    ventana,
    text='Vehículos en parqueadero: 0',
    font=('Arial', 16, 'bold')
)

total_label.pack(pady=10)



actualizar_tabla()



ventana.mainloop()