import time
import sys

from rich.console import Console
from rich.table import Table
from rich.live import Live

sys.path.append("/workspaces/Parqueadero/Libreria")

import ParqueaderoLib

console = Console()

parqueadero = {}
ultimo = "Esperando..."


def generar_tabla():
    table = Table(title="🚗 SISTEMA DE PARQUEADERO EN TIEMPO REAL")

    table.add_column("Celdas", justify="center", style="cyan")
    table.add_column("Estado", justify="center")
    table.add_column("Placa", justify="center", style="green")

    for i in range(1, 11):
        if i in parqueadero:
            table.add_row(str(i), "OCUPADA 🔴", parqueadero[i])
        else:
            table.add_row(str(i), "LIBRE 🟢", "---")

    return table


def actualizar():
    global ultimo

    console.print("Iniciando sistema de visualización...\n", style="bold yellow")

    with Live(generar_tabla(), refresh_per_second=2, console=console) as live:

        while True:
            try:
                evento = ParqueaderoLib.obtenerEvento()

                if not evento or evento == ultimo:
                    time.sleep(1)
                    continue

                partes = evento.split("|")

                placa = partes[0].split("->")[1].strip()
                numero = int(''.join(filter(str.isdigit, partes[1])))

                if "ENTRADA" in evento:
                    parqueadero[numero] = placa
                else:
                    if numero in parqueadero:
                        del parqueadero[numero]

                ultimo = evento

                live.update(generar_tabla())

            except Exception as e:
                console.print(f"[red]ERROR: {e}[/red]")

            time.sleep(1)


if __name__ == "__main__":
    actualizar()