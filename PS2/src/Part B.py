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
