import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from datetime import datetime, timedelta

# Read in dataset from GitHub
full_df = pd.read_csv("full_data.csv")
full_df['Date'] = pd.to_datetime(full_df['Date'])

st.title("Comparison of Nominal & Real GDP")
st.write("Nominal GDP measures current prices without adjusting for inflation while real GDP is readjusted for inflation. Nominal means 'in name only' or that nominal GDP gauges the economic output of a country at current market prices. In contrast, real GDP offers a more nuanced perspective by adjusting for inflation, thereby providing a clearer picture of the true economic growth or contraction over time. By accounting for inflation, real GDP allows analysts and policymakers to discern underlying trends in economic performance, separate from the distortions caused by changes in price levels.")
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

st.link_button("GDP data", "https://fred.stlouisfed.org/series/GDPC1")
st.divider()

st.header("Comparison of Unemployment Rate &  CIVPART")
st.write("CIVPART measures the percentage of the working-age population who are employed or actively seeking a job. This indicator offers valuable insights into the dynamics of workforce participation, and has been in recent decline only made worse by the pandemic. Unemployment rate is the opposite metric and should always move opposite to CIVPART.")

# Allow the user to select the duration of data to visualize
CIVPART_duration = st.selectbox('Select years', ['20 years', '15 years', '10 years', '5 years', 'Past year'])

# Calculate start date based on selected duration
end_date = datetime.now()
if CIVPART_duration == 'Past year':
    begin_date = datetime(2023, 1, 1)
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
st.divider()


# Display max and min values for indicators
st.header("Maximum and Minimum Values for Indicators:")
indicators_max_min = full_df.drop(columns=['Date']).agg(['max', 'min'])
st.write(indicators_max_min)
st.divider()


st.link_button("CIVPART data", "https://fred.stlouisfed.org/series/CIVPART")
st.link_button("Unemployment Rate data", "https://fred.stlouisfed.org/series/UNRATE")