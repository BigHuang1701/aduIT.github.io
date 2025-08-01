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

    st.success("✅ Loaded data from 'customer_data.csv'")
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    # Tabs for individual charts
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📌 Satisfaction Level",
        "👤 Age Distribution",
        "💸 Income vs Spending",
        "🔥 Correlation Heatmap",
        "📈 Age vs Spending (Gender)"
    ])

    with tab1:
        if "SatisfactionLevel" in df.columns:
            st.header("Distribution of Satisfaction Level")
            fig, ax = plt.subplots()
            sns.histplot(df["SatisfactionLevel"], kde=True, ax=ax, color="skyblue")
            ax.set_title("Distribution of Satisfaction Level")
            st.pyplot(fig)
        else:
            st.warning("Column 'SatisfactionLevel' not found.")

    with tab2:
        if "Age" in df.columns:
            st.header("Age Distribution")
            fig, ax = plt.subplots()
            sns.histplot(df["Age"], kde=True, ax=ax, color="orange")
            ax.set_title("Distribution of Age")
            st.pyplot(fig)
        else:
            st.warning("Column 'Age' not found.")

    with tab3:
        if "AnnualIncome" in df.columns and "SpendingScore" in df.columns:
            st.header("Annual Income vs Spending Score")
            fig, ax = plt.subplots()
            sns.scatterplot(data=df, x="AnnualIncome", y="SpendingScore", ax=ax, color="green")
            ax.set_title("Income vs Spending")
            st.pyplot(fig)
        else:
            st.warning("Columns 'AnnualIncome' or 'SpendingScore' not found.")

    with tab4:
        st.header("Correlation Heatmap")
        fig, ax = plt.subplots()
        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
        ax.set_title("Correlation between Numerical Features")
        st.pyplot(fig)

    with tab5:
        if "Age" in df.columns and "SpendingScore" in df.columns and "Gender" in df.columns:
            st.header("Age vs Spending Score (Colored by Gender)")
            fig, ax = plt.subplots()
            sns.scatterplot(data=df, x="Age", y="SpendingScore", hue="Gender", ax=ax)
            ax.set_title("Age vs Spending by Gender")
            st.pyplot(fig)
        else:
            st.warning("Columns 'Age', 'SpendingScore' or 'Gender' not found.")
