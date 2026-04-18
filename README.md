# 📊 Trabajo Práctico 1 - Modelo Predictivo de Tarifas de Uber

Este proyecto tiene como objetivo desarrollar un modelo de regresión para predecir el costo de viajes de Uber a partir de distintas variables del dataset.

## 👨‍💻 Integrantes
- Bollini, Lorenzo  
- Chiappe, Maximiliano  
- Lenarduzzi, Juan  

## 🏫 Institución
Facultad de Ciencias Exactas, Ingeniería y Agrimensura (FCEIA)  
Universidad Nacional de Rosario (UNR)

---

## 📁 Dataset

Se utiliza el dataset **uber_fares**, que contiene información sobre viajes, incluyendo:

- `fare_amount`: costo del viaje  
- `pickup_datetime`: fecha y hora  
- `passenger_count`: cantidad de pasajeros  
- `pickup/dropoff_latitude & longitude`: coordenadas geográficas  

---

## ⚙️ Contenido del proyecto

El análisis se divide en las siguientes etapas:

1. **Configuración del entorno**
2. **Carga e inspección del dataset**
3. **Análisis descriptivo**
4. **Feature Engineering**
   - Cálculo de distancias (métrica Manhattan)
   - Procesamiento de fechas
5. **Limpieza de datos**
6. **División Train-Test**
7. **Modelado con regresión lineal**
8. **Optimización de hiperparámetros**
9. **Comparación de modelos**
10. **Conclusiones**

---

## 🧠 Metodología

Se aplican técnicas de aprendizaje automático supervisado, enfocadas en modelos de regresión.  
Se prioriza el preprocesamiento de datos y la generación de variables relevantes para mejorar la performance.

---

## 📈 Objetivo

Predecir el valor de la tarifa (`fare_amount`) de un viaje en base a sus características.

---

## ▶️ Cómo ejecutar

1. Clonar el repositorio:
```bash
git clone <URL_DEL_REPO>
