import argparse
import requests
import sys
import csv

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

 #Función para guardar en CSV
def save_to_csv(data, location):
    filename = f"{location.replace(',', '_').replace(' ', '_')}_weather.csv"
    
    # Extraer la información relevante
    weather_info = [
        ["Location", location],
        ["Temperature (°C)", data['main']['temp']],
        ["Weather", data['weather'][0]['description']],
        ["Humidity (%)", data['main']['humidity']],
        ["Wind Speed (m/s)", data['wind']['speed']]
    ]
    
    # Guardar en un archivo CSV
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(weather_info)
    print(f"Datos del clima guardados en {filename}")

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
    elif args.format == "csv":
        save_to_csv(weather_data, args.location)
    else:
        print("Formato no soportado.")

if __name__ == "__main__":
    main()



