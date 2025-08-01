import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Customer Data Visualizer", layout="wide")

st.title("📊 Customer Data Analysis App")

# --- Upload CSV file ---
uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("🔍 Preview of Dataset")
    st.dataframe(df.head())

    # --- Plot 1: Distribution of Satisfaction Level ---
    if "SatisfactionLevel" in df.columns:
        st.subheader("1️⃣ Distribution of Satisfaction Level")
        fig1, ax1 = plt.subplots()
        sns.histplot(df["SatisfactionLevel"], kde=True, ax=ax1, color='skyblue')
        st.pyplot(fig1)
        st.markdown("This chart shows how customers are distributed in terms of satisfaction level.")

    # --- Plot 2: Age Distribution ---
    if "Age" in df.columns:
        st.subheader("2️⃣ Distribution of Age")
        fig2, ax2 = plt.subplots()
        sns.histplot(df["Age"], bins=20, kde=True, ax=ax2, color='orange')
        st.pyplot(fig2)
        st.markdown("This chart displays the age distribution of customers.")

    # --- Plot 3: Spending Score by Age ---
    if "Age" in df.columns and "SpendingScore" in df.columns:
        st.subheader("3️⃣ Age vs Spending Score")
        fig3, ax3 = plt.subplots()
        sns.scatterplot(data=df, x="Age", y="SpendingScore", hue="Gender", ax=ax3)
        st.pyplot(fig3)
        st.markdown("This scatter plot shows how spending score varies by age and gender.")

    # --- Plot 4: Correlation Heatmap ---
    st.subheader("4️⃣ Correlation Heatmap")
    fig4, ax4 = plt.subplots()
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', ax=ax4)
    st.pyplot(fig4)
    st.markdown("This heatmap displays the correlation between numerical features.")

    # --- Plot 5: Annual Income vs Spending Score ---
    if "AnnualIncome" in df.columns and "SpendingScore" in df.columns:
        st.subheader("5️⃣ Annual Income vs Spending Score")
        fig5, ax5 = plt.subplots()
        sns.scatterplot(data=df, x="AnnualIncome", y="SpendingScore", ax=ax5, color="green")
        st.pyplot(fig5)
        st.markdown("This chart helps identify the relationship between income and spending score.")
