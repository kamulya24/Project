import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("customer_data.csv")

# Title of the app
st.title("📊 Customer Data Segmentation")

# Dropdown to select the filtering criterion
option = st.selectbox(
    "🔍 Select a criterion to filter customers:",
    ("num_orders", "spent_amount", "installments", "age")
)

# Input field for the exact value
threshold = st.number_input(f"Enter an exact value for {option}:", min_value=0)

# Filter the dataset based on the exact match condition (== instead of >=)
filtered_df = df[df[option] == threshold]

# Display the results
st.write(f"### 📋 Showing customers where **{option}** is exactly **{threshold}**")
st.dataframe(filtered_df)

# Show basic statistics
st.write("### 📊 Dataset Overview:")
st.write(df.describe())

# Graphical representation of the filtered data
if not filtered_df.empty:
    st.write(f"### 🎨 Visual Representation of {option}:")
    
    # Create a Matplotlib figure
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Seaborn bar plot for better visualization
    sns.histplot(filtered_df[option], bins=10, kde=True, color="skyblue", ax=ax)
    
    # Labels and title
    ax.set_xlabel(option.capitalize(), fontsize=12)
    ax.set_ylabel("Count", fontsize=12)
    ax.set_title(f"Distribution of {option}", fontsize=14)
    
    # Display the plot in Streamlit
    st.pyplot(fig)
