import pandas as pd
import os

class DataProcessor:
    def __init__(self, json_file):
        self.json_file = json_file
    
    def load_data(self):
        # Cargar el archivo JSON en un DataFrame
        df = pd.read_json(self.json_file)
        return df
    
    def clean_data(self, df):
        # Ejemplo de limpieza básica: eliminar duplicados y valores nulos
        df.drop_duplicates(inplace=True)
        df.dropna(subset=['runtime'], inplace=True)
        return df
