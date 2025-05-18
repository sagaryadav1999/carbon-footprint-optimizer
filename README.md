# 🌱 Carbon Footprint Optimization in Supply Chain Logistics

This project focuses on building a deep learning model to optimize logistics routes for minimal carbon emissions, helping companies make greener and more sustainable delivery decisions.

## 🚀 Project Overview

Traditional logistics systems prioritize cost and time, often neglecting environmental impact. This project uses machine learning to estimate carbon emissions and suggest optimized logistics routes by analyzing various features like:

- Route distance
- Fuel usage
- Traffic and weather data
- Cargo weight
- Vehicle and shipment type

---

## 📂 Project Structure
icbp/
├── app.py # Streamlit web app for prediction
├── final_project_.ipynb # Jupyter notebook for model training and analysis
├── carbon_emission_model.keras # Trained deep learning model
├── carbon_footprint_logistics.csv # Dataset used for training
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## 🧠 Technologies Used

- Python
- TensorFlow / Keras
- Streamlit (for web app)
- Pandas, NumPy, Matplotlib
- Git/GitHub

---

## 📊 Model Summary

A deep neural network was trained using historical logistics data to predict CO₂ emissions (in kg) per shipment. Evaluation metrics used:

- ✅ Mean Absolute Error (MAE)
- ✅ Root Mean Squared Error (RMSE)
- ✅ % Error

---

## 🌐 Web App Preview

The Streamlit app allows users to:

- Input logistics features (distance, fuel, cargo type, etc.)
- Get real-time carbon footprint prediction
- Make eco-conscious route decisions

Run locally:
```bash
streamlit run app.py


