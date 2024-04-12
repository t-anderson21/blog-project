import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title('Economic Indicator Trends')
st.caption("Data Project for my Stat 386 class")
st.divider()

#url = 'https://github.com/t-anderson21/blog-project/blob/main/full_data.csv' # update this...
#df = pd.read_csv(url)
full_df = pd.read_csv("full_data.csv")

#df.head()

full_df.head()



st.divider()
st.title('Correlation between _____')


# Make Correlation Table

# Merge CPI and unemployment DataFrames on the 'Date' column
merged_df = pd.merge(cpi_df, unemployment_df, on='Date')

# Calculate the correlation between CPI and unemployment rate
correlation = merged_df['CPI'].corr(merged_df['Unemployment Rate'])

print("Correlation between CPI and Unemployment Rate:", correlation)

st.divider()


# Create the correlation matrix
corr_matrix = full_df.corr()

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))

# Plot the heatmap
sns.heatmap(corr_matrix, annot=True, cmap='YlGnBu')

# Add title
plt.title('Correlation Matrix Heatmap')

# Display the heatmap
plt.show()