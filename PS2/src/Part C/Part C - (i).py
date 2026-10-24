import pandas as pd

solar_data=pd.read_csv("SolarPrediction.csv")

solar_data = solar_data.astype(str).replace(r' 12:00:00 AM$', '', regex=True)

solar_data['Date and Time'] = pd.to_datetime(solar_data['Data'].astype(str) + ' ' + solar_data['Time'].astype(str), format = "%m/%d/%Y %H:%M:%S", errors = "coerce")

print(solar_data)