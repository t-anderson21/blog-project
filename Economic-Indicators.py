import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import datetime, timedelta

st.title("Economic Indicator Trends")
#st.sidebar.markdown("Economic Indicator Trends")
st.caption("Project App Creation for Stat 386")
st.divider()

st.write("This app is designed to help explore my economic trends dataset")
st.write("I've included a few EDA insights I found interesting as well as .... ___")
st.write("Here is a link to my GitHub project folder:")
st.markdown("[Economic Trends Folder](https://github.com/t-anderson21/blog-project/tree/main)")


st.divider()
# Read in dataset from GitHub
full_df = pd.read_csv("full_data.csv")
full_df['Date'] = pd.to_datetime(full_df['Date'])

# filtered data for after 2019
filtered_df = full_df[(full_df['Date'].dt.year >= 2000)]


year = st.slider('Choose a year', 1948, 2023)
st.header(f'Top Indicators -- shift to page 2 ? {year}')
year_df = full_df[full_df['Date'].dt.year == year]
year_df['Date'] = year_df['Date'].dt.strftime('%Y-%m-%d')
year_df = year_df.round(2)
    
# Define a function to apply background gradient to columns
def background_gradient(df):
     return df.style.background_gradient(cmap='Blues')

# Display the head of the DataFrame with style shading the columns
st.dataframe(background_gradient(year_df))
#st.write(year_df)


st.divider()

# Allow user to select the variable
selected_variable = st.selectbox("Select Variable", ['GDP', 'CPI', 'CIVPART', 'Nominal GDP', 'Unemployment Rate'])


st.header(f'Trends of {selected_variable} since 2000')
st.caption("FRED data starts in 1945")

# Create a line plot based on the selected variable
plt.figure(figsize=(10, 6))
plt.plot(filtered_df['Date'], filtered_df[selected_variable], marker='o', linestyle='-')
plt.title(f'{selected_variable} from 2019 to 2024')
plt.xlabel('Date')
plt.ylabel(selected_variable)
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()

# Display the plot using st.pyplot()
st.pyplot(plt)



st.write('See more on Pages 2 and 3')
st.divider()
# Add Source button at the bottom
st.link_button("FRED data source", "https://fred.stlouisfed.org/series/CPIAUCSL")