# ml_engine.py
import pandas as pd
import joblib

# Cargar modelo y LabelEncoder
model = joblib.load("data/trained_model.pkl")
le_label = joblib.load("data/processed/label_encoder.pkl")
print("✅ Modelo y LabelEncoder cargados correctamente.")

def predict_intrusion(record: str):
    """
    Recibe un registro de red como string separado por comas.
    Devuelve el nombre del ataque (normal, smurf, neptune, etc.)
    """
    try:
        features = record.strip().split(",")
        if len(features) != len(model.feature_names_in_):
            raise ValueError(f"Se esperaban {len(model.feature_names_in_)} features, recibidas {len(features)}")
        df = pd.DataFrame([features], columns=model.feature_names_in_)
        pred_num = model.predict(df)[0]
        pred_label = le_label.inverse_transform([pred_num])[0]
        return pred_label
    except Exception as e:
        print("Error en predicción:", e)
        return None
