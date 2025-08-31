import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------
# Settings
# ------------------------------
PLOT_DIR = "plots"
os.makedirs(PLOT_DIR, exist_ok=True)

# CSV from Dropbox (direct download)
url = "https://www.dropbox.com/scl/fi/i8glpy38fz71rodxswtda/owid-covid-data.csv?rlkey=rzm4s0r8pdtj1yec0fww6dly7&dl=1"

print("Loading dataset...")
df = pd.read_csv(url)
print("\n✅ Dataset loaded successfully!")
print(f"Shape: {df.shape}")
print(f"Columns (first 20): {df.columns[:20].tolist()}")

# ------------------------------
# Plotting functions
# ------------------------------
def plot_country(country, column, ylabel, title):
    data = df[df["country"] == country]
    plt.figure(figsize=(10,5))
    plt.plot(pd.to_datetime(data["date"]), data[column], marker='o', linestyle='-')
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plot_path = os.path.join(PLOT_DIR, f"{title.replace(' ','_')}.png")
    plt.savefig(plot_path)
    print(f"📌 Saved plot: {plot_path}")
    plt.close()

def plot_compare(c1, c2, column, ylabel, title):
    data1 = df[df["country"] == c1]
    data2 = df[df["country"] == c2]
    plt.figure(figsize=(10,5))
    plt.plot(pd.to_datetime(data1["date"]), data1[column], label=c1)
    plt.plot(pd.to_datetime(data2["date"]), data2[column], label=c2)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel(ylabel)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plot_path = os.path.join(PLOT_DIR, f"{title.replace(' ','_')}.png")
    plt.savefig(plot_path)
    print(f"📌 Saved plot: {plot_path}")
    plt.close()

def vaccination_trend(region, column="total_vaccinations", ylabel="Total vaccinations"):
    if region.lower() == "usa":
        data = df[df["country"] == "United States"]
        x = pd.to_datetime(data["date"])
        y = data[column]
    else:
        if "continent" in df.columns:
            europe_countries = df[df["continent"]=="Europe"]["country"].unique()
            data = df[df["country"].isin(europe_countries)].groupby("date")[column].sum()
            x = pd.to_datetime(data.index)
            y = data.values
        else:
            print("No continent information found.")
            return
    
    plt.figure(figsize=(10,5))
    plt.plot(x, y)
    plt.title(f"COVID-19 Vaccination Trend in {region}")
    plt.xlabel("Date")
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plot_path = os.path.join(PLOT_DIR, f"Vaccination_Trend_{region}.png")
    plt.savefig(plot_path)
    print(f"📌 Saved plot: {plot_path}")
    plt.close()

def global_plot(column, ylabel, title):
    global_data = df.groupby("date")[column].sum()
    x = pd.to_datetime(global_data.index)
    y = global_data.values
    
    plt.figure(figsize=(10,5))
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plot_path = os.path.join(PLOT_DIR, f"{title.replace(' ','_')}.png")
    plt.savefig(plot_path)
    print(f"📌 Saved plot: {plot_path}")
    plt.close()

# ------------------------------
# Auto-generate all plots
# ------------------------------
def generate_all_plots():
    countries = ["Greece", "United States", "Italy", "Spain", "Germany"]
    
    # Daily & total cases/deaths per country
    for country in countries:
        plot_country(country, "new_cases", "Cases", f"{country} - Daily cases")
        plot_country(country, "total_cases", "Cases", f"{country} - Total cases")
        plot_country(country, "new_deaths", "Deaths", f"{country} - Daily deaths")
        plot_country(country, "total_deaths", "Deaths", f"{country} - Total deaths")
        plot_country(country, "total_vaccinations", "Vaccinations", f"{country} - Total vaccinations")
    
    # Compare two countries
    plot_compare("Greece", "Italy", "new_cases", "Cases", "Greece vs Italy - Daily Cases")
    
    # Vaccination trends
    vaccination_trend("USA")
    vaccination_trend("Europe")
    
    # Global plots
    global_plot("new_cases", "Cases", "Global Daily Cases")
    global_plot("total_cases", "Cases", "Global Total Cases")
    global_plot("new_deaths", "Deaths", "Global Daily Deaths")
    global_plot("total_deaths", "Deaths", "Global Total Deaths")

# ------------------------------
# Run auto-generate
# ------------------------------
if __name__ == "__main__":
    generate_all_plots()
    print("\n✅ All plots generated and saved in 'plots' folder.")
