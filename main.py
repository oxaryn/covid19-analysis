from scripts.data_loading import load_covid_data
from scripts.data_cleaning import clean_covid_data
from scripts.plots import (
    plot_global_cases,
    plot_top10_cases,
    plot_top10_deaths,
    plot_vaccination_usa,
    plot_vaccination_europe
)

DATA_PATH = "data/owid-covid-data.csv"

df = load_covid_data(DATA_PATH)
df_clean = clean_covid_data(df)

plot_global_cases(df_clean)
plot_top10_cases(df_clean)
plot_top10_deaths(df_clean)
plot_vaccination_usa(df_clean)
plot_vaccination_europe(df_clean)

print("All plots generated and saved in 'plots/' folder.")
