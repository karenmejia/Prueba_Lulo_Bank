import os
import requests
import json

class APIExtraction:
    def __init__(self, base_url, save_directory):
        self.base_url = base_url
        self.save_directory = save_directory
        # Crear el directorio si no existe
        os.makedirs(self.save_directory, exist_ok=True)

    def fetch_data(self, date):
        url = f"{self.base_url}?date={str(date)}"
        response = requests.get(url)
        
        if response.status_code == 200:
            print("Datos obtenidos correctamente.")
            return response.json()
        else:
            print(f"Error al obtener los datos: {response.status_code}")
            return None

    def save_json(self, data, filename):
        if data:
            file_path = os.path.join(self.save_directory, filename)
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Datos guardados en {file_path}")
        else:
            print("No hay datos para guardar.")
