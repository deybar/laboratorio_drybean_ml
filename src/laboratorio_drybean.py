
"""
Laboratorio 1 - Dry Bean Dataset
Rol: Data Engineer / Analyst

Objetivo:
Comprender, explorar y preparar el dataset Dry Bean Dataset
para un problema de clasificación multiclase siguiendo
las fases de CRISP-DM y buenas prácticas del TDSP.

Artefactos generados:
- Dataset original (raw)
- Dataset limpio y transformado (processed)
- Conjuntos train/test
- Gráfico de distribución de clases
"""

# ======================================================
# 1. IMPORTACIÓN DE LIBRERÍAS
# ======================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split

# ======================================================
# 2. CARGA DEL DATASET DESDE UCI
# ======================================================
print("\n========== PASO 2: CARGA DEL DATASET ==========")

dry_bean = fetch_ucirepo(id=602)

X = dry_bean.data.features
y = dry_bean.data.targets

df = pd.concat([X, y], axis=1)

print("\nPrimeras filas del dataset:")
print(df.head())

# Guardar dataset ORIGINAL sin modificar (data/raw)
df.to_csv("data/raw/dry_bean_original.csv", index=False)

# ======================================================
# 3. RESPUESTAS INICIALES DEL LABORATORIO
# ======================================================
print("\n========== RESPUESTAS DEL ESTUDIANTE ==========")
print(f"1. Número de columnas: {df.shape[1]}")
print("2. Variable objetivo: Class")
print("3. Tipo de problema: Clasificación multiclase")

# ======================================================
# 4. COMPRENSIÓN DE LOS DATOS – CRISP-DM
# ======================================================
print("\n========== COMPRENSIÓN DE LOS DATOS ==========")

print("\nForma del dataset (filas, columnas):")
print(df.shape)

print("\nInformación general del dataset:")
df.info()

print("\nEstadísticas descriptivas:")
print(df.describe())

print("""
INTERPRETACIÓN:
- El dataset contiene 13.611 registros y 17 columnas.
- Todas las variables predictoras son numéricas.
- La variable objetivo 'Class' es categórica.
- Existen posibles valores extremos visibles en las estadísticas descriptivas.
""")

# ======================================================
# 5. CALIDAD DE DATOS: NULOS Y DUPLICADOS
# ======================================================
print("\n========== CALIDAD DE LOS DATOS ==========")

missing_values = df.isna().sum()
duplicated_rows = df.duplicated().sum()

print("\nValores nulos por columna:")
print(missing_values)

print(f"\nFilas duplicadas encontradas: {duplicated_rows}")

rows_before = df.shape[0]

if duplicated_rows > 0:
    df = df.drop_duplicates()
    rows_after = df.shape[0]
    print(f"Registros eliminados por duplicados: {rows_before - rows_after}")
else:
    print("No se encontraron filas duplicadas.")

# ======================================================
# 6. ANÁLISIS DE LA VARIABLE OBJETIVO
# ======================================================
print("\n========== ANÁLISIS DE LA VARIABLE OBJETIVO ==========")

class_counts = df["Class"].value_counts()
class_percentage = df["Class"].value_counts(normalize=True) * 100

class_summary = pd.DataFrame({
    "Cantidad": class_counts,
    "Porcentaje (%)": class_percentage.round(2)
})

print("\nResumen de clases:")
print(class_summary)

# Gráfico de distribución de clases
plt.figure(figsize=(11, 6))
bars = plt.bar(
    class_counts.index,
    class_counts.values,
    color=plt.cm.Set2.colors
)

plt.title("Distribución de clases del dataset Dry Bean", fontsize=14)
plt.xlabel("Clase de frijol")
plt.ylabel("Cantidad de registros")
plt.xticks(rotation=45)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{int(height)}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig("outputs/reports/distribucion_clases.png")
plt.close()

print("""
INTERPRETACIÓN:
- Las clases no están balanceadas.
- 'DERMASON' es la clase mayoritaria y 'BOMBAY' la minoritaria.
- Se recomienda usar métricas como F1-macro y considerar class_weight
  en los modelos de clasificación.
""")

# ======================================================
# 7. PREPARACIÓN DE LOS DATOS PARA MODELADO
# ======================================================
print("\n========== PREPARACIÓN DE LOS DATOS ==========")

X = df.drop(columns="Class")
y = df["Class"]

print("Dimensiones finales:")
print("X (features):", X.shape)
print("y (target):", y.shape)

# ======================================================
# 8. DIVISIÓN TRAIN / TEST – TDSP
# ======================================================
print("\n========== DIVISIÓN ENTRENAMIENTO / PRUEBA ==========")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("X_train:", X_train.shape)
print("X_test:", X_test.shape)

print("""
DECISIÓN TDSP:
- random_state=42 para reproducibilidad.
- stratify=y para conservar la distribución de clases.
""")

# ======================================================
# 9. GUARDADO DE ARTEFACTOS PARA ML ENGINEER
# ======================================================
print("\n========== GUARDADO DE ARTEFACTOS ==========")

df.to_csv("data/processed/dry_bean_clean.csv", index=False)
X_train.to_csv("data/processed/X_train.csv", index=False)
X_test.to_csv("data/processed/X_test.csv", index=False)
y_train.to_csv("data/processed/y_train.csv", index=False)
y_test.to_csv("data/processed/y_test.csv", index=False)

print("""
ARCHIVOS GENERADOS:
- data/raw/dry_bean_original.csv
- data/processed/dry_bean_clean.csv
- data/processed/X_train.csv
- data/processed/X_test.csv
- data/processed/y_train.csv
- data/processed/y_test.csv
- outputs/reports/distribucion_clases.png

Estos archivos deben ser utilizados directamente por el ML Engineer.
""")

print("\n========= FIN DEL ROL DATA ENGINEER =========")
