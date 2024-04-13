import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title('Economic Indicator Trends')
st.caption("Data Project for my Stat 386 class")
st.divider()

st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

#url = 'https://github.com/t-anderson21/blog-project/blob/main/full_data.csv' # update this...
#df = pd.read_csv(url)
full_df = pd.read_csv("full_data.csv")
full_df['Date'] = pd.to_datetime(full_df['Date'])

print(full_df.head())


st.title('Correlation between _____')


st.divider()


filtered_df = full_df[(full_df['Date'].dt.year >= 2019)]

# Create a line plot
plt.figure(figsize=(10, 6))
plt.plot(filtered_df['Date'], filtered_df['CIVPART'], marker='o', linestyle='-')
plt.title('CIVPART from 2019 to 2024')
plt.xlabel('Date')
plt.ylabel('CIVPART')
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()

# Display the plot using st.pyplot()
st.pyplot(plt)



# Allow user to select the variable
selected_variable = st.selectbox("Select Variable", ['CIVPART', 'CPI', 'GDP'])

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

