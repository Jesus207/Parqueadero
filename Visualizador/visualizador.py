import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from datetime import datetime
import threading
import socket
import sys
import os

# Agregar carpeta Libreria al path para importar SWIG
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "Libreria"))
import ParqueaderoLib

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ── Librería ──
parqueadero = ParqueaderoLib.Parqueadero()
TOTAL_CELDAS = parqueadero.obtenerTotal()

labels_celdas = {}

# ── Funciones UI ──
def actualizar_reloj():
    hora_actual = datetime.now().strftime("%H:%M:%S")
    reloj_label.configure(text=hora_actual)
    ventana.after(1000, actualizar_reloj)

def actualizar_mapa():
    estado = parqueadero.obtenerEstado()
    # formato: "A1:LIBRE;A2:ABC123;..."
    for parte in estado.split(";"):
        if ":" not in parte:
            continue
        nombre, placa = parte.split(":")
        if placa == "LIBRE":
            labels_celdas[nombre].configure(
                text=nombre,
                fg_color="#14532d"
            )
        else:
            labels_celdas[nombre].configure(
                text=placa,
                fg_color="#7f1d1d"
            )

def procesar_evento(placa):
    resultado = parqueadero.procesarPlaca(placa)
    # formato: "ENTRADA|ABC123|A1|14:32:05" o "LLENO|..."
    partes = resultado.split("|")
    if len(partes) < 4:
        return

    tipo, placa_ev, celda, hora = partes

    if tipo == "LLENO":
        return

    tag = 'entrada' if tipo == "ENTRADA" else 'salida'

    # Insertar en tabla (hilo principal)
    ventana.after(0, lambda: tabla.insert(
        '', 0,
        values=(placa_ev, hora, celda, tipo),
        tags=(tag,)
    ))

    # Actualizar stats y mapa
    ventana.after(0, actualizar_stats)
    ventana.after(0, actualizar_mapa)

def actualizar_stats():
    ocupados = TOTAL_CELDAS - parqueadero.obtenerLibres()
    disponibles = parqueadero.obtenerLibres()
    porcentaje = int((ocupados / TOTAL_CELDAS) * 100)

    ocupados_label.configure(text=f'Ocupadas: {ocupados}')
    disponibles_label.configure(text=f'Disponibles: {disponibles}')
    porcentaje_label.configure(text=f'Ocupación: {porcentaje}%')

# ── Hilo socket ──
def escuchar_servidor():
    HOST = "127.0.0.1"  # IP del servidor (cambiar si es otra PC)
    PORT = 9090

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:
        try:
            s.connect((HOST, PORT))
            print("Conectado al servidor")
            break
        except:
            print("Reintentando conexión...")
            import time
            time.sleep(2)

    while True:
        try:
            data = s.recv(1024).decode("utf-8").strip()
            if not data:
                break
            print(f"Placa recibida: {data}")
            procesar_evento(data)
        except:
            break

    s.close()

# ── Construcción UI (igual a la tuya) ──
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

stats_frame = ctk.CTkFrame(ventana, corner_radius=20)
stats_frame.pack(fill="x", padx=20, pady=20)

ocupados_label = ctk.CTkLabel(
    stats_frame,
    text="Ocupadas: 0",
    font=("Arial", 22, "bold"),
    text_color="#ff5555"
)
ocupados_label.pack(side="left", padx=40, pady=20)

disponibles_label = ctk.CTkLabel(
    stats_frame,
    text=f"Disponibles: {TOTAL_CELDAS}",
    font=("Arial", 22, "bold"),
    text_color="#50fa7b"
)
disponibles_label.pack(side="left", padx=40)

porcentaje_label = ctk.CTkLabel(
    stats_frame,
    text="Ocupación: 0%",
    font=("Arial", 22, "bold"),
    text_color="#f1fa8c"
)
porcentaje_label.pack(side="right", padx=40)

main_frame = ctk.CTkFrame(ventana)
main_frame.pack(fill="both", expand=True, padx=20, pady=10)

left_frame = ctk.CTkFrame(main_frame, corner_radius=20)
left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

mapa_titulo = ctk.CTkLabel(
    left_frame,
    text="MAPA DEL PARQUEADERO",
    font=("Arial", 26, "bold")
)
mapa_titulo.pack(pady=20)

mapa_frame = ctk.CTkFrame(left_frame, corner_radius=20)
mapa_frame.pack(padx=20, pady=20)

# Celdas dinámicas desde la librería
estado_inicial = parqueadero.obtenerEstado()
nombres_celdas = [p.split(":")[0] for p in estado_inicial.split(";") if ":" in p]

fila = 0
columna = 0
for nombre in nombres_celdas:
    celda = ctk.CTkLabel(
        mapa_frame,
        text=nombre,
        width=150,
        height=100,
        corner_radius=15,
        fg_color="#14532d",
        font=("Arial", 24, "bold")
    )
    celda.grid(row=fila, column=columna, padx=15, pady=15)
    labels_celdas[nombre] = celda
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

leyenda = ctk.CTkLabel(
    left_frame,
    text="🟩 Disponible     🟥 Ocupada",
    font=("Arial", 18)
)
leyenda.pack(pady=10)

right_frame = ctk.CTkFrame(main_frame, corner_radius=20)
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

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
    columns=("Placa", "Hora", "Celda", "Estado"),
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
tabla.tag_configure('entrada', background='#166534')
tabla.tag_configure('salida', background='#991b1b')
tabla.pack(padx=20, pady=20, fill="both", expand=True)

footer = ctk.CTkLabel(
    ventana,
    text="Sistema Inteligente de Parqueadero - Estructura de Datos",
    font=("Arial", 16)
)
footer.pack(pady=10)

# ── Arranque ──
actualizar_reloj()
actualizar_mapa()

hilo = threading.Thread(target=escuchar_servidor, daemon=True)
hilo.start()

ventana.mainloop()