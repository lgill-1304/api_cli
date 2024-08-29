import argparse

def main():
    # Configurar el parser de argumentos
    parser = argparse.ArgumentParser(description="Consulta el clima de una ubicación específica")
    parser.add_argument("location", type=str, help="Nombre de la ciudad y país (ejemplo: Asuncion, PY)")
    parser.add_argument("--format", choices=["json", "csv", "text"], default="text", help="Formato de salida: json, csv, text (predeterminado: text)")

    # Parsear los argumentos
    args = parser.parse_args()

    # Lógica para manejar los argumentos
    print(f"Consultando el clima para: {args.location}")
    print(f"Formato de salida seleccionado: {args.format}")

if __name__ == "__main__":
    main()
