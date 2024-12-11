def cleaning(df, *column_name):
    df[column_name[0]] = df[column_name[0]].apply(lambda x: "None" if x == "[]" else x)
    df[column_name[1]] = df[column_name[1]].apply(lambda x: "None" if x == "[]" else x)
    df.columns = df.columns.str.replace('.', '_')
    return df