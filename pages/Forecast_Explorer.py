import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Forecast Explorer")

# Load Forecast Data
forecast = pd.read_csv("forecast_results.csv")

# Select Forecast Type
forecast_type = st.selectbox(
    "Select Forecast",
    [
        "Furniture",
        "Technology",
        "Office Supplies",
        "West Region",
        "East Region"
    ]
)

# Forecast Horizon
months = st.slider(
    "Forecast Horizon (Months)",
    1,
    3,
    3
)

forecast_display = forecast.iloc[:months]

# Plot
fig = px.line(
    forecast_display,
    x="Month",
    y=forecast_type,
    markers=True,
    title=f"{forecast_type} Forecast"
)

st.plotly_chart(fig, use_container_width=True)

# Table
st.subheader("Forecast Values")

st.dataframe(
    forecast_display[["Month", forecast_type]]
)

# Model Performance
st.subheader("Best Model Performance")

st.write("**Selected Model:** XGBoost")

col1, col2 = st.columns(2)

with col1:
    st.metric("MAE", "14,763.81")

with col2:
    st.metric("RMSE", "18,337.41")

st.success(
    "XGBoost was selected because it achieved the lowest MAE, RMSE, and MAPE among all forecasting models."
)
