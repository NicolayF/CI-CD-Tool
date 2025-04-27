#!/bin/bash

echo "Compilando..."
if make build; then
    echo "Compilación sin errores!"
    exit 0
else
    echo "Error al compilar."
    exit 1
fi