# Predicción de Bancarrota con Regresión Logística en Azure

Este mini-proyecto entrena un modelo de regresión logística para predecir si una empresa se irá a bancarrota, lo despliega en Azure, y expone una API para inferencia.

## Pasos para usar este repositorio

**Paso 1: Fork it**  
Haz un fork de este repo para guardarlo en tu cuenta y trabajar con él.

**Paso 2: Ejecuta `1_Model.ipynb`**  
Entrena el modelo, lo evalúa y guarda `model.pkl`.

**Paso 3: Ejecuta `2_Deployer.ipynb`**  

- Registra el modelo en Azure ML.
- Genera el archivo `score.py`.
- Crea el entorno con `pandas`, `scikit-learn` y `numpy`.
- Despliega el modelo como un endpoint REST en Azure.

**Paso 4: Ejecuta `3_API.ipynb`**  

- Carga un archivo de prueba (`prueba.csv`).
- Lo convierte a JSON.
- Hace la petición al endpoint en Azure.
- Devuelve predicciones.

## Archivos incluidos

| Archivo         | Descripción                                              |
|----------------|----------------------------------------------------------|
| `1_Model.ipynb` | Entrenamiento del modelo de regresión logística         |
| `2_Deployer.ipynb` | Registro del modelo y despliegue en Azure         |
| `3_API.ipynb`   | Cliente API para enviar datos y obtener predicciones    |
| `score.py`      | Script de inferencia utilizado en Azure                 |
| `uri.json`      | Contiene la URI del servicio desplegado                 |
| `model.pkl`     | Modelo serializado                                      |
| `prueba.csv`    | Dataset de prueba para predicciones                     |

## ¿Cómo usar la API?

Una vez desplegado, puedes hacer peticiones a la API usando el código en `3_API.ipynb`.  
Solo necesitas reemplazar el archivo `prueba.csv` por el dataset que quieras evaluar.

Nota: Las columnas deben coincidir exactamente con las usadas durante el entrenamiento.

## Requisitos mínimos del sistema

- Sistema Operativo: Windows 10/11, macOS 12+ o Linux.
- RAM: 4 GB (8 GB recomendados).
- CPU: Procesador de al menos 2 núcleos (Intel i5 o equivalente).
- Python: Versión 3.9 o superior.
- Librerías requeridas: `pandas`, `scikit-learn`, `numpy`, `requests`, `azureml-core`.
- Conexión a Internet: Requerida para trabajar con Azure y hacer solicitudes a la API.

