from utils.api_extraction import APIExtraction
from utils.data_processing import DataProcessor
import os
from utils.date_iteration import iteration
import calendar
import time

# Definir la ruta para guardar el JSON en la carpeta raíz del proyecto
directorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ruta_json = os.path.join(directorio_raiz, 'json')
year = 2024
month = 1

# Crear una instancia de la clase APIHandler
api = APIExtraction(base_url="http://api.tvmaze.com/schedule/web", save_directory=ruta_json)

# Llamar a los métodos de la clase
date_generator = iteration(year,month)
last_day = calendar.monthrange(year, month)[1]

for day in range(0,last_day):
    current_date = next(date_generator)
    datos = api.fetch_data(current_date)
    json_file = 'series_'+str(current_date)+'.json'
    api.save_json(datos, json_file)

# Procesar datos
#processor = DataProcessor(ruta_json + "//" + json_file)
#df = processor.load_data()
#df_cleaned = processor.clean_data(df)
#print(df.head())