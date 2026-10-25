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
#groupby sorts the date strings alphabetically ("10/1/2016" before "9/1/2016"),
#so dfn is NOT in chronological order. Re-sort by each day's first timestamp.
dfn.sort(key=lambda d: d["UNIXTime"].iloc[0])
n_days = len(dfn)

#Colourbar end labels - edit these


def a1():
    CBAR_START = "9/1/2016"
    CBAR_END = "12/31/2016"

    fig, ax = plt.subplots()

    for i, d in enumerate(dfn):
        sc = ax.scatter(
            d["Normalised_Hours"],
            d["Radiation"],
            c=np.full(len(d), i),
            cmap="turbo",
            vmin=0,
            vmax=n_days - 1,
            alpha=0.5,
            s=1,
        )

    cbar = fig.colorbar(sc, ax=ax, ticks=[0, n_days - 1])
    cbar.solids.set_alpha(1)
    cbar.set_ticklabels([CBAR_START, CBAR_END])
    ax.set_xlabel("Hour of Day (0-24)")
    ax.set_ylabel("Radiation (W/m²)")
    ax.set_title("Overlapping Daily Solar Radiation Profiles")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.set_xlim(0, 24)  #Force X-axis boundaries from midnight to midnight

    plt.show()


def a2():
    CBAR_START = "9/1/2016"
    CBAR_END = "12/31/2016"

    fig, ax = plt.subplots(ncols=2, figsize=(12, 5), layout="constrained")

    for i, d in enumerate(dfn):
        #Temperature vs Radiation
        sc0 = ax[0].scatter(
            d["Radiation"],
            d["Temperature"],
            c=np.full(len(d), i),
            cmap="viridis",
            vmin=0,
            vmax=n_days - 1,
            alpha=0.7,
            s=1,
        )

        #Humidity vs Radiation
        sc1 = ax[1].scatter(
            d["Radiation"],
            d["Humidity"],
            c=np.full(len(d), i),
            cmap="turbo",
            vmin=0,
            vmax=n_days - 1,
            alpha=0.7,
            s=1,
        )

    # One colourbar per panel: the panels use different colourmaps
    for s, a in zip((sc0, sc1), ax):
        cbar = fig.colorbar(s, ax=a,label="Date", ticks=[0, n_days - 1])
        cbar.solids.set_alpha(1)
        cbar.set_ticklabels([CBAR_START, CBAR_END])

    ax[0].set_xlabel("Radiation (W/m²)")
    ax[0].set_ylabel("Temperature (°F)")
    ax[0].set_title("Radiation vs. Temperature Correlation")
    ax[0].grid(True, linestyle="--", alpha=0.5)

    ax[1].set_xlabel("Radiation (W/m²)")
    ax[1].set_ylabel("Humidity (%)")
    ax[1].set_title("Radiation vs. Humidity Correlation")
    ax[1].grid(True, linestyle="--", alpha=0.5)

    plt.show()

def a3():
    #Pressure minus that day's mean, against hour of day.
    CBAR_START = "9/1/2016"
    CBAR_END = "12/31/2016"

    fig, ax = plt.subplots()
    hours, devs = [], []
    for i, d in enumerate(dfn):
        dev = d["Pressure"] - d["Pressure"].mean()
        hours.append(d["Normalised_Hours"])
        devs.append(dev)
        sc = ax.scatter(
            d["Normalised_Hours"],
            dev,
            c=np.full(len(d), i),
            cmap="turbo",
            vmin=0,
            vmax=n_days - 1,
            alpha=0.3,
            s=2,
        )

    #Mean deviation per hour across all days
    mean_dev = pd.concat(devs).groupby(np.floor(pd.concat(hours))).mean()
    ax.plot(mean_dev.index + 0.5, mean_dev.values, color="k", lw=2.5, label="Mean over all days")

    cbar = fig.colorbar(sc, ax=ax,label="Date", ticks=[0, n_days - 1])
    cbar.solids.set_alpha(1)
    cbar.set_ticklabels([CBAR_START, CBAR_END])
    ax.set_xlabel("Hour of Day (0-24)")
    ax.set_ylabel("Pressure deviation from daily mean (in Hg)")
    ax.set_title("Daily Pressure Cycle (Semidiurnal Tide)")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.set_xlim(0, 24)
    ax.legend()

    plt.show()

print("Plot")
print("1.\tRadiation vs Time")
print("2.\tRadiation vs Temperature and Radiation vs Humidity")
print("3.\tPressure deviation vs Time")

ch=int(input(": "))

match(ch):
    case 1:
        a1()
    case 2:
        a2()
    case 3:
        a3()
    case _:
        print("Not a valid choice")