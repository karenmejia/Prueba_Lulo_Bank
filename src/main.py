from utils.api_extraction import APIExtraction
from utils.df_generation import normalize
import os
from utils.date_iteration import iteration
import calendar
from utils.data_profiling import data_profiling
from utils.constants import Constants
from utils.data_cleaning import cleaning
from utils.to_parquet import to_parquet
from utils.helper import Helper
import pandas as pd
from utils.calculations import calculations

pd.set_option('display.max_rows', None)

def main():
    # Definicion de rutas
    main_path = Constants.main_path.value
    json_path = os.path.join(main_path, 'json')
    report_path = os.path.join(main_path,'profiling/profiling_report')
    parquet_path = os.path.join(main_path,'data')
    db_path = os.path.join(main_path,'db')

    year = Constants.year.value
    month = Constants.month.value

    # Creacion de una instancia de la clase APIExtraction
    api = APIExtraction(base_url="http://api.tvmaze.com/schedule/web", save_directory=json_path)

    # Creacion del generador
    date_generator = iteration(year,month)
    last_day = calendar.monthrange(year, month)[1]

    for day in range(0,last_day):
        current_date = next(date_generator)
        datos = api.fetch_data(current_date)
        json_file = 'series_'+str(current_date)+'.json'
        api.save_json(datos, json_file)

    df = normalize(json_path)
    data_profiling(df,report_path)
    cleaned_df = cleaning(df, "_embedded.show.schedule.days", "_embedded.show.genres")
    df_parquet = to_parquet(cleaned_df, parquet_path)
    df_parquet = pd.read_parquet(parquet_path)
    df_parquet = df_parquet.astype("object")
    df_parquet = df_parquet.where(pd.notnull(df_parquet), "None")

    Helper = Helper(df_parquet, db_path)
    Helper.create_table(Constants.table_name.value, Constants.fields.value)
    Helper.data_insert(Constants.table_name.value, Constants.fields_insert.value)

    avg_runtime, genre_counts, unique_domains = calculations(df_parquet)
    print("INFORMACION SOBRE SHOWS DEL MES:\n")
    print("Runtime promedio (averageRuntime):" + str(avg_runtime))
    print('\n')
    print("Conteo de shows de tv por género:\n", genre_counts)
    print('\n')
    print("Listado dominios únicos (web) del sitio oficial de los shows:\n", unique_domains)

main()