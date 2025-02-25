
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("olist_customers_dataset.csv", encoding="utf-8")

# Streamlit UI
st.title("📊 E-Commerce Customer Data Analysis")

st.write("Displaying the first 10 rows of the customer dataset:")
st.dataframe(df.head(10))  # Display first 10 rows

# Show dataset summary
if st.button("Show Dataset Summary"):
    st.write(df.describe())

# Show unique customers count
if st.button("Show Unique Customers Count"):
    unique_customers = df["customer_unique_id"].nunique()
    st.write(f"Total Unique Customers: {unique_customers}")

# Search by customer ID
st.subheader("🔍 Search for a Customer by ID")
customer_id = st.text_input("Enter Customer ID:")

if customer_id:
    filtered_data = df[df["customer_id"] == customer_id]  # Filter dataset
    if not filtered_data.empty:
        st.write("📌 Customer Details:")
        st.dataframe(filtered_data)
    else:
        st.write("⚠️ No customer found with this ID.")

# 📊 Visualization Section
st.subheader("📊 Data Visualizations")

# 1️⃣ Customers per state
st.write("### 🗺️ Customers Distribution by State")
plt.figure(figsize=(10,5))
sns.countplot(data=df, x="customer_state", order=df["customer_state"].value_counts().index, palette="viridis")
plt.xticks(rotation=45)
plt.xlabel("State")
plt.ylabel("Number of Customers")
plt.title("Number of Customers per State")
st.pyplot(plt)

# 2️⃣ Zip Code Frequency
st.write("### 📍 Most Common Customer Zip Codes")
plt.figure(figsize=(10,5))
top_zipcodes = df["customer_zip_code_prefix"].value_counts().head(10)
sns.barplot(x=top_zipcodes.index, y=top_zipcodes.values, palette="mako")
plt.xlabel("Zip Code Prefix")
plt.ylabel("Number of Customers")
plt.title("Top 10 Most Common Customer Zip Codes")
st.pyplot(plt)

# 3️⃣ City-Wise Customer Distribution
st.write("### 🌆 Top 10 Cities with Most Customers")
plt.figure(figsize=(10,5))
top_cities = df["customer_city"].value_counts().head(10)
sns.barplot(x=top_cities.index, y=top_cities.values, palette="rocket")
plt.xticks(rotation=45)
plt.xlabel("City")
plt.ylabel("Number of Customers")
plt.title("Top 10 Cities with Most Customers")
st.pyplot(plt)
