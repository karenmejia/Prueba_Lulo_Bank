import ydata_profiling
import os

def data_profiling(df, path):
    profile = ydata_profiling.ProfileReport(df, title="Profiling del DataFrame", explorative=True) 
    profile.to_file(path)
