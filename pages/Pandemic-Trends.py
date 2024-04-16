import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from datetime import datetime, timedelta

full_df = pd.read_csv("full_data.csv")
full_df['Date'] = pd.to_datetime(full_df['Date'])

st.title("Trends during the COVID-19 pandemic")
st.write("_______")

# Filter DataFrame for data from 2018 to present
start_date = '2018-01-01'
end_date = pd.Timestamp.now().strftime('%Y-%m-%d')
selected_data = full_df[(full_df['Date'] >= start_date) & (full_df['Date'] <= end_date)]

# Allow the user to select the month
selected_month = st.slider('Select month', min_value=1, max_value=12, value=1)

# Filter DataFrame based on selected month
selected_data = selected_data[selected_data['Date'].dt.month == selected_month]

# Plot CPI
plt.figure(figsize=(10, 6))
plt.plot(selected_data['Date'], selected_data['CPI'], marker='o')
plt.xlabel('Date')
plt.ylabel('CPI')
plt.title(f'CPI from 2018 to Present (Month: {selected_month})')
plt.xticks(rotation=45)
plt.grid(True)

# Display the plot
st.pyplot(plt)




st.header("Future Research on Predictors of Recessions....")