import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Read in dataset from GitHub
full_df = pd.read_csv("full_data.csv")
full_df['Date'] = pd.to_datetime(full_df['Date'])


st.title("❄️ Correlation Matrix ❄️")
#st.markdown("❄️ Page 2 ❄️")
#st.sidebar.markdown("❄️ Page 2 ❄️")
st.divider()

st.header('Strength of Relationship between Indicators:')

## Display Correlation Matrix
corr_matrix = full_df.corr()

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