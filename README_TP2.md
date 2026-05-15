# 📊 Trabajo Práctico 2 - Predicción de Lluvia en Australia

Este proyecto tiene como objetivo desarrollar modelos de clasificación capaces de predecir si lloverá al día siguiente utilizando datos meteorológicos históricos de distintas ciudades de Australia.

## 👨‍💻 Integrantes
- Bollini, Lorenzo  
- Chiappe, Maximiliano  
- Lenarduzzi, Juan  

## 🏫 Institución
Facultad de Ciencias Exactas, Ingeniería y Agrimensura (FCEIA)  
Universidad Nacional de Rosario (UNR)

---

## 📁 Dataset

Se utiliza el dataset **WeatherAUS**, que contiene información meteorológica histórica, incluyendo:

- `MinTemp`: temperatura mínima  
- `MaxTemp`: temperatura máxima  
- `Rainfall`: precipitaciones  
- `Humidity`: humedad  
- `Pressure`: presión atmosférica  
- `WindSpeed`: velocidad del viento  
- `Cloud`: nubosidad  
- `RainTomorrow`: variable objetivo  

---

## ⚙️ Contenido del proyecto

El análisis se divide en las siguientes etapas:

1. **Configuración del entorno**
2. **Carga e inspección del dataset**
3. **Análisis descriptivo**
4. **Limpieza y preprocesamiento de datos**
5. **Tratamiento de valores faltantes**
6. **Codificación y escalado de variables**
7. **División Train-Test**
8. **Entrenamiento de modelos de clasificación**
9. **Evaluación y comparación de modelos**
10. **Conclusiones**

---

## 🧠 Metodología

Se aplican técnicas de aprendizaje automático supervisado orientadas a problemas de clasificación.  
Se prioriza el análisis exploratorio, el tratamiento adecuado de los datos y la evaluación mediante distintas métricas para comparar el rendimiento de los modelos.

---

## 📈 Objetivo

Predecir si ocurrirá lluvia al día siguiente (`RainTomorrow`) en base a distintas variables meteorológicas.

---

## 🤖 Modelos utilizados

- Regresión Logística  
- Random Forest  

También se compararon resultados utilizando datasets:

- Balanceados  
- Sin balancear  

---

## 📊 Métricas de evaluación

Para evaluar el rendimiento de los modelos se utilizaron:

- Accuracy  
- Precision  
- Recall  
- F1-Score  
- Matriz de confusión  
- Curva ROC  
- AUC  

---

## ▶️ Cómo ejecutar

1. Clonar el repositorio:

```bash
git clone <URL_DEL_REPO>
```

2. Instalar dependencias:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn notebook
```

3. Ejecutar Jupyter Notebook:

```bash
jupyter notebook
```

4. Abrir el archivo:

```bash
TP2.ipynb
```

---

## 📌 Archivos del proyecto

```bash
├── TP2.ipynb
├── weatherAUS_2026C1.csv
└── README.md
```

---

## 📄 Licencia

Trabajo realizado con fines académicos para la materia Aprendizaje Automático 1 (AA1).

