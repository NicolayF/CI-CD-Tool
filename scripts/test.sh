#!/bin/bash

echo "Ejecutando tests..."
echo "==================="

if make test; then
    echo "Todos los tests pasaron!"
    exit 0
else
    echo "ALERTA: Tests sin pasar!"
    exit 1
fi