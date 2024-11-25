import numpy as np
from scipy import stats

def calculate_statistics(df, column):
    """Вычисляет базовую статистику для указанного столбца."""
    data = df[column]
    return {
        "mean": np.mean(data),
        "median": np.median(data),
        "std_dev": np.std(data),
        "mode": stats.mode(data, nan_policy="omit").mode[0]
    }
