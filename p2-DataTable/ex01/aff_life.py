from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Load life expectancy data and display graph for a specific country.
    """
    try:
        df = load("../life_expectancy_years.csv")
        if df is None:
            return
        country_data = df[df['country'] == 'France']

        if country_data.empty:
            print("Error: France not found in dataset")
            return

        years = country_data.columns[1:]  # Skip 'country' column
        life_expectancy = country_data.iloc[0, 1:].values

        years = [int(year) for year in years]

        plt.figure(figsize=(10, 6))
        plt.plot(years, life_expectancy, linewidth=2)

        plt.title("France Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
