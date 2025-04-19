# train_model.py

# Detection of Man-in-the-Middle Attack: AI Approach
# This script handles data preprocessing and model training using AI for intrusion detection.
# It is based on analyzing network traffic data to detect MITM techniques such as ARP spoofing, DNS hijacking, etc.
# Background concepts: data preprocessing (scaling, feature selection), classification using Decision Trees.


import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, ConfusionMatrixDisplay
)
import joblib
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Load dataset
# Load the UNSW-NB15 dataset which contains labeled traffic (normal + attack).
# Used for supervised learning to train the AI intrusion detection model.

df = pd.read_csv("UNSW_NB15_training-set.csv")

# Drop non-numeric or irrelevant columns
# Data Preprocessing:
# - Feature selection: choosing relevant columns for training
# - StandardScaler: normalizing data for better AI performance

df = df.select_dtypes(include=['number'])

# Separate features and labels
X = df.drop('label', axis=1)
y = df['label']

# Save column names for use in live detection
feature_names = X.columns.tolist()
with open("feature_config.py", "w") as f:
    f.write(f"FEATURE_NAMES = {feature_names}\n")

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the model
# Model Training:
# - Using DecisionTreeClassifier for classification (can detect both known and new attack patterns)
# - AI is suitable for real-time detection due to low latency and good accuracy

clf = RandomForestClassifier()
clf.fit(X_train_scaled, y_train)

# Save model and scaler
# Save the trained model and the scaler
# Enables real-time detection by reusing the same training config during testing

joblib.dump(clf, 'random_forest_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

# Make predictions and calculate metrics
y_pred = clf.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Log folder
os.makedirs("logs", exist_ok=True)

# Save training logs
with open("logs/training_logs.txt", "a") as log:
    log.write(f"\nTraining completed: {datetime.now()}\n")
    log.write(f"Accuracy: {accuracy:.4f}\n")
    log.write(f"Recall: {recall:.4f}\n")
    log.write(f"Precision: {precision:.4f}\n")
    log.write(f"F1 Score: {f1:.4f}\n")

# Plot and save confusion matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap='Blues', values_format='d')
plt.title("Confusion Matrix")
os.makedirs("static", exist_ok=True)
plt.savefig("static/confusion_matrix.png")
plt.close()

print(" Model training complete and saved.")
print(f" Accuracy: {accuracy:.4f} | Precision: {precision:.4f} | Recall: {recall:.4f} | F1 Score: {f1:.4f}")
print(" Confusion matrix saved to static/confusion_matrix.png")

