import numpy as np
import pandas as pd
import joblib
import tensorflow as tf
import json
import sys

# ── Carga de artefactos ──────────────────────────────────────────────
modelo = tf.keras.models.load_model('modelo.h5')
imputer_num = joblib.load('imputer_num.joblib')
imputer_cat = joblib.load('imputer_cat.joblib')
scaler = joblib.load('scaler.joblib')
columnas_train = joblib.load('columnas_train.joblib')

# ── Columnas por tipo (igual que en el notebook) ─────────────────────
cols_num = ['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine',
            'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am',
            'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am',
            'Cloud3pm', 'Temp9am', 'Temp3pm']

cols_cat = ['Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday', 'Month']

def preprocesar(df):
    # Extraemos el mes de la fecha antes de imputar
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month.astype(str)
    df = df.drop(columns=['Date'])

    # Imputación
    df[cols_num] = imputer_num.transform(df[cols_num])
    df[cols_cat] = imputer_cat.transform(df[cols_cat])

    # One-Hot Encoding
    df = pd.get_dummies(df, columns=cols_cat, drop_first=True)

    # Alineamos columnas con las del train
    df = df.reindex(columns=columnas_train, fill_value=0)

    # Escalado
    df[cols_num] = scaler.transform(df[cols_num])

    return df

def predecir(input_json):
    datos = pd.DataFrame([input_json])
    datos_proc = preprocesar(datos)
    proba = modelo.predict(datos_proc).flatten()[0]
    clase = int(proba >= 0.5)
    return {
        'probabilidad_lluvia': round(float(proba), 4),
        'prediccion': 'Llueve' if clase == 1 else 'No llueve'
    }

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_json = json.loads(sys.argv[1])
    else:
        with open('input.json') as f:
            input_json = json.load(f)
    resultado = predecir(input_json)
    print(json.dumps(resultado, indent=2))