import pandas as pd

# === 1. Definir nombres de las columnas ===
columns = [
    "duration","protocol_type","service","flag","src_bytes","dst_bytes",
    "land","wrong_fragment","urgent","hot","num_failed_logins","logged_in",
    "num_compromised","root_shell","su_attempted","num_root","num_file_creations",
    "num_shells","num_access_files","num_outbound_cmds","is_host_login","is_guest_login",
    "count","srv_count","serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate",
    "same_srv_rate","diff_srv_rate","srv_diff_host_rate","dst_host_count",
    "dst_host_srv_count","dst_host_same_srv_rate","dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate","dst_host_srv_diff_host_rate","dst_host_serror_rate",
    "dst_host_srv_serror_rate","dst_host_rerror_rate","dst_host_srv_rerror_rate",
    "label","difficulty"
]

def convertir_txt_a_csv(input_file, output_file):
    print(f"📂 Convirtiendo {input_file} ...")
    df = pd.read_csv(input_file, names=columns)
    df.to_csv(output_file, index=False)
    print(f"✅ Guardado en {output_file}")

if __name__ == "__main__":
    # Convertir dataset de entrenamiento
    convertir_txt_a_csv("data/KDDTrain+.txt", "data/KDDTrain+.csv")
    # Convertir dataset de prueba
    convertir_txt_a_csv("data/KDDTest+.txt", "data/KDDTest+.csv")
