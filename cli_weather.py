import argparse
import requests
import sys
import csv

API_KEY = (
    "2646114b21ec90e3b79c91add1a7b965"  # Reemplaza con tu API key de OpenWeatherMap
)
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


# Función para obtener datos del clima
def obtener_datos_clima(ubicacion):
    try:
        # Realizar la solicitud a la API
        respuesta = requests.get(
            BASE_URL,
            params={
                "q": ubicacion,
                "appid": API_KEY,
                "units": "metric",  # Unidades métricas (Celsius)
                "lang": "es",  # Idioma español
            },
        )

        if respuesta.status_code == 404:
            print(f"Ubicación '{ubicacion}' no encontrada.")
            sys.exit(1)

        # Verificar si la respuesta fue exitosa
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.HTTPError as error_http:
        print(f"Error HTTP: {error_http}")
        sys.exit(1)
    except requests.exceptions.RequestException as error:
        print(f"Error en la solicitud: {error}")
        sys.exit(1)


# Función para guardar datos en CSV
def guardar_como_csv(datos, ubicacion):
    nombre_archivo = f"{ubicacion.replace(',', '_').replace(' ', '_')}_clima.csv"

    # Extraer la información relevante del clima
    clima_info = [
        ["Ubicación", ubicacion],
        ["Temperatura (°C)", datos["main"]["temp"]],
        ["Condición", datos["weather"][0]["description"]],
        ["Humedad (%)", datos["main"]["humidity"]],
        ["Velocidad del Viento (m/s)", datos["wind"]["speed"]],
    ]

    # Guardar en un archivo CSV
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(clima_info)

    print(f"Datos del clima guardados en el archivo: {nombre_archivo}")


# Función principal del programa
def main():
    parser = argparse.ArgumentParser(
        description="Consulta el clima de una ubicación específica"
    )
    parser.add_argument(
        "ubicacion", type=str, help="Nombre de la ciudad y país (ejemplo: Asuncion, PY)"
    )
    parser.add_argument(
        "--formato",
        choices=["json", "csv", "texto"],
        default="texto",
        help="Formato de salida: json, csv, texto (predeterminado: texto)",
    )

    # Analizar los argumentos
    args = parser.parse_args()

    # Obtener los datos del clima
    datos_clima = obtener_datos_clima(args.ubicacion)

    # Mostrar datos según el formato especificado
    if args.formato == "json":
        datos_filtrados = {
            "ubicacion": args.ubicacion,
            "temperatura": datos_clima["main"]["temp"],
            "condicion": datos_clima["weather"][0]["description"],
            "humedad": datos_clima["main"]["humidity"],
            "velocidad_viento": datos_clima["wind"]["speed"],
        }
        print(datos_filtrados)

    elif args.formato == "texto":
        print(f"Clima en {args.ubicacion}:")
        print(f"Temperatura: {datos_clima['main']['temp']}°C")
        print(f"Condiciones: {datos_clima['weather'][0]['description']}")
        print(f"Humedad: {datos_clima['main']['humidity']}%")
        print(f"Velocidad del viento: {datos_clima['wind']['speed']} m/s")
    elif args.formato == "csv":
        guardar_como_csv(datos_clima, args.ubicacion)
    else:
        print("Formato no soportado.")


# Punto de entrada de la aplicación
if __name__ == "__main__":
    main()
