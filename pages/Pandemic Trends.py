import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from datetime import datetime, timedelta

full_df = pd.read_csv("full_data.csv")
full_df['Date'] = pd.to_datetime(full_df['Date'])

st.title("Trends during the COVID-19 pandemic")
st.write("A closer look at CPI shows the sudden growth of inflation as well as the sudden shock to GDP growth when the pandemic hit. The spike back up in GDP comes from the burst of government spending.")

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

st.divider()

# Calculate GDP / Nominal growth percentage
full_df['gdp_growth'] = full_df['GDP'].pct_change() * 100
full_df['nominal_growth'] = full_df['Nominal GDP'].pct_change() * 100

# Create a new object
change_df = full_df[['Date', 'gdp_growth', 'nominal_growth']]

# Filter the DataFrame for data from 2018 to present
change_df = change_df[change_df['Date'] >= '2018-01-01']


fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.plot(change_df['Date'], change_df['gdp_growth'], label='Real GDP Change')
ax2.plot(change_df['Date'], change_df['nominal_growth'], label='Nominal GDP Change')
ax2.set_xlabel('Date')
ax2.set_ylabel('Percentage Change')
ax2.set_title('GDP vs Nominal GDP Change (2018 - Present)')
ax2.legend()
ax2.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(fig2)


st.link_button("FRED data: CPI", "https://fred.stlouisfed.org/series/CPIAUCSL")