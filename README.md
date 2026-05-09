# Laboratorio de Machine Learning - Dry Bean Dataset

**Clasificación de variedades de frijol seco mediante visión por computador**

Proyecto desarrollado como parte de la **Maestría en Inteligencia Artificial y Ciencia de Datos**  
**Asignatura:** Gestión de Proyectos en IA y CD

---

## 🎯 Objetivo del Proyecto

Construir un modelo de clasificación que prediga la variedad de frijol seco a partir de características geométricas extraídas de imágenes, aplicando de forma rigurosa las metodologías:

- **CRISP-DM** (estándar para proyectos de minería de datos)
- **TDSP** (Team Data Science Process)
- **Scrum ML** (gestión ágil adaptada a proyectos de Machine Learning)

---

## 🏗️ Estructura del Proyecto (TDSP)

```bash
laboratorio_drybean_ml/
├── data/
│   ├── raw/           # Datos originales (sin modificar)
│   └── processed/     # Datos limpios y preparados
├── notebooks/         # Notebooks de exploración y experimentación
├── outputs/
│   ├── models/        # Modelos entrenados (.joblib)
│   └── reports/       # Métricas, gráficas y reportes
├── src/               # Código fuente reutilizable (módulos Python)
├── requirements.txt
├── README.md
└── .gitignore