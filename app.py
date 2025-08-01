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

    # --- Plot 1: Distribution of Customer Satisfaction ---
    if "CustomerSatisfaction" in df.columns:
        st.subheader("1️⃣ Distribution of Customer Satisfaction")
        fig1, ax1 = plt.subplots()
        sns.histplot(df["CustomerSatisfaction"], kde=True, ax=ax1, color='skyblue')
        st.pyplot(fig1)
        st.markdown("Biểu đồ này thể hiện mức độ hài lòng của khách hàng.")

    # --- Plot 2: Customer Age Distribution ---
    if "CustomerAge" in df.columns:
        st.subheader("2️⃣ Distribution of Customer Age")
        fig2, ax2 = plt.subplots()
        sns.histplot(df["CustomerAge"], bins=20, kde=True, ax=ax2, color='orange')
        st.pyplot(fig2)
        st.markdown("Biểu đồ này thể hiện phân bố độ tuổi khách hàng.")

    # --- Plot 3: Purchase Frequency by Age ---
    if "CustomerAge" in df.columns and "PurchaseFrequency" in df.columns:
        st.subheader("3️⃣ Age vs Purchase Frequency")
        fig3, ax3 = plt.subplots()
        if "CustomerGender" in df.columns:
            sns.scatterplot(data=df, x="CustomerAge", y="PurchaseFrequency", hue="CustomerGender", ax=ax3)
        else:
            sns.scatterplot(data=df, x="CustomerAge", y="PurchaseFrequency", ax=ax3)
        st.pyplot(fig3)
        st.markdown("Biểu đồ này thể hiện tần suất mua hàng theo độ tuổi và giới tính.")

    # --- Plot 4: Correlation Heatmap ---
    st.subheader("4️⃣ Correlation Heatmap")
    fig4, ax4 = plt.subplots()
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', ax=ax4)
    st.pyplot(fig4)
    st.markdown("Biểu đồ heatmap thể hiện mối tương quan giữa các biến số.")

    # --- Plot 5: Product Price vs Purchase Frequency ---
    if "ProductPrice" in df.columns and "PurchaseFrequency" in df.columns:
        st.subheader("5️⃣ Product Price vs Purchase Frequency")
        fig5, ax5 = plt.subplots()
        sns.scatterplot(data=df, x="ProductPrice", y="PurchaseFrequency", ax=ax5, color="green")
        st.pyplot(fig5)
        st.markdown("Biểu đồ này giúp nhận diện mối quan hệ giữa giá sản phẩm và tần suất mua hàng.")
