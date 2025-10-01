# prepare_dataset_preserve_labels.py
import pandas as pd
import os
import joblib
from sklearn.preprocessing import LabelEncoder

RAW_PATH = "data/raw/"
PROCESSED_PATH = "data/processed/nsl_kdd.csv"
LABEL_ENCODER_PATH = "data/processed/label_encoder.pkl"

os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)

files = ["KDDTrain+.txt", "KDDTest+.txt"]
dfs = []
for f in files:
    p = os.path.join(RAW_PATH, f)
    if os.path.exists(p):
        # leer sin encabezado; NSL-KDD usa comas
        df = pd.read_csv(p, header=None)
        dfs.append(df)
        print("✅ Cargado", f)
    else:
        print("⚠️ No se encontró", p)

if not dfs:
    raise SystemExit("No se cargaron archivos raw. Pon los .txt en data/raw/")

df_total = pd.concat(dfs, ignore_index=True)

# Asignar nombres de columna: f0..f40 + label (NSL-KDD tiene 42 columnas incl label)
num_cols = df_total.shape[1]
cols = [f"f{i}" for i in range(num_cols-1)] + ["label"]
df_total.columns = cols

# Asegurar que 'label' sea string (strip espacios)
df_total["label"] = df_total["label"].astype(str).str.strip()

# NO codificamos 'label' aquí. Solo codificamos otras columnas si son object
from sklearn.preprocessing import LabelEncoder
encoders = {}
for c in df_total.columns[:-1]:
    if df_total[c].dtype == "object":
        le = LabelEncoder()
        df_total[c] = le.fit_transform(df_total[c].astype(str))
        encoders[c] = le
        print(f"Columna {c} codificada (categorical)")

# Guardar CSV procesado (LABEL COMO NOMBRES)
df_total.to_csv(PROCESSED_PATH, index=False)
print("✅ Guardado processed CSV en", PROCESSED_PATH)

# Guardar LabelEncoder del label (SÓLO etiqueta, con nombres reales)
le_label = LabelEncoder()
le_label.fit(df_total["label"])
joblib.dump(le_label, LABEL_ENCODER_PATH)
print("✅ LabelEncoder de labels guardado en", LABEL_ENCODER_PATH)
