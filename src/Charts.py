import matplotlib.pyplot as plt
from src.UserCalculators import UserCalculators

a, b, c = [int(input("podaj liczby")) for i in range(3)]


def chart_folding_percent():
    plt.plot(UserCalculators.folding_percentage(a, b, c))
    plt.ylabel('Zysk')
    return plt.show()


if __name__ == "__main__":
    chart_folding_percent()
