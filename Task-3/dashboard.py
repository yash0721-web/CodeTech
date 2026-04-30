import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Superstore Dashboard", layout="wide")

st.title("📊 Superstore Sales Dashboard")
st.markdown("Interactive Dashboard with Actionable Insights")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("Superstore.csv", encoding="latin1")
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("🔎 Filters")

region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

date_range = st.sidebar.date_input(
    "Select Date Range",
    [df["Order Date"].min(), df["Order Date"].max()]
)

# Apply Filters
filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category)) &
    (df["Order Date"] >= pd.to_datetime(date_range[0])) &
    (df["Order Date"] <= pd.to_datetime(date_range[1]))
]

# KPIs
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
col2.metric("📈 Total Profit", f"${total_profit:,.2f}")
col3.metric("🧾 Total Orders", total_orders)

# Sales by Category
st.subheader("Sales by Category")

category_sales = filtered_df.groupby("Category")["Sales"].sum().reset_index()

fig1 = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    color="Category",
    title="Category-wise Sales"
)

st.plotly_chart(fig1, use_container_width=True)

# Profit by Region
st.subheader("Profit by Region")

region_profit = filtered_df.groupby("Region")["Profit"].sum().reset_index()

fig2 = px.pie(
    region_profit,
    names="Region",
    values="Profit",
    title="Region-wise Profit Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

# Monthly Sales Trend
st.subheader("Monthly Sales Trend")

monthly_sales = filtered_df.groupby(
    filtered_df["Order Date"].dt.to_period("M")
)["Sales"].sum().reset_index()

monthly_sales["Order Date"] = monthly_sales["Order Date"].astype(str)

fig3 = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    title="Monthly Sales Trend"
)

st.plotly_chart(fig3, use_container_width=True)

# Top 10 Products
st.subheader("Top 10 Products by Sales")

top_products = (
    filtered_df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig4 = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Top 10 Products"
)

st.plotly_chart(fig4, use_container_width=True)

# Insights Section
st.subheader("📌 Actionable Insights")

st.markdown("""
- Identify high-sales but low-profit regions to reduce operational costs.
- Focus marketing efforts on top-performing categories.
- Improve inventory planning based on monthly sales trends.
- Promote top-selling products for maximum revenue growth.
""")
