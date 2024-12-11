def to_parquet(df, path):
    return df.to_parquet(path + "/january_series.parquet", engine="pyarrow", compression="snappy")
    