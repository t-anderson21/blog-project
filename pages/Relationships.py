import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Read in dataset from GitHub
full_df = pd.read_csv("full_data.csv")
full_df['Date'] = pd.to_datetime(full_df['Date'])


st.title("Strength of Relationship between Indicators:")
st.write("A table used to identify and visualize patterns in the economic variables")
st.divider()

st.write("A correlation value measures how closely two variables move together. The correlation coefficient ranges from -1 to 1. ")
st.write("If the correlation coefficient is closer to -1 or 1, it indicates a stronger positive or negative correlation between the variables. ")
st.header('Correlation Matrix')

## Display Correlation Matrix
corr_matrix = full_df.drop(columns=['Date']).corr()

# Option to display heatmap
display_heatmap = st.checkbox("Display Heatmap")

if display_heatmap:
    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # Plot the heatmap
    sns.heatmap(corr_matrix, annot=True, cmap='YlGnBu', ax=ax)

    # Add title
    ax.set_title('Correlation Matrix Heatmap')

    # Display the heatmap in Streamlit
    st.pyplot(fig)