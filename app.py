import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

# Page setup
st.set_page_config(page_title="Carbon Emission Predictor", layout="centered")

# Load trained model
model = load_model("carbon_emission_model.keras")

# --- HEADER ---
st.markdown("<h1 style='text-align: center;'>🚛 Carbon Emission Predictor</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <div style='text-align: center; font-size: 18px;'>
        Enter logistics-related inputs below to estimate the<br><strong>carbon footprint of a shipment (in kg CO₂)</strong>.
    </div>
    <br>
    """,
    unsafe_allow_html=True
)

# --- SIDEBAR INPUT FORM ---
st.sidebar.header("📥 Input Logistics Features")

def get_user_inputs():
    distance_km = st.sidebar.number_input("🛣️ Distance (km)", min_value=1.0, step=1.0)
    fuel_used_liters = st.sidebar.number_input("⛽ Fuel Used (liters)", min_value=0.1, step=0.1)
    delivery_time_hrs = st.sidebar.number_input("⏱️ Delivery Time (hrs)", min_value=0.1, step=0.1)
    fuel_cost_usd = st.sidebar.number_input("💵 Fuel Cost (USD)", min_value=0.1, step=0.1)
    emission_factor = st.sidebar.number_input("🧪 Emission Factor", min_value=0.0, step=0.01)
    co2_per_km = st.sidebar.number_input("🌍 CO₂ per km", min_value=0.0, step=0.01)

    origin_Warehouse_B = st.sidebar.selectbox("🏠 Origin: Warehouse B?", ["No", "Yes"]) == "Yes"
    destination_City_Y = st.sidebar.selectbox("🏙️ Destination: City Y?", ["No", "Yes"]) == "Yes"
    vehicle_type_Truck_Small = st.sidebar.selectbox("🚚 Vehicle: Small Truck?", ["No", "Yes"]) == "Yes"
    shipment_type_Machinery = st.sidebar.selectbox("⚙️ Shipment: Machinery?", ["No", "Yes"]) == "Yes"

    input_data = {
        'distance_km': distance_km,
        'fuel_used_liters': fuel_used_liters,
        'delivery_time_hrs': delivery_time_hrs,
        'fuel_cost_usd': fuel_cost_usd,
        'emission_factor': emission_factor,
        'co2_per_km': co2_per_km,
        'origin_Warehouse_B': int(origin_Warehouse_B),
        'destination_City_Y': int(destination_City_Y),
        'vehicle_type_Truck_Small': int(vehicle_type_Truck_Small),
        'shipment_type_Machinery': int(shipment_type_Machinery)
    }

    return pd.DataFrame([input_data])

# Collect input
input_df = get_user_inputs()

# --- DISPLAY INPUT SUMMARY ---
st.markdown("## 🔍 Input Summary")
st.dataframe(input_df.style.format(precision=2), use_container_width=True)

# --- PREDICTION ---
if st.button("📊 Predict Carbon Emission"):
    try:
        prediction = model.predict(input_df)
        st.success(f"🌱 **Estimated Carbon Emission:** `{prediction[0][0]:.2f}` kg CO₂")
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
