from load_csv import load
import matplotlib.pyplot as plt


def fr_life_expectancy() -> None:
    """
    Plots the life expectancy projections for France from the loaded CSV data.

    This function performs the following steps:
    1. Loads the life expectancy data from a CSV file.
    2. Filters the data for France.
    3. Sets the x-axis to show intervals of 40 years.
    4. Plots the life expectancy projections for France.

    Returns:
        None
    """
    data = load("../data/life_expectancy_years.csv")
    fr = data.loc[data["country"] == "France"]

    print(fr)

    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")

    years = data.columns[1:].astype(int)

    # A less elegant solution:
    # x_ticks = [y for y in range(0, len(years), 40)]
    x_ticks = years[::40]
    plt.xticks(x_ticks)

    plt.plot(years, fr.values[0][1:])
    plt.show()


if __name__ == "__main__":
    fr_life_expectancy()
