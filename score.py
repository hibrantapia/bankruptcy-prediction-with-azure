
import json
import joblib
import numpy as np
import pandas as pd
from azureml.core.model import Model

def init():
    global model
    model_path = Model.get_model_path('model')
    model = joblib.load(model_path)

def run(raw_data):
    try:
        # Cargar y convertir los datos a DataFrame
        data = json.loads(raw_data)['data']
        df = pd.DataFrame(data)

        # Asegurar nombres de columnas limpios (sin espacios)
        df.columns = df.columns.str.strip()

        # Hacer predicción
        result = model.predict(df).tolist()

        return json.dumps(result)

    except Exception as e:
        return json.dumps({{"error": str(e)}})
