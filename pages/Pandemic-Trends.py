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
end_date = pd.to_datetime('today').strftime('%Y-%m-%d')
selected_data = full_df[(full_df['Date'] >= start_date) & (full_df['Date'] <= end_date)]

# Allow the user to select the month and year
selected_date = st.date_input('Select a date', value=pd.to_datetime('today'), min_value=pd.to_datetime('2018-01-01'), max_value=pd.to_datetime('today'))

# Filter DataFrame based on selected month and year
selected_data = selected_data[selected_data['Date'] <= selected_date]

# Plot CPI
plt.figure(figsize=(10, 6))
plt.plot(selected_data['Date'], selected_data['CPI'], marker='o')
plt.xlabel('Date')
plt.ylabel('CPI')
plt.title('Consumer Price Index (CPI)')
plt.xticks(rotation=45)
plt.grid(True)

# Display the plot
st.pyplot(plt)




st.header("Future Research on Predictors of Recessions....")