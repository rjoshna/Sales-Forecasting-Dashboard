import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🚨 Sales Anomaly Report")

# Load anomaly data
anomaly = pd.read_csv("anomalies.csv")

# Convert Order Date to datetime
anomaly["Order Date"] = pd.to_datetime(
    anomaly["Order Date"],
    format="mixed",
    dayfirst=True
)

# -----------------------------
# Sales Trend
# -----------------------------
fig = px.line(
    anomaly,
    x="Order Date",
    y="Sales",
    title="Weekly Sales with Detected Anomalies"
)

# Highlight anomalies
anomaly_points = anomaly[anomaly["Anomaly"] == -1]

fig.add_scatter(
    x=anomaly_points["Order Date"],
    y=anomaly_points["Sales"],
    mode="markers",
    marker=dict(color="red", size=10),
    name="Anomaly"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Anomaly Table
# -----------------------------
st.subheader("Detected Anomalies")

st.dataframe(
    anomaly_points[["Order Date", "Sales"]]
)

# -----------------------------
# Summary
# -----------------------------
st.metric(
    "Total Anomalies Detected",
    len(anomaly_points)
)
