# models.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Cargar dataset codificado
df = pd.read_csv("data/processed/nsl_kdd_encoded.csv")

# Separar features y target
X = df.drop(columns=["label", "label_num"])
y = df["label_num"]

# Entrenar RandomForest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Guardar modelo entrenado
os.makedirs("data", exist_ok=True)
joblib.dump(model, "data/trained_model.pkl")
print("✅ Modelo entrenado y guardado")

# Guardar LabelEncoder (solo si no existe)
if not os.path.exists("data/processed/label_encoder.pkl"):
    le = joblib.load("data/processed/label_encoder.pkl")
    joblib.dump(le, "data/processed/label_encoder.pkl")
