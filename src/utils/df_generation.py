import pandas as pd
import glob
import json

    
def normalize(path):
    json_files = glob.glob(f"{path}/*.json")

    dataframes = []

    for file in json_files:
        with open(file, "r", encoding = "utf-8") as f:
            json_data = json.load(f)
        
        df = pd.json_normalize(json_data)
        dataframes.append(df)

    df_normalized = pd.concat(dataframes, ignore_index=True)
    return df_normalized