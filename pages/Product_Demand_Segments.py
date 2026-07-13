import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📦 Product Demand Segments")

# Load clustered data
clusters = pd.read_csv("clusters.csv")

# -----------------------------
# Scatter Plot
# -----------------------------

fig = px.scatter(
    clusters,
    x="PC1",
    y="PC2",
    color="Demand Segment",
    hover_data=[
        "Total Sales",
        "Growth Rate",
        "Volatility",
        "Average Order Value"
    ],
    title="Product Demand Clusters (PCA Visualization)"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Cluster Table
# -----------------------------

st.subheader("Cluster Assignment")

st.dataframe(
    clusters[
        [
            "Total Sales",
            "Growth Rate",
            "Volatility",
            "Average Order Value",
            "Cluster",
            "Demand Segment"
        ]
    ]
)

# -----------------------------
# Cluster Summary
# -----------------------------

st.subheader("Demand Segment Summary")

summary = clusters.groupby("Demand Segment").size().reset_index(name="Products")

st.dataframe(summary)

# -----------------------------
# Stocking Strategy
# -----------------------------

st.subheader("Recommended Stocking Strategy")

strategies = {
    "High Volume, Stable Demand":
        "✅ Maintain higher inventory levels and prioritize continuous replenishment.",

    "Growing Demand":
        "📈 Gradually increase stock and monitor sales trends closely.",

    "Low Volume, High Volatility":
        "⚠️ Maintain limited safety stock and avoid overstocking.",

    "Declining Demand":
        "📉 Reduce inventory levels and use promotions to clear stock."
}

for segment in clusters["Demand Segment"].unique():

    st.markdown(f"### {segment}")

    st.info(
        strategies.get(
            segment,
            "Monitor demand regularly and adjust inventory accordingly."
        )
    )
