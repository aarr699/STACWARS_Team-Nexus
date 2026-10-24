import pandas as pd

solar_data = pd.read_csv("SolarPrediction.csv")

solar_data['Date and Time'] = pd.to_datetime(solar_data['Data'].astype(str) + ' ' + solar_data['Time'].astype(str))

solar_data['Date and Time'] = pd.to_datetime(solar_data['Date and Time'], format='mixed', errors='coerce')

maxavgfive= (solar_data.groupby(solar_data['Date and Time'].dt.date)['Radiation'].mean().nlargest(5).reset_index())

maxavgfive.columns = ['Date', 'Average_Radiation']
maxavgfive.index+=1

print("The five days with highest average radiation is: ")
print(maxavgfive)