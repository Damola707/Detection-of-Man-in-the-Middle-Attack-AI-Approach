import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load training and testing datasets
train_path = 'C:/Users/Ephraim/Documents/mitm-local-repo/UNSW_NB15_training-set.csv'
test_path = 'C:/Users/Ephraim/Documents/mitm-local-repo/UNSW_NB15_testing-set.csv'

df_train = pd.read_csv(train_path)
df_test = pd.read_csv(test_path)

# Drop unnecessary columns if present
columns_to_drop = ['id', 'attack_cat']
df_train = df_train.drop(columns=[col for col in columns_to_drop if col in df_train.columns])
df_test = df_test.drop(columns=[col for col in columns_to_drop if col in df_test.columns])

# Separate features and target labels
X_train = df_train.drop(columns=['label'])
y_train = df_train['label']

X_test = df_test.drop(columns=['label'])
y_test = df_test['label']

# Normalize feature data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Predict and evaluate the model
y_pred = model.predict(X_test_scaled)

print("Model Evaluation Results")
print("------------------------")
print(f"Accuracy Score: {accuracy_score(y_test, y_pred):.4f}")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
