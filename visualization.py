import matplotlib.pyplot as plt

def plot_histogram(df, column):
    """Рисует гистограмму для указанного столбца."""
    plt.hist(df[column], bins=10, alpha=0.7, color='blue')
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()
