from src.data_loader import load_csv
from src.data_analysis import calculate_statistics
from src.visualization import plot_histogram

def main():
    # Загружаем данные
    file_path = "data/sample_data.csv"
    data = load_csv(file_path)
    if data is None:
        return

    # Анализируем данные
    column = "Sales"
    stats = calculate_statistics(data, column)
    print(f"Статистика для столбца '{column}': {stats}")

    # Визуализируем данные
    plot_histogram(data, column)

if __name__ == "__main__":
    main()
