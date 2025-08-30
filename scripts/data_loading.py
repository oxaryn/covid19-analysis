import pandas as pd

def load_covid_data(path):
    df = pd.read_csv(path)
    print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    print("Columns:", df.columns.tolist())
    return df
