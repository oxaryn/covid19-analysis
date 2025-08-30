import pandas as pd

def clean_covid_data(df):
    cols = ["country", "date", "total_cases", "new_cases", 
            "total_deaths", "new_deaths", "total_vaccinations", 
            "people_vaccinated", "people_fully_vaccinated", 
            "population", "continent"]
    
    df_clean = df[cols].copy()
    df_clean.rename(columns={"country": "location"}, inplace=True)
    df_clean["date"] = pd.to_datetime(df_clean["date"])
    
    numeric_cols = ["total_cases","new_cases","total_deaths","new_deaths"]
    df_clean[numeric_cols] = df_clean[numeric_cols].fillna(0)
    
    df_clean = df_clean[df_clean["location"] != "World"]  # Remove global aggregates
    return df_clean
