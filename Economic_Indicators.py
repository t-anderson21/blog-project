import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.title("Economic Indicators Dashboard")
#st.sidebar.markdown("Economic Indicator Trends")
st.write("Project App Creation for Stat 386, by Talmage Anderson")
st.divider()

st.write("Welcome!")
st.write("This app is designed to help explore my economic trends dataset. I've included a few exploratory data analysis insights that I found interesting. You can interactively visualize the data, customize the time range, and analyze correlations between different economic indicators. My goal is to help the user visualize economic terms often heard on the news or social media. I hope it can help unravel the numbers driving the US economy.")

st.divider()
# Read in dataset from GitHub
full_df = pd.read_csv("full_data.csv")
full_df['Date'] = pd.to_datetime(full_df['Date'])

# filtered data for after 2019
filtered_df = full_df[(full_df['Date'].dt.year >= 2000)]

# Allow user to select the variable
selected_variable = st.selectbox("Select Variable", ['GDP', 'CPI', 'CIVPART', 'Nominal GDP', 'Unemployment Rate'])

st.header(f'Trends of {selected_variable} since 2000')
st.write("Above are the 5 indicators I've isolated for this dashboard to explore. By toggling between variables, users can uncover overarching trends and gain insights into the recent economic landscape. FRED data does start in 1945 but this plot only looks at the last 25 years because I wanted to focus on the 2009 recession and 2020 pandemic recession.")

# Create line plot using plotly.express
fig1 = px.line(filtered_df, x='Date', y=selected_variable,
              labels={'value': selected_variable, 'Date': 'Date'},
              title=f'{selected_variable} from 2019 to 2024')

# Show the plot
st.plotly_chart(fig1)


st.divider()

year = st.slider('Choose a year', 1950, 2023)

st.header(f'Top Economic Indicators for {year}')
st.write("The table provides an overview of key economic metrics for the selected year. The indicators included in the table highlight critical aspects of economic health and performance. By examining these indicators collectively, users can gain a better understanding of how the entire economy was doing during the specified year.")
    
# Filter DataFrame based on selected year
year_df = full_df[full_df['Date'].dt.year == year]
year_df['Date'] = year_df['Date'].dt.strftime('%Y-%m-%d')
year_df = year_df.round(2)

# Create an interactive table using Plotly graph objects
fig = go.Figure(data=[go.Table(
    header=dict(values=list(year_df.columns),
                fill_color='paleturquoise',
                align='center'),
    cells=dict(values=[year_df[col] for col in year_df.columns],
               fill_color='lavender',
               align='center'))
])

# Display the interactive table
st.plotly_chart(fig)

st.divider()
st.write('See more on Pages 2, 3, & 4')

# Add Source button at the bottom
st.link_button("Link to data source: FRED", "https://fred.stlouisfed.org")

st.divider()
st.write("Here is a link to my GitHub project folder to see data collection & general EDA:")
st.markdown("[Economic Trends Folder](https://github.com/t-anderson21/blog-project/tree/main)")