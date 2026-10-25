import pandas as pd

solar_data=pd.read_csv("data\\SolarPrediction.csv")

solar_data['Date and Time'] = pd.to_datetime(solar_data['Data'].astype(str) + ' ' + solar_data['Time'].astype(str), format = "%m/%d/%Y %H:%M:%S", errors = "coerce")

daily_report = solar_data.groupby(solar_data['Date and Time'].dt.date)['Radiation'].agg(['max', 'mean'])

maxindex = solar_data['Radiation'].idxmax()

solar_data = solar_data.astype(str).replace(r' 12:00:00 AM$', '', regex=True)

maxdate = solar_data.loc[maxindex, 'Data']
maxrad = solar_data.loc[maxindex, 'Radiation']
maxtime = solar_data.loc[maxindex, 'Time']
sunrise = solar_data.loc[maxindex, 'TimeSunRise']
sunset = solar_data.loc[maxindex, 'TimeSunSet']

print(f"Maximum radiation level of {maxrad} units occurred on {maxdate} at {maxtime} hrs.")
print(f"Sunrise occured on {maxdate} at {sunrise} hrs.")
print(f"Sunset occured on {maxdate} at {sunset} hrs.")

solar_data['Time'] = pd.to_datetime(solar_data['Time'], format='%H:%M:%S')
solar_data['TimeSunRise'] = pd.to_datetime(solar_data['TimeSunRise'], format='%H:%M:%S')

diff = solar_data.loc[maxindex, 'Time'] - solar_data.loc[maxindex, 'TimeSunRise']

print(f"Maximum radiation occured {diff} hrs after sunrise.")