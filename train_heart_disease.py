import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from xgboost import XGBClassifier

# Load the dataset
df = pd.read_csv("heart.csv")

# Features and target
X = df.drop(columns='target')
y = df['target']

# Stratified split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# Handle imbalance
scale_pos_weight = (y == 0).sum() / (y == 1).sum()

# Train with XGBoost
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss', scale_pos_weight=scale_pos_weight)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save the trained model
pickle.dump(model, open("heart_disease_model.sav", "wb"))
