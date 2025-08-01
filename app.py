import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Customer Data Analyzer", layout="wide")

st.title("📊 Customer Data Analyzer with Tabs")

# 🔹 Đọc CSV mặc định từ local
csv_file_path = "consumer_electronics_sales_data.csv"

if not os.path.exists(csv_file_path):
    st.error("❌ File 'customer_data.csv' not found. Please place it in the same folder as this app.")
else:
    df = pd.read_csv(csv_file_path)

    st.success("✅ Loaded data from 'consumer_electronics_sales_data.csv' successfully!")
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    # Tabs for individual charts
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📌 Customer Satisfaction",
        "👤 Age Distribution",
        "💸 Price vs Purchase Frequency",
        "🔥 Correlation Heatmap",
        "📈 Age vs Purchase Frequency (Gender)"
    ])

    with tab1:
        if "CustomerSatisfaction" in df.columns:
            st.header("Distribution of Customer Satisfaction")
            fig, ax = plt.subplots()
            sns.histplot(df["CustomerSatisfaction"], kde=True, ax=ax, color="skyblue")
            ax.set_title("Distribution of Customer Satisfaction")
            st.pyplot(fig)
        else:
            st.warning("Column 'CustomerSatisfaction' not found.")

    with tab2:
        if "CustomerAge" in df.columns:
            st.header("Customer Age Distribution")
            fig, ax = plt.subplots()
            sns.histplot(df["CustomerAge"], kde=True, ax=ax, color="orange")
            ax.set_title("Distribution of Customer Age")
            st.pyplot(fig)
        else:
            st.warning("Column 'CustomerAge' not found.")

    with tab3:
        if "ProductPrice" in df.columns and "PurchaseFrequency" in df.columns:
            st.header("Product Price vs Purchase Frequency")
            fig, ax = plt.subplots()
            sns.scatterplot(data=df, x="ProductPrice", y="PurchaseFrequency", ax=ax, color="green")
            ax.set_title("Product Price vs Purchase Frequency")
            st.pyplot(fig)
        else:
            st.warning("Columns 'ProductPrice' or 'PurchaseFrequency' not found.")

    with tab4:
        st.header("Correlation Heatmap")
        fig, ax = plt.subplots()
        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
        ax.set_title("Correlation between Numerical Features")
        st.pyplot(fig)

    with tab5:
        if "CustomerAge" in df.columns and "PurchaseFrequency" in df.columns and "CustomerGender" in df.columns:
            st.header("Age vs Purchase Frequency (Colored by Gender)")
            fig, ax = plt.subplots()
            sns.scatterplot(data=df, x="CustomerAge", y="PurchaseFrequency", hue="CustomerGender", ax=ax)
            ax.set_title("Age vs Purchase Frequency by Gender")
            st.pyplot(fig)
        else:
            st.warning("Columns 'CustomerAge', 'PurchaseFrequency' or 'CustomerGender' not found.")
