from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def aff_pop() -> None:
    """
    Plots population projections for France and Brazil.

    This function loads population data from a CSV file, filters the data for
    France and Brazil, and then plots the population projections for these
    countries over the years. The plot includes a title, labels for the x and
    y axes, and a legend.

    The population data is expected to be in millions and is read from a file
    located at "../data/population_total.csv". The years are extracted from
    the columns of the data, and the population values are converted to floats
    removing any 'M' characters.

    The y-axis is formatted to display values in millions, and the x-axis
    ticks are set to display every 40 years.

    Returns:
        None
    """
    data = load("../data/population_total.csv")
    countries = data[data["country"].isin(["France", "Brazil"])]

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")

    max_pop = 0
    years = data.columns[1:].astype(int)

    for country in countries["country"]:
        country_data = countries[countries["country"] == country]
        pop = country_data.iloc[0, 1:].replace(
                                'M', '', regex=True).astype(float)
        max_pop = max(max_pop, pop.max())
        plt.plot(years, pop, label=country)

    plt.xticks(years[::40])
    plt.yticks(np.arange(0, max_pop.max(), 20))
    plt.gca().yaxis.set_major_formatter(
                                plt.FuncFormatter(lambda x, pos: f"{x:.0f}M"))

    plt.legend(loc="lower right")
    plt.show()


if __name__ == "__main__":
    aff_pop()
