import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd

def save_plot(fig, filename, plots_dir="plots"):
    os.makedirs(plots_dir, exist_ok=True)
    fig.savefig(os.path.join(plots_dir, filename))
    plt.close(fig)

def plot_global_cases(df_clean, plots_dir="plots"):
    global_cases = df_clean.groupby("date")["new_cases"].sum(min_count=1).reset_index()
    fig, ax = plt.subplots(figsize=(12,6))
    sns.lineplot(data=global_cases, x="date", y="new_cases", color="blue", ax=ax)
    ax.set_title("Global Daily COVID-19 Cases")
    ax.set_xlabel("Date")
    ax.set_ylabel("New Cases")
    ax.grid(True, linestyle="--", alpha=0.7)
    save_plot(fig, "global_cases.png", plots_dir)

def plot_top10_cases(df_clean, plots_dir="plots"):
    latest_data = df_clean.sort_values("date").groupby("location").tail(1)
    top10 = latest_data.nlargest(10, "total_cases")[["location", "total_cases"]]
    fig, ax = plt.subplots(figsize=(10,6))
    sns.barplot(data=top10, x="location", y="total_cases", palette="Reds_r", ax=ax)
    ax.set_title("Top 10 Countries by Total COVID-19 Cases (latest)")
    ax.set_ylabel("Total Cases")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
    plt.tight_layout()
    save_plot(fig, "top_countries_cases.png", plots_dir)

def plot_top10_deaths(df_clean, plots_dir="plots"):
    latest_data = df_clean.sort_values("date").groupby("location").tail(1)
    top10 = latest_data.nlargest(10, "total_deaths")[["location", "total_deaths"]]
    fig, ax = plt.subplots(figsize=(10,6))
    sns.barplot(data=top10, x="location", y="total_deaths", palette="Greys_r", ax=ax)
    ax.set_title("Top 10 Countries by Total COVID-19 Deaths (latest)")
    ax.set_ylabel("Total Deaths")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
    plt.tight_layout()
    save_plot(fig, "top_countries_deaths.png", plots_dir)

def plot_vaccination_usa(df_clean, plots_dir="plots"):
    usa = df_clean[df_clean["location"] == "United States"].sort_values("date")
    usa[["people_vaccinated","people_fully_vaccinated"]] = \
        usa[["people_vaccinated","people_fully_vaccinated"]].fillna(method="ffill").fillna(0)
    fig, ax = plt.subplots(figsize=(12,6))
    sns.lineplot(data=usa, x="date", y="people_fully_vaccinated", label="Fully Vaccinated", ax=ax)
    sns.lineplot(data=usa, x="date", y="people_vaccinated", label="At least 1 dose", ax=ax)
    ax.set_title("COVID-19 Vaccination Trend in USA")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of People Vaccinated")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    save_plot(fig, "vaccination_trend_usa.png", plots_dir)

def plot_vaccination_europe(df_clean, plots_dir="plots"):
    europe = df_clean[df_clean["continent"] == "Europe"].sort_values("date")
    europe_daily = europe.groupby("date")[["people_vaccinated","people_fully_vaccinated"]].sum(min_count=1).reset_index()
    europe_daily[["people_vaccinated","people_fully_vaccinated"]] = \
        europe_daily[["people_vaccinated","people_fully_vaccinated"]].fillna(method="ffill").fillna(0)
    fig, ax = plt.subplots(figsize=(12,6))
    sns.lineplot(data=europe_daily, x="date", y="people_fully_vaccinated", label="Fully Vaccinated", ax=ax)
    sns.lineplot(data=europe_daily, x="date", y="people_vaccinated", label="At least 1 dose", ax=ax)
    ax.set_title("COVID-19 Vaccination Trend in Europe")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of People Vaccinated")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    save_plot(fig, "vaccination_trend_europe.png", plots_dir)
