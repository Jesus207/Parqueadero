%module ParqueaderoLib

%{
#include "ParqueaderoLib.h"
%}

extern void guardarEvento(const char* evento);
extern const char* obtenerEvento();