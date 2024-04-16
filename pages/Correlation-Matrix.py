import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


st.title("❄️ Page 2 ❄️")
st.markdown("❄️ Page 2 ❄️")
st.sidebar.markdown("❄️ Page 2 ❄️")

# Read in dataset from GitHub
full_df = pd.read_csv("full_data.csv")
full_df['Date'] = pd.to_datetime(full_df['Date'])

st.divider()

st.header('Correlation Matrix')

## Display Correlation Matrix
corr_matrix = full_df.corr()

# Display the correlation matrix DataFrame
st.write("Strength of Relationship between Indicators:", corr_matrix)

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