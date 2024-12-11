import pandas as pd

def calculations(df):
    df['_embedded_show_runtime'] = df['_embedded_show_runtime'].replace('None', '0')
    df['_embedded_show_runtime'] = df['_embedded_show_runtime'].astype(float)
    avg_runtime = df['_embedded_show_runtime'].mean()
    genre_counts = df['_embedded_show_genres'].explode().value_counts()
    unique_domains = df['_embedded_show_webChannel_officialSite'].dropna().unique()
    return avg_runtime, genre_counts, unique_domains