import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from datetime import datetime, timedelta
import plotly.graph_objects as go

full_df = pd.read_csv("full_data.csv")
full_df['Date'] = pd.to_datetime(full_df['Date'])

st.title("Trends during the COVID-19 pandemic")
st.write("A closer look at CPI shows the sudden growth of inflation as well as the sudden shock to GDP growth when the pandemic hit. The spike back up in GDP comes from the burst of government spending. I used import plotly.graph_objects to make the graphs downloadable.")

# Filter data from 2018 to present
cpi_data = full_df[(full_df['Date'].dt.year >= 2018)]

# Create a line plot of CPI with Plotly
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=cpi_data['Date'], y=cpi_data['CPI'], mode='lines+markers'))
fig1.update_layout(title='CPI Trends (2018 - Present)',
                  xaxis_title='Date',
                  yaxis_title='CPI',
                  xaxis=dict(tickangle=-45),
                  legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01))

# Display the plot in Streamlit
st.plotly_chart(fig1)

st.divider()

# Calculate GDP / Nominal growth percentage
full_df['gdp_growth'] = full_df['GDP'].pct_change() * 100
full_df['nominal_growth'] = full_df['Nominal GDP'].pct_change() * 100

# Create a new object
change_df = full_df[['Date', 'gdp_growth', 'nominal_growth']]

# Filter the DataFrame for data from 2018 to present
change_df = change_df[change_df['Date'] >= '2018-01-01']

# Create interactive line plot with Plotly
fig = go.Figure()

# Add Real GDP Change trace
fig.add_trace(go.Scatter(x=change_df['Date'], y=change_df['gdp_growth'], mode='lines', name='Real GDP Change'))

# Add Nominal GDP Change trace
fig.add_trace(go.Scatter(x=change_df['Date'], y=change_df['nominal_growth'], mode='lines', name='Nominal GDP Change'))

# Update layout
fig.update_layout(title='GDP vs Nominal GDP Change (2018 - Present)',
                  xaxis_title='Date',
                  yaxis_title='Percentage Change',
                  xaxis=dict(tickangle=-45),
                  legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01))

# Display the plot in Streamlit
st.plotly_chart(fig)


st.link_button("FRED data: CPI", "https://fred.stlouisfed.org/series/CPIAUCSL")