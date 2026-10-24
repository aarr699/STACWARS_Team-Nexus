import pandas as pd 

solar_data=pd.read_csv("SolarPrediction.csv")

solar_data['Date and Time'] = pd.to_datetime(solar_data['Data'].astype(str) + ' ' + solar_data['Time'].astype(str))

daily_report = solar_data.groupby(solar_data['Date and Time'].dt.date)['Radiation'].agg(['max', 'mean'])

daily_report.columns = ("Maximum Radiation", "Average Radiation")

print(daily_report)