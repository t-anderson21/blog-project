import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.graph_objects as go

# Read in dataset from GitHub
full_df = pd.read_csv("full_data.csv")
full_df['Date'] = pd.to_datetime(full_df['Date'])


st.title("Strength of Relationship between Indicators:")
st.write("A table used to identify and visualize patterns in the economic variables. A correlation value measures how closely two variables move together. The correlation coefficient can range from -1 to 1. If the correlation coefficient is closer to -1 or 1, it indicates a stronger positive or negative correlation between the variables. This allows insights into the extent to which changes in one variable correspond to changes in another, offering insights into potential cause-and-effect relationships.")
st.divider()

st.header('Correlation Matrix')

corr_matrix = full_df.drop(columns=['Date']).corr()

# Option to display heatmap
display_heatmap = st.checkbox("Display Heatmap")

if display_heatmap:
    # Create heatmap trace
    heatmap = go.Heatmap(z=corr_matrix.values,
                         x=corr_matrix.columns,
                         y=corr_matrix.columns,
                         colorscale='YlGnBu',
                         zmin=-1,
                         zmax=1)

    # Create layout
    layout = go.Layout(title='Correlation Matrix Heatmap')

    # Create figure
    fig = go.Figure(data=[heatmap], layout=layout)

    # Display the heatmap in Streamlit
    st.plotly_chart(fig)