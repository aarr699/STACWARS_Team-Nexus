from sklearn.ensemble import RandomForestRegressor
import matplotlib
import matplotlib.pyplot as graph 
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

solar_data=pd.read_csv("data\\SolarPrediction.csv")

temp_time = pd.to_datetime(solar_data['Time'], format='%H:%M:%S', errors='coerce')

solar_data['Hour'] = temp_time.dt.hour
solar_data['Minute'] = temp_time.dt.minute
solar_data['Total_Minutes'] = (temp_time.dt.hour * 60) + temp_time.dt.minute

X = solar_data[['Temperature', 'Humidity', 'Hour', 'Total_Minutes', 'Pressure', 'Speed', 'WindDirection(Degrees)' ]] 
y = solar_data['Radiation']  

X = X.dropna()
y = y[X.index]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


solar_data_model = RandomForestRegressor(n_estimators=100, random_state=42)
solar_data_model.fit(X_train, y_train)

y_pred_rf = solar_data_model.predict(X_test)
print(f"Root Mean Square Error (RMSE): {np.sqrt(mean_squared_error(y_test, y_pred_rf)):.4f}")
print(f"R² Score (fraction of values it predicts approximately correctly) : {r2_score(y_test, y_pred_rf):.4f}")


solar_compare = pd.DataFrame({'Radiation': y_test.values, 'RadiationPredicted': y_pred_rf})

solar_compare['Error'] = solar_compare['Radiation'] - solar_compare['RadiationPredicted']
solar_compare.to_csv('RegressorPredictions.csv', mode='a', index=False, header=False)

solar_predict = pd.read_csv("RegressorPredictions.csv", header = None)

graph.figure(figsize=(10, 6))

graph.plot(solar_predict[0], label='Actual Radiation', color='blue', linewidth=1.5)
graph.plot(solar_predict[1], label='Predicted Radiation', color='red', linewidth=1.5)
graph.plot(solar_predict[2], label='Error Margin', color='green', linewidth=1.5,alpha=0.5)

graph.title('Plot Comparing the Regression Model Predictions to the Actual Radiation', fontsize=14, fontweight='bold')
graph.xlabel('', fontsize=12)
graph.ylabel('Radiation', fontsize=12)
graph.grid(True, linestyle='--', alpha=0.6)
graph.legend(loc='upper right')

graph.show()

