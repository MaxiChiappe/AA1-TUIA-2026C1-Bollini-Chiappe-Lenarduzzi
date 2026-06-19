# Inferencia — Modelo de Predicción de Lluvia en Australia

## Requisitos
- Docker instalado en el sistema

## Contenido de la carpeta
- `inferencia.py` — script de inferencia
- `requirements.txt` — dependencias necesarias
- `modelo.h5` — red neuronal entrenada
- `imputer_num.joblib` — imputer para variables numéricas
- `imputer_cat.joblib` — imputer para variables categóricas
- `scaler.joblib` — scaler para estandarización
- `columnas_train.joblib` — columnas del conjunto de entrenamiento
- `input.json` — ejemplo de datos de entrada
- `Dockerfile` — instrucciones para construir la imagen

## Construir la imagen
Desde la carpeta `docker/` ejecutar:
```bash
docker build -t modelo-lluvia .
```

## Ejecutar el contenedor

**Opción 1 — Con datos de ejemplo (input.json incluido):**
```bash
docker run --rm modelo-lluvia
```

**Opción 2 — Pasando datos por línea de comandos (requiere CMD en Windows, no PowerShell):**
```cmd
docker run --rm modelo-lluvia "{\"Date\": \"2021-06-01\", \"Location\": \"Sydney\", \"MinTemp\": 10.5, \"MaxTemp\": 22.3, \"Rainfall\": 0.0, \"Evaporation\": 4.2, \"Sunshine\": 8.1, \"WindGustDir\": \"W\", \"WindGustSpeed\": 35.0, \"WindDir9am\": \"W\", \"WindDir3pm\": \"SW\", \"WindSpeed9am\": 15.0, \"WindSpeed3pm\": 20.0, \"Humidity9am\": 65.0, \"Humidity3pm\": 45.0, \"Pressure9am\": 1015.0, \"Pressure3pm\": 1012.0, \"Cloud9am\": 3.0, \"Cloud3pm\": 4.0, \"Temp9am\": 14.0, \"Temp3pm\": 21.0, \"RainToday\": \"No\"}"
```

## Resultado esperado
```json
{
  "probabilidad_lluvia": 0.4706,
  "prediccion": "No llueve"
}
```

## Notas
- Los datos de entrada deben incluir todas las variables del dataset original
- Los valores faltantes son manejados automáticamente por el script
- La predicción usa un umbral de 0.5 sobre la probabilidad
- En Windows usar CMD en lugar de PowerShell para pasar datos por línea de comandos