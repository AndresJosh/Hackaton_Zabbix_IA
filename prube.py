import pandas as pd
import joblib

# Cargar el modelo
model = joblib.load("5G_QoS_Model.pkl")

# Crear un DataFrame asegurando que todas las columnas están presentes
new_data = pd.DataFrame({
    'Signal_Strength': [-75], 
    'Latency': [30], 
    'Required_Bandwidth': [10],
    'Resource_Allocation': [70],
    'Application_Type_Video_Call': [1],
    'Application_Type_Streaming': [0],
    'Application_Type_Online_Gaming': [0],
    'Application_Type_Voice_Call': [0],
    'Application_Type_Emergency_Service': [0],
    'Application_Type_Background_Download': [0],
    'Application_Type_Web_Browsing': [0],
    'Application_Type_IoT_Temperature': [0],
    'Application_Type_Video_Streaming': [0],
    'Application_Type_File_Download': [0],
    'Application_Type_VoIP_Call': [0]  # Se agrega la columna faltante
})

# Asegurarse de que las columnas estén en el mismo orden que en el modelo
new_data = new_data[model.feature_names_in_]

# Hacer la predicción
predicted_bandwidth = model.predict(new_data)
print(f"Ancho de Banda Asignado Predicho: {predicted_bandwidth[0]} Mbps")
