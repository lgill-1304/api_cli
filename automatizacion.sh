#!/bin/bash

# Activar el entorno virtual
echo "Activando el entorno virtual..."
source .venv/Scripts/activate

# Instalar dependencias
echo "Instalando dependencias..."
pip install -r requirements.txt

# Ejecutar la aplicación CLI
echo "Ejecutando la aplicacion CLI..."
python ./cli_weather.py Asuncion --formato texto

# Mensaje final
echo "Ejecución completada con éxito."