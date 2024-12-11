import pandas as pd

def cleaning(df, *column_name):
    df[column_name[0]] = df[column_name[0]].apply(lambda x: str(x))
    df[column_name[1]] = df[column_name[1]].apply(lambda x: str(x))
    df = df.applymap(lambda x: x.replace("'", "") if isinstance(x, str) else x)
    df.columns = df.columns.str.replace('.', '_')
    return df