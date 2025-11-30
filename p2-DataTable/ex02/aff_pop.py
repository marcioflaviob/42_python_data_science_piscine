from load_csv import load
import matplotlib.pyplot as plt


def convert_population(value):
    """
    Convert population values with suffix (M, K) to numeric.

    Args:
        value: Population value (can be string with M/K suffix or numeric)

    Returns:
        Numeric value
    """
    if isinstance(value, str):
        value = value.strip()
        if value.endswith('M'):
            return float(value[:-1]) * 1_000_000
        elif value.endswith('K'):
            return float(value[:-1]) * 1_000
        else:
            return float(value)
    return float(value)


def main():
    """
    Load population data and compare two countries from 1800 to 2050.
    """
    df = load("../population_total.csv")

    if df is None:
        return

    country1 = "France"
    country2 = "Brazil"

    try:
        country1_data = df[df['country'] == country1]
        country2_data = df[df['country'] == country2]

        if country1_data.empty:
            print(f"Error: Country '{country1}' not found in dataset")
            return

        if country2_data.empty:
            print(f"Error: Country '{country2}' not found in dataset")
            return

        year_columns = [col for col in df.columns if col != 'country']

        filtered_years = [year for year in year_columns
                          if '1800' <= year <= '2050']

        years = [int(year) for year in filtered_years]
        pop1 = [convert_population(country1_data[year].values[0])
                for year in filtered_years]
        pop2 = [convert_population(country2_data[year].values[0])
                for year in filtered_years]

        plt.figure(figsize=(12, 6))
        plt.plot(years, pop1, label=country1, linewidth=2)
        plt.plot(years, pop2, label=country2, linewidth=2)

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")

        ax = plt.gca()
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x,
                                                       p: f'{x/1e6:.0f}M'))

        plt.xlim(1800, 2050)

        plt.legend(loc='lower right')

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
