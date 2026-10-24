# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt


# df = pd.read_csv("data\\SolarPrediction.csv")
# df["Normalised_Hours"] = df["Time"].apply(
#     lambda x: pd.to_datetime(x, format="%I:%M:%S %p").hour
#     + pd.to_datetime(x, format="%I:%M:%S %p").minute / 60.0
# )
# df=df.sort_values("UNIXTime",ascending=True,ignore_index=True)

# grouped = df.groupby('Data')

# dfn=[i for _, i in grouped]
# # dfn[0]=df[df["Data"]=="9/29/2016 12:00:00 AM"]
# print(dfn[0])
# print(dfn)

    



# fig,ax=plt.subplots()
# for d in dfn:
#     ax.plot(d["Normalised_Hours"],d["Radiation"])
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data\\SolarPrediction.csv")

# 1. FASTER & SAFER: Convert 24-hour strings directly into decimal hours
# pd.to_timedelta turns "23:55:26" into a duration, then we extract the total hours
df["Normalised_Hours"] = (
    pd.to_timedelta(df["Time"]).dt.total_seconds() / 3600.0
)

df = df.sort_values("UNIXTime", ascending=True, ignore_index=True)

# 2. Group by date
grouped = df.groupby("Data")
dfn = [i for _, i in grouped]

# 3. Plot curves with localized sorting
# fig, ax = plt.subplots(figsize=(10, 5))
fig, ax = plt.subplots()

for d in dfn:
    # ax.plot(
    #     d_sorted["Normalised_Hours"],
    #     d_sorted["Radiation"],
    #     alpha=0.3,
    #     linewidth=1,
    # )
    ax.scatter(
        d["Normalised_Hours"],
        d["Radiation"],
        alpha=0.5,
        s=1,
    )
    


# 4. Clean up labels
ax.set_xlabel("Hour of Day (0-24)")
ax.set_ylabel("Radiation")
ax.set_title("Overlapping Daily Solar Radiation Profiles")
ax.grid(True, linestyle="--", alpha=0.5)
ax.set_xlim(0, 24)  # Force X-axis boundaries from midnight to midnight

plt.show()
