import argparse
import requests
import sys

API_KEY = "2646114b21ec90e3b79c91add1a7b965"  # Reemplaza con tu API key de OpenWeatherMap
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_data(location):
    try:
        # Realizar la solicitud a la API
        response = requests.get(BASE_URL, params={
            "q": location,
            "appid": API_KEY,
            "units": "metric",
            "lang": "es"
        })
        
        # Verificar si la respuesta fue exitosa
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(f"Error en la solicitud: {err}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Consulta el clima de una ubicación específica")
    parser.add_argument("location", type=str, help="Nombre de la ciudad y país (ejemplo: Asuncion, PY)")
    parser.add_argument("--format", choices=["json", "csv", "text"], default="text", help="Formato de salida: json, csv, text (predeterminado: text)")
    args = parser.parse_args()

    weather_data = get_weather_data(args.location)

    if args.format == "json":
        print(weather_data)
    elif args.format == "text":
        print(f"Clima en {args.location}:")
        print(f"Temperatura: {weather_data['main']['temp']}°C")
        print(f"Condiciones: {weather_data['weather'][0]['description']}")
    # Aquí podrías agregar la lógica para CSV o cualquier otro formato
    else:
        print("Formato no soportado.")

if __name__ == "__main__":
    main()


