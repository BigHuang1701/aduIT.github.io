import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Customer Data Analyzer", layout="wide")

st.title("📊 Customer Data Analyzer with Tabs")

# Upload file
uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

if uploaded_file:
    # Save uploaded CSV to a temporary location
    temp_file_path = os.path.join("uploaded_data.csv")
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Load the CSV
    df = pd.read_csv(temp_file_path)

    st.success("✅ File uploaded and saved as 'uploaded_data.csv'")
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    # Tabs for individual charts
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📌 Satisfaction Level",
        "👤 Age Distribution",
        "💸 Income vs Spending",
        "🔥 Correlation Heatmap",
        "📈 Age vs Spending (Gend
