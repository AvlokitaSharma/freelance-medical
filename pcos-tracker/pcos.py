# Step 1: Import Necessary Libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import GradientBoostingRegressor

# Step 2: Create a Synthetic Dataset
np.random.seed(42)  # For reproducibility

data = {
    'Age': np.random.randint(18, 45, 1000),
    'BMI': np.random.uniform(18, 40, 1000),
    'Insulin_Level': np.random.uniform(2, 25, 1000),
    'LH': np.random.uniform(5, 20, 1000),
    'FSH': np.random.uniform(1, 10, 1000),
    'Testosterone': np.random.uniform(0.2, 2.5, 1000),
    'Ultrasound_Follicles': np.random.randint(0, 30, 1000),
    'Period_Irregularity': np.random.randint(0, 15, 1000),
    'PCOS_Risk': np.random.uniform(0, 1, 1000)  # Risk score instead of binary classification
}

df = pd.DataFrame(data)

# Step 3: Preprocess the Data
X = df.drop('PCOS_Risk', axis=1)
y = df['PCOS_Risk']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 4: Train a Gradient Boosting Regressor Model
model = GradientBoostingRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Step 5: Evaluate the Model
y_pred = model.predict(X_test_scaled)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")
