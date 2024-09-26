from load_csv import load
import matplotlib.pyplot as plt


def projection_life() -> None:
    """Plots a scatter plot of GDP vs Life Expectancy for the year 1900.

    This function loads GDP and life expectancy data from CSV files, extracts
    the data for the year 1900, and creates a scatter plot with GDP on the
    x-axis (logarithmic scale) and life expectancy on the y-axis. The plot is
    customized with specific x-axis limits and tick labels.

    The data files are expected to be located at:
    - "../data/income_per_person_gdppercapita_ppp_inflation_adj.csv"
    - "../data/life_expectancy_years.csv"

    The plot is displayed using matplotlib's `show` function.

    Returns:
        None
    """
    gdp = load("../data/income_per_person_gdppercapita_ppp_inflation_adj.csv")
    expectancy = load("../data/life_expectancy_years.csv")

    year = expectancy["1900"]
    gdp_data = gdp["1900"]

    fig, ax = plt.subplots()

    ax.scatter(gdp_data, year)
    ax.set_xscale("log")

    ax.set_title("1900")
    ax.set_xlabel("Gross domestic product")
    ax.set_ylabel("Life expectancy")

    # Customize x-axis
    ax.set_xlim(300, 10000)
    ax.set_xticks([300, 1000, 10000])
    ax.set_xticklabels(['300', '1k', '10k'])

    plt.show()


if __name__ == "__main__":
    projection_life()
