import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import datetime, timedelta

# Read in dataset from GitHub
full_df = pd.read_csv("full_data.csv")
full_df['Date'] = pd.to_datetime(full_df['Date'])

st.title("Comparison of Nominal and Real GDP")
st.write("🎈 Nominal GDP measures current prices without adjusting for inflation 🎈")
st.write("🎈 Real GDP is inflation adjusted 🎈")
st.divider()

# Allow the user to select the duration of data to visualize
selected_duration = st.selectbox('Select duration', ['Last 20 years', 'Last 15 years', 'Last 10 years', 'Last 5 years', 'Last year' ])

# Calculate start date based on selected duration
end_date = datetime.now()
if selected_duration == 'Last year':
    start_date = end_date - timedelta(days=365)
elif selected_duration == 'Last 5 years':
    start_date = end_date - timedelta(days=365*5)
elif selected_duration == 'Last 10 years':
    start_date = end_date - timedelta(days=365*10)
elif selected_duration == 'Last 15 years':
    start_date = end_date - timedelta(days=365*15)
elif selected_duration == 'Last 20 years':
    start_date = end_date - timedelta(days=365*20)

# Filter DataFrame based on selected duration
selected_data = full_df[(full_df['Date'] >= start_date) & (full_df['Date'] <= end_date)]

# Plot Nominal GDP and GDP
plt.figure(figsize=(10, 6))
plt.plot(selected_data['Date'], selected_data['Nominal GDP'], label='Nominal GDP', marker='o')
plt.plot(selected_data['Date'], selected_data['GDP'], label='Real GDP', marker='o')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title(f'Nominal GDP vs Real GDP ({selected_duration})')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)

# Display the plot
st.pyplot(plt)

st.header("Comparison of Unemployment Rate and CIVPART")
st.write("🎈 CIVPART measures the percentage of the working-age population who are either employed or actively seeking employment 🎈")

# Allow the user to select the duration of data to visualize
CIVPART_duration = st.selectbox('Select years', ['20 years', '15 years', '10 years', '5 years', 'Past year'])

# Calculate start date based on selected duration
end_date = datetime.now()
if CIVPART_duration == 'Past year':
    begin_date = end_date - timedelta(days=365)
elif CIVPART_duration == '5 years':
    begin_date = end_date - timedelta(days=365*5)
elif CIVPART_duration == '10 years':
    begin_date = end_date - timedelta(days=365*10)
elif CIVPART_duration == '15 years':
    begin_date = end_date - timedelta(days=365*15)
elif CIVPART_duration == '20 years':
    begin_date = end_date - timedelta(days=365*20)

# Filter DataFrame based on selected duration
selected_data = full_df[(full_df['Date'] >= begin_date) & (full_df['Date'] <= end_date)]

# Plot Unemployment and CIVPART
plt.figure(figsize=(10, 6))
plt.plot(selected_data['Date'], selected_data['Unemployment Rate'], label='Unemployment', marker='o')
plt.plot(selected_data['Date'], selected_data['CIVPART'], label='CIVPART', marker='o')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title(f'Unemployment vs CIVPART ({CIVPART_duration})')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)

# Display the plot
st.pyplot(plt)

st.link_button("CIVPART data source", "https://fred.stlouisfed.org/series/CIVPART")