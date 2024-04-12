import pandas as pd
import plotly.express as px
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