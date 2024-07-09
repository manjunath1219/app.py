###  Import the libraries  ###

import pandas as pd
import numpy as np
import streamlit as st

### Step 1: Loading the Data

st.file_uploader("Upload your input file", type=["csv"], key="uploaded_file")
data = pd.read_table(st.session_state["uploaded_file"] , sep=",", header=0)
st.dataframe(data)

### Step 2: Data Cleaning
missing_values = data.isnull().sum()
print(missing_values)

# Drop rows with missing values or fill them with appropriate values

data.duplicated().sum()

# Convert 'Date' column to datetime type
data['Date'] = pd.to_datetime(data['Date'])

# Display cleaned data
data.columns

### Step 3: Exploratory Data Analysis (EDA)

# Summary statistics
summary_stats = data.describe()
print(summary_stats)

# Group by Category and calculate total sales
category_sales = data.groupby('Product Category').agg({'Units Sold': 'sum', 'Unit Price': 'mean'}).reset_index()
print(category_sales)

# Calculate total revenue
data['Revenue'] = data['Unit Price'] * data['Units Sold']
total_revenue = data['Revenue'].sum()
print(f"Total Revenue: ${total_revenue}")

# Monthly sales trend
monthly_sales = data.set_index('Date').resample('M').agg({'Units Sold': 'sum', 'Revenue': 'sum'}).reset_index()
print(monthly_sales)

### Step 4: Statistical Analysis

# Correlation between Price and Quantity Sold
correlation = data['Unit Price'].corr(data['Units Sold'])
print(f"Correlation between Price and Units Sold: {correlation}")

# Average revenue per product category
avg_revenue_per_category = data.groupby('Product Category')['Revenue'].mean()
print(avg_revenue_per_category)

######  Deploying the model  ######

# Display the data
st.title('Reading the Data')
st.dataframe(data)

# Display the Missing Values
st.title('Missing Values')
st.dataframe(missing_values)

# Display the Summary statistics like mean, median etc
st.title('Summary statistics')
st.dataframe(summary_stats)

# Display the Group by Category and calculate total sales
st.title('Group by Category and calculate total sales')
st.dataframe(category_sales)

# Display the Total revenue
st.title('Calculate total revenue')
st.text(total_revenue)

# Display the Monthly sales trend
st.title('Monthly sales trend')
st.dataframe(monthly_sales)

# Display the Correlation between Price and Quantity Sold
st.title('Correlation between Price and Quantity Sold')
st.text( correlation)

# Display the Average revenue per product category
st.title('Average revenue per product category')
st.dataframe(avg_revenue_per_category)

# Display the Barplot of Sales by category
st.title('Barplot of Sales by category')
st.bar_chart(category_sales, x='Product Category', y='Units Sold')

# Display the Lineplot of Monthly sales trend
st.title('Lineplot of Monthly sales trend')
st.line_chart(monthly_sales, x='Date', y='Units Sold' )

# Display the Revenu Distribution
st.title('Revenu Distribution')
st.bar_chart(data['Revenue'], width=700, height=500)




