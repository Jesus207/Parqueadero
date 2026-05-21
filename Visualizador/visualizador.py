import ctypes
import time

lib = ctypes.CDLL(
    "/workspaces/Parqueadero/Libreria/libparqueadero.so"
)

lib.obtenerEvento.restype = ctypes.c_char_p

ultimo = ""

print(
    "VISUALIZADOR DEL PARQUEADERO"
)

while True:

    evento = (
        lib.obtenerEvento()
        .decode()
    )

    if (
        evento
        and
        evento != ultimo
    ):

        print(
            evento
        )

        ultimo = evento

    time.sleep(
        1
    )