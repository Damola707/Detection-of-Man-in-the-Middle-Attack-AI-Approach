# predict.py
import numpy as np
import pickle

# Step 1: Load model and scaler
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Step 2: Input your new data (replace with real values)
new_data = np.array([[value1, value2, value3, value4, value5]])

# Step 3: Scale it
new_data_scaled = scaler.transform(new_data)

# Step 4: Predict
prediction = model.predict(new_data_scaled)
print("Prediction:", prediction)
