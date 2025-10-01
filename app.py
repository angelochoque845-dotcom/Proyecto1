from flask import Flask, render_template, request
import pandas as pd
from ml_engine import predict_intrusion

app = Flask(__name__)

# Carga dataset procesado
df = pd.read_csv("data/processed/nsl_kdd.csv")

# Asegúrate de que la columna 'label' exista
if 'label' not in df.columns:
    raise ValueError("La columna 'label' no existe en nsl_kdd.csv")

# Filtra ejemplos
df_normal = df[df['label'] == 'normal']
df_attack = df[df['label'] != 'normal']

@app.route("/")
def home():
    # Función segura para convertir DataFrame a lista de strings
    def df_to_list_of_str(df_subset):
        if df_subset.empty:
            return []
        # Asegurarse de que 'label' se elimine solo si existe
        cols = [c for c in df_subset.columns if c != 'label']
        return df_subset[cols].astype(str).apply(lambda row: ','.join(row), axis=1).tolist()

    normal_examples = df_to_list_of_str(df_normal)[:5]
    attack_examples = df_to_list_of_str(df_attack)[:5]

    return render_template("index.html", normal_examples=normal_examples, attack_examples=attack_examples)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.form.get("data").strip()
    prediction = predict_intrusion(data)
    return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
