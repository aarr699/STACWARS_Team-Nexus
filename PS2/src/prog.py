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
    fig, ax = plt.subplots(ncols=2)

    for d in dfn:
        #Temperature vs Radiation
        ax[0].scatter(
            d["Radiation"],
            d["Temperature"],
            c=d["Normalised_Hours"],
            cmap="plasma",
            vmin=0,
            vmax=24,
            alpha=0.7,
            s=1,
        )

        #Humidity vs Radiation
        ax[1].scatter(
            d["Radiation"],
            d["Humidity"],
            c=d["Normalised_Hours"],
            cmap="viridis",
            vmin=0,
            vmax=24,
            alpha=0.2,
            s=1,
        )

    ax[0].set_xlabel("Radiation")
    ax[0].set_ylabel("Temperature")
    ax[0].set_title("Radiation vs. Temperature Correlation")
    ax[0].grid(True, linestyle="--", alpha=0.5)

    ax[1].set_xlabel("Radiation")
    ax[1].set_ylabel("Humidity")
    ax[1].set_title("Radiation vs. Temperature Correlation")
    ax[1].grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()


a1()
a2()