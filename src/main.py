from utils.api_extraction import APIExtraction
from utils.df_generation import normalize
import os
from utils.date_iteration import iteration
import calendar
from utils.data_profiling import data_profiling
from utils.constants import constants

# Definir la ruta para guardar el JSON en la carpeta raíz del proyecto
main_path = constants.main_path.value
json_path = os.path.join(main_path, 'json')
report_path = os.path.join(main_path,'profiling/profiling_report')

year = constants.year.value
month = constants.month.value

# Crear una instancia de la clase APIExtraction
api = APIExtraction(base_url="http://api.tvmaze.com/schedule/web", save_directory=json_path)

# Se crea el generador
date_generator = iteration(year,month)
last_day = calendar.monthrange(year, month)[1]

for day in range(0,last_day):
    current_date = next(date_generator)
    datos = api.fetch_data(current_date)
    json_file = 'series_'+str(current_date)+'.json'
    api.save_json(datos, json_file)

df = normalize(json_path)
data_profiling(df,report_path)