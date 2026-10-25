import pandas as pd 

solar_data=pd.read_csv("data\\SolarPrediction.csv")

solar_data['Date and Time'] = pd.to_datetime(solar_data['Data'].astype(str) + ' ' + solar_data['Time'].astype(str), format = "%m/%d/%Y %H:%M:%S", errors = "coerce")

daily_report = solar_data.groupby(solar_data['Date and Time'].dt.date)['Radiation'].agg(['max', 'mean'])

maxindex = solar_data['Radiation'].idxmax()

solar_data = solar_data.astype(str).replace(r' 12:00:00 AM$', '', regex=True)

maxdate = solar_data.loc[maxindex, 'Data']
maxrad = solar_data.loc[maxindex, 'Radiation']

print(f"Maximum radiation level of {maxrad} units occurred on {maxdate}")