#!/bin/bash

echo "Compilando..."
cd app || exit 1

if make build > /dev/null; then
    echo "Compilación sin errores!"
    exit 0
else
    echo "Error al compilar."
    exit 1
fi