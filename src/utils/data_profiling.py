from data_profiling import ProfileReport
import os

class DataProfiler:
    def __init__(self, save_directory):
        self.save_directory = save_directory
        os.makedirs(self.save_directory, exist_ok=True)

    def generate_report(self, df, filename):
        """
        Genera un reporte de profiling para un DataFrame.
        Args:
            df (pd.DataFrame): DataFrame a analizar.
            filename (str): Nombre del archivo para guardar el reporte.
        """
        print("Generando reporte de profiling...")
        profile = ProfileReport(df, title="Data Profiling Report", explorative=True)
        file_path = os.path.join(self.save_directory, filename)
        profile.to_file(file_path)
        print(f"Reporte guardado en {file_path}")
