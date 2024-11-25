import pandas as pd

def load_csv(file_path):
    """Загружает данные из CSV-файла."""
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Ошибка загрузки CSV: {e}")
        return None
