import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("train.csv")

# Convert dates
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="mixed",
    dayfirst=True
)

# Create Year and Month columns
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month_name()

st.title("📊 Sales Overview Dashboard")

# -----------------------------
# Total Sales by Year
# -----------------------------
year_sales = df.groupby("Year")["Sales"].sum().reset_index()

fig1 = px.bar(
    year_sales,
    x="Year",
    y="Sales",
    text_auto=".2s",
    color="Sales",
    title="Total Sales by Year"
)

st.plotly_chart(fig1, use_container_width=True)

# -----------------------------
# Monthly Sales Trend
# -----------------------------
monthly_sales = (
    df.set_index("Order Date")
      .resample("ME")["Sales"]
      .sum()
      .reset_index()
)

fig2 = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# Interactive Filters
# -----------------------------
st.subheader("Sales by Region and Category")

region = st.selectbox(
    "Select Region",
    sorted(df["Region"].unique())
)

category = st.selectbox(
    "Select Category",
    sorted(df["Category"].unique())
)

filtered = df[
    (df["Region"] == region) &
    (df["Category"] == category)
]

fig3 = px.bar(
    filtered.groupby("Sub-Category")["Sales"].sum().reset_index(),
    x="Sub-Category",
    y="Sales",
    color="Sub-Category",
    title=f"{category} Sales in {region}"
)

st.plotly_chart(fig3, use_container_width=True)
