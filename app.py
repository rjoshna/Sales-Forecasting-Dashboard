import streamlit as st

st.set_page_config(
    page_title="Intelligent Sales Forecasting System",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Intelligent Sales Forecasting System")

st.markdown("""
## Welcome

This dashboard provides:

- 📈 Sales Overview
- 🔮 Sales Forecast Explorer
- 🚨 Anomaly Detection Report
- 📦 Product Demand Segmentation

### Best Forecasting Model

**XGBoost**

**Performance Metrics**
- MAE: **14,763.81**
- RMSE: **18,337.41**
- MAPE: **14.48%**

Use the navigation menu on the left to explore each page.
""")

st.success("Dashboard successfully built using Streamlit.")
