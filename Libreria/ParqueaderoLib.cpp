#include "ParqueaderoLib.h"
#include <ctime>
#include <sstream>
#include <fstream>

Parqueadero::Parqueadero() {
    string nombres[] = {"A1","A2","A3","A4","B1","B2","B3","B4","C1","C2","C3","C4"};
    for (int i = 0; i < 12; i++) {
        Celda c;
        c.nombre = nombres[i];
        c.placa = "LIBRE";
        celdas.push_back(c);
    }
}

static string horaActual() {
    time_t ahora = time(NULL);
    tm* t = localtime(&ahora);
    char buf[20];
    strftime(buf, sizeof(buf), "%H:%M:%S", t);
    return string(buf);
}

string Parqueadero::procesarPlaca(string placa) {
    Evento ev;
    ev.hora = horaActual();
    ev.placa = placa;

    // ¿Ya está en el parqueadero? → SALIDA
    for (auto& c : celdas) {
        if (c.placa == placa) {
            c.placa = "LIBRE";
            ev.celda = c.nombre;
            ev.tipo = "SALIDA";
            eventos.push_back(ev);

            string linea = ev.tipo + "|" + ev.placa + "|" + ev.celda + "|" + ev.hora;

            ofstream f("evento.txt", ios::app);
            f << linea << "\n";
            f.close();

            return linea;
        }
    }

    // Buscar celda libre → ENTRADA
    for (auto& c : celdas) {
        if (c.placa == "LIBRE") {
            c.placa = placa;
            ev.celda = c.nombre;
            ev.tipo = "ENTRADA";
            eventos.push_back(ev);

            string linea = ev.tipo + "|" + ev.placa + "|" + ev.celda + "|" + ev.hora;

            ofstream f("evento.txt", ios::app);
            f << linea << "\n";
            f.close();

            return linea;
        }
    }

    // Parqueadero lleno
    return "LLENO|" + placa + "||" + horaActual();
}

string Parqueadero::obtenerEstado() {
    string resultado = "";
    for (auto& c : celdas) {
        resultado += c.nombre + ":" + c.placa + ";";
    }
    return resultado;
}

string Parqueadero::obtenerUltimoEvento() {
    if (eventos.empty()) return "Sin eventos";
    Evento& ev = eventos.back();
    return ev.tipo + "|" + ev.placa + "|" + ev.celda + "|" + ev.hora;
}

int Parqueadero::obtenerTotal() {
    return celdas.size();
}

int Parqueadero::obtenerLibres() {
    int libres = 0;
    for (auto& c : celdas) {
        if (c.placa == "LIBRE") libres++;
    }
    return libres;
}