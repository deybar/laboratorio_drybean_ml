# 🫘 Clasificación de Variedades de Frijol Seco - Dry Bean Dataset

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![Status](https://img.shields.io/badge/Estado-Sprint%201-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/Licencia-Académica-green?style=for-the-badge)

### 📚 Proyecto de Machine Learning  
### 🎓 Maestría en Inteligencia Artificial y Ciencia de Datos  
### 🏫 Universidad Autónoma de Occidente (UAO)

</div>

---

# 📌 Descripción del Proyecto

Este proyecto tiene como objetivo desarrollar un sistema de **clasificación multiclase** capaz de identificar variedades de frijol seco utilizando técnicas de **Machine Learning** y características geométricas extraídas mediante **visión por computador**.

El desarrollo se realiza aplicando metodologías profesionales utilizadas en proyectos reales de Ciencia de Datos e Inteligencia Artificial:

- 🔄 **CRISP-DM** → Metodología estándar para minería de datos
- 🧠 **TDSP** → Team Data Science Process
- ⚡ **Scrum ML** → Gestión ágil aplicada a Machine Learning

---

# 🎯 Objetivo General

Construir y evaluar modelos de clasificación que permitan predecir correctamente la variedad de frijol seco a partir de variables geométricas, garantizando:

- ✔️ Alta precisión de clasificación
- ✔️ Reproducibilidad del proyecto
- ✔️ Buenas prácticas de ingeniería de datos
- ✔️ Documentación clara y escalabilidad

---

# 🏗️ Arquitectura del Proyecto (TDSP)

```bash
laboratorio_drybean_ml/
│
├── data/
│   ├── raw/                 # Datos originales sin modificar
│   └── processed/           # Datos limpios y transformados
│
├── notebooks/               # Exploración y experimentación
│
├── outputs/
│   ├── models/              # Modelos entrenados (.joblib)
│   └── reports/             # Métricas, gráficos y reportes
│
├── src/                     # Código fuente modular
│
├── requirements.txt         # Dependencias del proyecto
├── README.md                # Documentación principal
└── .gitignore
```

---

## 👥 Equipo y Roles (Scrum ML)

| Rol                        | Responsable                | GitHub                    | Responsabilidades |
|---------------------------|----------------------------|---------------------------|-------------------|
| **Product Owner**         | Martín Herrera             | @martinherrera-144        | Definir objetivos y priorizar tareas |
| **Scrum Master**          | Deybar Mora                | @deybar                   | Coordinar el proceso y remover impedimentos |
| **Data Engineer / Analyst** | Luisa Candelo            | @LuisaCandelo             | Limpieza, transformación y análisis de datos |
| **ML Engineer**           | Valentina Sierra / Jahir Giraldo | @Valentinasierra98 / @JahirSnake | Entrenamiento, evaluación y despliegue |

---

## 📋 Project Board (Scrum)

**Seguimiento del proyecto:**  
[🔗 Scrum ML - Dry Bean Dataset (Project Board)](https://github.com/users/deybar/projects/5)

---

## 📌 Product Backlog


- [x] PB-01: Descargar y cargar dataset Dry Bean
- [x] PB-02: Análisis Exploratorio y Calidad de Datos
- [x] PB-03: Modelo Baseline - Logistic Regression
- [x] PB-04: Modelo Mejorado - Random Forest
- [x] PB-05: Evaluación y Comparación de Modelos
- [x] PB-06: Matriz de Confusión y Visualizaciones
- [x] PB-07: Revisión y Aprobación (Product Owner)
- [x] PB-08: Guardar Modelo y Preparar Entrega

---

# 🚀 Planeación de Sprints

## 🥇 Sprint 1 — Comprensión del Negocio y Datos
- Comprensión del problema
- Obtención del dataset
- Limpieza y preparación de datos
- Exploración inicial

## 🥈 Sprint 2 — Modelado y Evaluación
- Entrenamiento de modelos
- Ajuste de hiperparámetros
- Comparación de métricas
- Evaluación de desempeño

## 🥉 Sprint 3 — Despliegue y Documentación
- Exportación del modelo
- Organización del repositorio
- Elaboración de reportes
- Presentación final

---

# 🛠️ Tecnologías Utilizadas

<div align="center">

| Tecnología | Uso |
|------------|-----|
| 🐍 Python 3.10+ | Desarrollo principal |
| 📊 pandas / numpy | Procesamiento de datos |
| 📈 matplotlib / seaborn | Visualización |
| 🤖 scikit-learn | Modelado de Machine Learning |
| 📦 joblib | Persistencia de modelos |
| 📚 ucimlrepo | Descarga del dataset |
| 📓 Jupyter Notebook | Experimentación |

</div>

---

# 📥 Instalación y Ejecución

## 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/deybar/laboratorio_drybean_ml.git
cd laboratorio_drybean_ml
```

---

## 2️⃣ Crear entorno virtual

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Ejecutar Jupyter Notebook

```bash
jupyter notebook
```

---

# 📊 Métricas de Evaluación

Los modelos serán evaluados utilizando:

- 🎯 **Accuracy**
- 📌 **F1-Score Macro**
- 📉 **Matriz de Confusión**
- 📈 Comparación entre modelos

---

# ✅ Definition of Done (DoD)

El proyecto se considerará terminado cuando:

- ✔️ El código ejecute sin errores
- ✔️ El dataset esté correctamente procesado
- ✔️ Los modelos estén entrenados
- ✔️ Las métricas sean reportadas
- ✔️ Exista una matriz de confusión
- ✔️ El proyecto sea reproducible
- ✔️ La documentación esté completa

---

# 📂 Dataset

El proyecto utiliza el **Dry Bean Dataset** del repositorio UCI Machine Learning Repository.

📎 Características del dataset:

- 7 clases de frijoles
- Variables geométricas y morfológicas
- Problema de clasificación multiclase
- Datos provenientes de visión artificial

---

# 📄 Licencia

Proyecto académico desarrollado para la:

### 🎓 Maestría en Inteligencia Artificial y Ciencia de Datos  
### 🏫 Universidad Autónoma de Occidente (UAO)

Uso exclusivamente educativo y académico.

---

# 📌 Estado del Proyecto

```diff
+ ✅ Sprint 2 Finalizado - Modelado y Evaluación completo
+ ✅ Sprint 3 Finalizado
```

---

# 📊 Resultados Obtenidos (Sprint 2)

Tras la fase de experimentación, se obtuvieron los siguientes resultados:

* **Modelo Seleccionado:** Random Forest Classifier.
* **Accuracy:** 92%.
* **F1-Score (Macro):** 0.93.
* **Hallazgo Clave:** El perímetro y el área son las variables con mayor poder predictivo para diferenciar las variedades de frijol.

<div align="center">

## ⭐ Si este proyecto te parece interesante, no olvides darle una estrella al repositorio ⭐

</div>
