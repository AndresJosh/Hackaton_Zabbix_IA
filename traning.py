import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Definir la ruta al dataset
dataset_path = r"C:\Users\andre\.cache\kagglehub\datasets\omarsobhy14\5g-quality-of-service\versions\2"

# Buscar archivos CSV en la carpeta
files = [f for f in os.listdir(dataset_path) if f.endswith('.csv')]

# Cargar el primer archivo CSV encontrado
if files:
    file_path = os.path.join(dataset_path, files[0])
    df = pd.read_csv(file_path)
    print("Dataset cargado correctamente.")
else:
    print("No se encontraron archivos CSV en la ruta especificada.")
    exit()

# Mostrar las primeras filas del dataset
print(df.head())

# Eliminar columnas innecesarias
df = df.drop(columns=['Timestamp', 'User_ID'])

# Función para limpiar y convertir valores numéricos
def convert_numeric(value):
    if isinstance(value, str):
        return float(value.replace(" dBm", "").replace(" ms", "").replace(" Mbps", "").replace(" Kbps", "").replace("%", ""))
    return value

# Aplicar la conversión a las columnas necesarias
for col in ['Signal_Strength', 'Latency', 'Required_Bandwidth', 'Allocated_Bandwidth', 'Resource_Allocation']:
    df[col] = df[col].apply(convert_numeric)

# Convertir variables categóricas (One-Hot Encoding)
df = pd.get_dummies(df)

# Dividir los datos en características (X) y variable objetivo (y)
X = df.drop(columns=['Allocated_Bandwidth'])
y = df['Allocated_Bandwidth']

# Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar un modelo de Machine Learning
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Hacer predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo
mae = mean_absolute_error(y_test, y_pred)
print(f"Error Absoluto Medio (MAE): {mae}")

# Guardar el modelo entrenado
import joblib
joblib.dump(model, "5G_QoS_Model.pkl")
print("Modelo guardado exitosamente como '5G_QoS_Model.pkl'.")
