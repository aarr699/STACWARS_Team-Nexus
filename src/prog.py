import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data\\SolarPrediction.csv")
df=df.sort_values("UNIXTime",ascending=True,ignore_index=True)

fig,ax=plt.subplots()
ax.plot(df["UNIXTime"],df["Radiation"])
plt.show()
print(df)
