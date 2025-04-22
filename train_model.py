import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load your dataset
df = pd.read_csv('UNSW_NB15_training-set.csv')  # Replace with the correct path

print("Columns in CSV:", df.columns)  # Debugging step

# Replace with the actual column names from your dataset
selected_features = ['ttl', 'length', 'sport', 'dport', 'packet_size']
X = df[selected_features]
y = df['label']  # Assuming your label column is called 'label'

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
model = RandomForestClassifier()
model.fit(X_scaled, y)

# Save model and scaler
joblib.dump(model, 'model_5f.pkl')
joblib.dump(scaler, 'scaler_5f.pkl')
print("Model and scaler saved!")
