# Hackaton_Zabbix_IA

# 🚀 AI-Enhanced Zabbix Monitoring - Implementation Guide

This guide provides step-by-step instructions to deploy **Zabbix with AI-powered monitoring** and a **web-based prediction system**.

## 📌 Project Overview
- **Zabbix Server:** Monitors network performance, alerts issues.
- **AI Integration:** Uses **Orca Mini** & **GPT-4** to diagnose & recommend fixes.
- **Web Interface:** Streamlit app predicts bandwidth & provides recommendations.
- **Machine Learning Model:** Predicts network bandwidth allocation based on traffic patterns.

---


# 1️⃣ Zabbix Setup (Ubuntu Server)
## ✅ Prerequisites
- Ubuntu 20.04/22.04 LTS
- MySQL Server & Apache
- SNMP-enabled devices (Mikrotik, ESP32, PCs)

## 🔧 Installation
```bash
sudo apt update && sudo apt upgrade -y
wget https://repo.zabbix.com/zabbix/6.4/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.4-1+ubuntu20.04_all.deb
sudo dpkg -i zabbix-release_6.4-1+ubuntu20.04_all.deb
sudo apt update
sudo apt install zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf zabbix-agent snmpd -y
```

## 🛠 Configuration
- **Set up MySQL Database**
- **Enable SNMP monitoring**
- **Configure hosts & alerts in Zabbix**

---

# 2️⃣ AI Integration with Zabbix
## ✅ Prerequisites
- Python 3.9+
- `gpt4all` installed
- SSH connection between AI & Zabbix server
- `paramiko` for SSH automation

## 🔧 Installation
```bash
pip install gpt4all paramiko
```

## 🛠 Setup
- **Orca Mini & GPT-4 Deployment**
  - Install AI models locally.
  - Load **Orca Mini** for lightweight tasks.
  - Use **GPT-4** for advanced recommendations.
  
- **AI-Zabbix Interaction Script (`chatgpt_api.py`)**
  - Fetch alerts from Zabbix via API.
  - Use AI to diagnose root causes.
  - Automate response generation.

## 🚀 Running the AI Assistant
```bash
python ai-integration/chatgpt_api.py
```

---

# 3️⃣ Web Interface (Streamlit)
## ✅ Prerequisites
- Python 3.9+
- `streamlit`, `joblib`, `numpy`, `gpt4all`

## 🔧 Installation
```bash
pip install streamlit joblib numpy gpt4all
```

## 🛠 Setup
- **Deploy Streamlit app (`app.py`)** for bandwidth prediction
- **Connect AI for real-time insights**
- **Enable user input for AI-driven recommendations**

## 🚀 Running the Web App
```bash
streamlit run web-interface/app.py
```

---

# 4️⃣ Machine Learning Model
## ✅ Prerequisites
- `scikit-learn`, `pandas`, `joblib`

## 🔧 Installation
```bash
pip install scikit-learn pandas joblib
```

## 🛠 Setup
- **Train ML Model (`traning.py`)**
  - Preprocess Kaggle dataset (`h.py` downloads it)
  - Train RandomForestRegressor
  - Save trained model as `5G_QoS_Model.pkl`

- **Test ML Model (`prube.py`)**
  - Load `5G_QoS_Model.pkl`
  - Predict bandwidth allocation based on test data

## 🚀 Training the Model
```bash
python ml-model/traning.py
```

## 🚀 Testing Predictions
```bash
python ml-model/prube.py
```

---

# 🚀 Deployment
## 🏗️ Run Services
```bash
sudo systemctl start zabbix-server apache2
python ai-integration/chatgpt_api.py &
streamlit run web-interface/app.py
```

## 🛠 Future Improvements
- Automate AI-Zabbix communication
- Expand AI model capabilities
- Enhance real-time alerts with AI predictions

---

### 💡 This guide ensures smooth deployment of AI-powered Zabbix monitoring. Let me know if you need refinements! 🚀
