import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from datetime import datetime, timedelta

full_df = pd.read_csv("full_data.csv")
full_df['Date'] = pd.to_datetime(full_df['Date'])

st.title("Trends during the COVID-19 pandemic")
st.write("_______")

# Filter data from 2018 to present
cpi_data = full_df[(full_df['Date'].dt.year >= 2018)]

# Create a line plot of CPI
plt.figure(figsize=(10, 6))
plt.plot(cpi_data['Date'], cpi_data['CPI'], marker='o', linestyle='-')
plt.title('CPI Trends (2018 - Present)')
plt.xlabel('Date')
plt.ylabel('CPI')
plt.grid(True)
plt.xticks(rotation=45)

# Display the plot
st.pyplot(plt)




st.header("Future Research on Predictors of Recessions....")

st.link_button("FRED data source", "https://fred.stlouisfed.org/series/CPIAUCSL")