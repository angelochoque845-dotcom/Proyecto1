import pandas as pd
import joblib

# === 1. Cargar el modelo entrenado ===
try:
    model = joblib.load("data/ids_model.pkl")
    print("✅ Modelo cargado correctamente.")
except Exception as e:
    print("⚠️ No se pudo cargar el modelo:", e)
    model = None

# === 2. Función para predecir intrusiones ===
def predict_intrusion(data: str):
    """
    Recibe una cadena con datos (ej: '0,tcp,http,SF,181,5450,...')
    Devuelve la predicción del modelo (normal o ataque).
    """
    if model is None:
        return "⚠️ Modelo no cargado"

    try:
        # Convertir la entrada en una lista
        values = data.split(",")
        
        # Cargar nombres de columnas desde el dataset original
        columns = [
            "duration","protocol_type","service","flag","src_bytes","dst_bytes",
            "land","wrong_fragment","urgent","hot","num_failed_logins","logged_in",
            "num_compromised","root_shell","su_attempted","num_root","num_file_creations",
            "num_shells","num_access_files","num_outbound_cmds","is_host_login","is_guest_login",
            "count","srv_count","serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate",
            "same_srv_rate","diff_srv_rate","srv_diff_host_rate","dst_host_count",
            "dst_host_srv_count","dst_host_same_srv_rate","dst_host_diff_srv_rate",
            "dst_host_same_src_port_rate","dst_host_srv_diff_host_rate","dst_host_serror_rate",
            "dst_host_srv_serror_rate","dst_host_rerror_rate","dst_host_srv_rerror_rate"
        ]
        
        # Crear DataFrame con un solo registro
        df = pd.DataFrame([values], columns=columns)

        # One-hot encoding (para coincidir con entrenamiento)
        df = pd.get_dummies(df, columns=["protocol_type", "service", "flag"])

        # Alinear columnas con el modelo entrenado
        missing_cols = set(model.feature_names_in_) - set(df.columns)
        for c in missing_cols:
            df[c] = 0  # columnas faltantes con 0
        df = df[model.feature_names_in_]

        # Predicción
        pred = model.predict(df)[0]
        return f" Predicción: {pred}"

    except Exception as e:
        return f"❌ Error procesando datos: {e}"
