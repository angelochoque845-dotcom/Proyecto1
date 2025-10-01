import pandas as pd
import os

RAW_PATH = "data/raw/"
PROCESSED_PATH = "data/raw/nsl_kdd.csv"

# Archivos a combinar
archivos = ["KDDTrain+.txt", "KDDTest+.txt"]

# Lista para almacenar dataframes
dfs = []

for archivo in archivos:
    ruta = os.path.join(RAW_PATH, archivo)
    if os.path.exists(ruta):
        df = pd.read_csv(ruta, header=None)
        dfs.append(df)
        print(f"✅ Cargado {archivo}")
    else:
        print(f"⚠️ No se encontró {archivo}")

# Combinar todos
df_total = pd.concat(dfs, ignore_index=True)
print("✅ Archivos combinados")

# Guardar como CSV
df_total.to_csv(PROCESSED_PATH, index=False)
print(f"✅ Guardado como {PROCESSED_PATH}")
