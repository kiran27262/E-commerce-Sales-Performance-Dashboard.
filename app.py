import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. CONFIGURATION AND LAYOUT ---
st.set_page_config(
    page_title="E-commerce Sales Insights Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. DATA LOADING AND CLEANING FUNCTION ---
@st.cache_data
def load_and_clean_data(file_path):
    # Load the data - IMPORTANT: CHANGE 'your_data.csv' to your actual file name
    df = pd.read_csv(file_path, encoding='latin1')

    # Basic Cleaning and Feature Engineering
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Date'] = df['InvoiceDate'].dt.date
    df['Month'] = df['InvoiceDate'].dt.to_period('M') 
    df['DayOfWeek'] = df.InvoiceDate.dt.day_name()
    
    # Calculate Revenue
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    
    # Clean: Drop rows with missing CustomerID and invalid transactions
    df.dropna(subset=['CustomerID'], inplace=True)
    df = df[df['Quantity'] > 0]
    df = df[df['UnitPrice'] > 0]

    return df

# --- 3. EXECUTE DATA LOAD ---
# *** REPLACE 'your_data.csv' HERE ***
DATA_FILE = 'sample_data.csv' 
try:
    df = load_and_clean_data(DATA_FILE)
except FileNotFoundError:
    st.error(f"Error: Could not find the file '{DATA_FILE}'. Please check the file name and path.")
    st.stop()
    
df['Date'] = df['Date'].astype(str)

# --- 4. DASHBOARD TITLE AND KPI METRICS ---

st.title("🛍️ E-commerce Sales Performance Dashboard")

# Calculate KPIs
total_revenue = df['Revenue'].sum()
total_sales = df['Quantity'].sum()
unique_customers = df['CustomerID'].nunique()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Revenue", value=f"₹{total_revenue:,.0f}")

with col2:
    st.metric(label="Total Units Sold", value=f"{total_sales:,}")

with col3:
    st.metric(label="Unique Customers", value=unique_customers)

st.markdown("---")


# --- 5. SIDEBAR FILTERS ---

st.sidebar.header("Filter Data")

# Filter 1: Top Products (e.g., top 10 products by total quantity)
top_products = df.groupby('Description')['Quantity'].sum().nlargest(10).index.tolist()
selected_products = st.sidebar.multiselect(
    "Select Products",
    options=top_products,
    default=top_products 
)

# Apply filters to a new DataFrame
df_filtered = df[
    (df['Description'].isin(selected_products))
]


# --- 6. VISUALIZATIONS ---

st.header("Sales Trend and Key Drivers")

# Row 1: Time Series Trend and Top Products
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Monthly Revenue Trend")
    
    # Group by month and sum the revenue for the line chart
    revenue_monthly = df_filtered.groupby('Month')['Revenue'].sum().reset_index()
    
    # 💥 FIX IS HERE: Convert the Period object to a string 💥
    revenue_monthly['Month'] = revenue_monthly['Month'].astype(str) 
    
    # Create interactive line chart
    fig_line = px.line(
        revenue_monthly,
        x='Month',
        y='Revenue',
        title='Total Revenue Over Time (Interactive)',
        markers=True
    )
    st.plotly_chart(fig_line, use_container_width=True)

with chart_col2:
    st.subheader("Top Selling Products (Units)")
    
    # Prepare product data
    product_performance = df_filtered.groupby('Description')['Quantity'].sum().nlargest(10).reset_index()
    
    # Create interactive bar chart
    fig_bar = px.bar(
        product_performance.sort_values(by='Quantity', ascending=True),
        x='Quantity',
        y='Description',
        orientation='h',
        title='Top 10 Products by Quantity Sold'
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# Row 2: Customer Behavior
st.subheader("Sales Activity by Day of Week")

# Prepare day of week data
day_revenue = df_filtered.groupby('DayOfWeek')['Revenue'].sum().reset_index()

# Define the correct order of the days
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_revenue['DayOfWeek'] = pd.Categorical(day_revenue['DayOfWeek'], categories=day_order, ordered=True)
day_revenue.sort_values('DayOfWeek', inplace=True)

# Create interactive pie chart
fig_pie = px.pie(
    day_revenue,
    names='DayOfWeek',
    values='Revenue',
    title='Revenue Distribution by Day of Week',
)

st.plotly_chart(fig_pie, use_container_width=True)
