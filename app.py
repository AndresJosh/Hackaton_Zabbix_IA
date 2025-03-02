import streamlit as st
import joblib
import numpy as np
from gpt4all import GPT4All

# Load GPT4All model and test it before continuing
gpt_model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")
initial_test = gpt_model.generate("Test response to verify GPT4All is working correctly.")

# Load the prediction model
model_path = "5G_QoS_Model.pkl"
model = joblib.load(model_path)

# Get feature names expected by the model
feature_names = model.feature_names_in_

st.title("📡 5G Bandwidth Prediction")

st.header("📊 Enter Data for Prediction")

# Display initial test result to ensure GPT4All is working
st.info(f"✅ GPT4All Test Response: {initial_test}")

# Dictionary to store input values
input_data = {}

# Sliders for main values
input_data["Signal_Strength"] = st.slider("Signal Strength (dBm)", -120, 0, -75)
input_data["Latency"] = st.slider("Latency (ms)", 1, 100, 30)
input_data["Required_Bandwidth"] = st.slider("Required Bandwidth (Mbps)", 0.1, 100.0, 10.0)
input_data["Resource_Allocation"] = st.slider("Resource Allocation (%)", 10, 100, 70)

# List of application types
application_types = [
    "Background_Download",
    "Emergency_Service",
    "File_Download",
    "IoT_Temperature",
    "Online_Gaming",
    "Streaming",
    "Video_Call",
    "Video_Streaming",
    "VoIP_Call",
    "Web_Browsing"
]

# Select application type
selected_app = st.selectbox("Application Type", application_types)

# Generate binary values for each application type (1 for selected, 0 for others)
for app in application_types:
    input_data[f"Application_Type_{app}"] = 1 if app == selected_app else 0

# Ensure all required features are present
for feature in feature_names:
    if feature not in input_data:
        input_data[feature] = 0  # Ensure all expected features are defined

# Convert to array in expected order
input_array = np.array([[input_data[feature] for feature in feature_names]])

# Prediction
if st.button("🎯 Predict Bandwidth"):
    try:
        prediction = model.predict(input_array)[0]
        st.success(f"🚀 Assigned Bandwidth: {prediction:.2f} Mbps")
        
        # Get recommendation from GPT4All directly (no HTTP request)
        prompt = f"Given a network bandwidth of {prediction:.2f} Mbps, what are the best optimization strategies?"
        recommendation = gpt_model.generate(prompt)
        st.info(f"💡 Recommendation: {recommendation}")
    except ValueError as e:
        st.error(f"Error in prediction: {e}")