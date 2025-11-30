from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Display the projection of life expectancy vs GDP per capita for year 1900.
    """
    # Renamed the file to have a shorter name
    gdp_df = load("../income_per_person_gdp.csv")
    life_df = load("../life_expectancy_years.csv")

    if gdp_df is None or life_df is None:
        return

    year = "1900"

    try:
        # Check if year exists in both datasets
        if year not in gdp_df.columns or year not in life_df.columns:
            print(f"Error: Year {year} not found in datasets")
            return

        gdp_data = gdp_df[['country', year]].copy()
        life_data = life_df[['country', year]].copy()

        # Rename columns
        gdp_data.columns = ['country', 'gdp']
        life_data.columns = ['country', 'life_expectancy']

        merged_data = gdp_data.merge(life_data, on='country')

        # Remove rows with missing values
        merged_data = merged_data.dropna()

        gdp_values = merged_data['gdp'].values
        life_values = merged_data['life_expectancy'].values

        plt.figure(figsize=(10, 6))
        plt.scatter(gdp_values, life_values, alpha=0.6)

        plt.title(f"{year}")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")

        plt.xscale('log')

        # Format x-axis to display values like 300, 1k, 10k
        ax = plt.gca()
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x,
                                                       p: f'{int(x)}'
                                                       if x < 1000 else
                                                       f'{int(x/1000)}k'))

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
