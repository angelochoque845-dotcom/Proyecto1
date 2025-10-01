# encode_labels.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Cargar dataset original (con números o nombres)
df = pd.read_csv("data/processed/nsl_kdd.csv")

# Mapear números a nombres (si tu CSV solo tiene números)
num_to_name = {
    0: "normal",
    1: "neptune",
    2: "smurf",
    3: "satan",
    4: "ipsweep",
    5: "portsweep",
    6: "teardrop",
    7: "nmap",
    8: "guess_passwd",
    9: "buffer_overflow",
    10: "imap",
    11: "pod",
    12: "land",
    13: "ftp_write",
    14: "loadmodule",
    15: "multihop",
    16: "phf",
    17: "perl",
    18: "spy",
    19: "warezclient",
    20: "warezmaster",
    21: "rootkit"
}

if df['label'].dtype != object:
    df['label'] = df['label'].map(num_to_name)

# Codificar etiquetas
le = LabelEncoder()
df['label_num'] = le.fit_transform(df['label'])

# Guardar LabelEncoder y dataset codificado
os.makedirs("data/processed", exist_ok=True)
joblib.dump(le, "data/processed/label_encoder.pkl")
df.to_csv("data/processed/nsl_kdd_encoded.csv", index=False)

print("✅ Dataset codificado y LabelEncoder guardado")
print("Clases:", list(le.classes_))
