import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import datetime, timedelta

full_df = pd.read_csv("full_data.csv")
full_df['Date'] = pd.to_datetime(full_df['Date'])

st.title("Trends during the COVID-19 pandemic")
st.write("_______")

# Allow the user to select the month and year
selected_month = st.selectbox('Select month', range(1, 13), index=11)  # Default to December
selected_year = st.selectbox('Select year', range(2018, 2023), index=4)  # Default to 2022

# Calculate start date based on selected month and year
start_date = datetime(selected_year, selected_month, 1)

# Calculate end date as 5 years from start date
end_date = start_date + timedelta(days=365*5)

# Filter DataFrame based on selected date range
selected_data = full_df[(full_df['Date'] >= start_date) & (full_df['Date'] <= end_date)]

# Plot CPI
plt.figure(figsize=(10, 6))
plt.bar(selected_data['Date'], selected_data['CPI'])
plt.xlabel('Date')
plt.ylabel('CPI')
plt.title(f'CPI Over the Last 5 Years (Starting from {start_date.strftime("%B %Y")})')
plt.xticks(rotation=45)
plt.grid(True)

# Display the plot
st.pyplot(plt)




st.header("Future Research on Predictors of Recessions....")