import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/AER/CollegeDistance.csv')
data = data.drop(columns=['rownames'])
data = data.dropna()

print(data.info())
print(data.describe())

data = pd.get_dummies(data, drop_first=True)

x = data.drop('score', axis=1)
y = data['score']

x_scaled = StandardScaler().fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

prediction = model.predict(x_test)

mae = mean_absolute_error(y_test, prediction)
mse = mean_squared_error(y_test, prediction)
r2 = r2_score(y_test, prediction)

print(f"MAE: {mae}")
print(f"MSE: {mse}")
print(f"R²: {r2}")

os.makedirs("Results", exist_ok=True)

plt.scatter(y_test, prediction)
plt.xlabel('Real values')
plt.ylabel('Expected values')
plt.title('Prediction results')
plt.savefig('Results/prediction_results.png')

with open('Results/results.md', 'w', encoding='utf-8') as file:
    file.write(f"""### Results:
- MAE: {mae}
- MSE: {mse}
- R²: {r2}
""")
