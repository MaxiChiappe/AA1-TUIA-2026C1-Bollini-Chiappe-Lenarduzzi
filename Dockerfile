FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos primero el requirements para aprovechar la caché de Docker
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de los archivos
COPY inferencia.py .
COPY modelo.h5 .
COPY imputer_num.joblib .
COPY imputer_cat.joblib .
COPY scaler.joblib .
COPY columnas_train.joblib .
COPY input.json .
# Comando por defecto
ENTRYPOINT ["python", "inferencia.py"]