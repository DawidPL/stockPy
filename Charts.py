import matplotlib.pyplot as plt
from UserCalculators import UserCalculators


def chart_folding_percent():
    plt.plot(UserCalculators.folding_percentage(100.0, 5.0, 3))
    plt.ylabel('Zysk')
    return plt.show()
