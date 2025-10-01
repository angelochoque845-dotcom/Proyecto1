import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os
import joblib

# Rutas
RAW_PATH = "data/raw/"
PROCESSED_PATH = "data/processed/nsl_kdd.csv"
LABEL_ENCODER_PATH = "data/processed/label_encoder.pkl"

# Crear carpeta processed si no existe
os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)

# Archivos a combinar
archivos = ["KDDTrain+.txt", "KDDTest+.txt"]
dfs = []

for archivo in archivos:
    ruta = os.path.join(RAW_PATH, archivo)
    if os.path.exists(ruta):
        df = pd.read_csv(ruta, header=None)
        dfs.append(df)
        print(f"✅ Cargado {archivo}")
    else:
        print(f"⚠️ No se encontró {archivo}")

# Combinar todos los archivos
df_total = pd.concat(dfs, ignore_index=True)
print("✅ Archivos combinados")

# Asignar nombres de columnas: f0, f1, ..., f41, label
num_cols = df_total.shape[1]
columnas = [f"f{i}" for i in range(num_cols-1)] + ["label"]
df_total.columns = columnas

# Codificar columnas categóricas (menos la última, que será la label)
for col in df_total.columns[:-1]:
    if df_total[col].dtype == 'object':
        le = LabelEncoder()
        df_total[col] = le.fit_transform(df_total[col])
        print(f"Columna '{col}' codificada.")

# Codificar columna label y guardar LabelEncoder
le_label = LabelEncoder()
df_total["label"] = le_label.fit_transform(df_total["label"])
joblib.dump(le_label, LABEL_ENCODER_PATH)
print(f"✅ LabelEncoder de 'label' guardado en {LABEL_ENCODER_PATH}")

# Guardar CSV procesado
df_total.to_csv(PROCESSED_PATH, index=False)
print(f"✅ Dataset procesado y guardado en {PROCESSED_PATH}")
