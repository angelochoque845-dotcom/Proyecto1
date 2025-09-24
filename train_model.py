import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# === 1. Cargar dataset de entrenamiento ===
print("📂 Cargando dataset...")
df = pd.read_csv("data/KDDTrain+.csv")

# === 2. Separar características (X) y etiquetas (y) ===
X = df.drop(columns=["label", "difficulty"])
y = df["label"]

# === 3. Codificar variables categóricas (protocol_type, service, flag) ===
X = pd.get_dummies(X, columns=["protocol_type", "service", "flag"])

# === 4. Dividir en entrenamiento y validación ===
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# === 5. Entrenar un modelo Random Forest ===
print("🌲 Entrenando modelo RandomForest...")
model = RandomForestClassifier(n_estimators=50, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# === 6. Evaluar el modelo ===
y_pred = model.predict(X_val)
print("\n📊 Reporte de Clasificación:\n", classification_report(y_val, y_pred))
print("✅ Accuracy:", accuracy_score(y_val, y_pred))

# === 7. Guardar modelo entrenado ===
joblib.dump(model, "data/ids_model.pkl")
print("💾 Modelo guardado en data/ids_model.pkl")
