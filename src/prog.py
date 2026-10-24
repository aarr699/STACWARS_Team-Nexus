import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data\\SolarPrediction.csv")

# pd.to_timedelta turns "23:55:26" into a duration, then we extract the total hours
df["Normalised_Hours"] = (
    pd.to_timedelta(df["Time"]).dt.total_seconds() / 3600.0
)

df = df.sort_values("UNIXTime", ascending=True, ignore_index=True)

#Group by date
grouped = df.groupby("Data")
dfn = [i for _, i in grouped]


def a1():
    fig, ax = plt.subplots()

    for d in dfn:
        ax.scatter(
            d["Normalised_Hours"],
            d["Radiation"],
            alpha=0.5,
            s=1,
        )
        
    ax.set_xlabel("Hour of Day (0-24)")
    ax.set_ylabel("Radiation")
    ax.set_title("Overlapping Daily Solar Radiation Profiles")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.set_xlim(0, 24)  # Force X-axis boundaries from midnight to midnight

    plt.show()

def a2():
    fig, ax = plt.subplots()
    


a1()
a2()