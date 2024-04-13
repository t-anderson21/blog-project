import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title('Economic Indicator Trends')
st.caption("App Creation for my Stat 386 class")
st.divider()

st.sidebar.markdown("# Main page 🎈")
st.sidebar.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 3 🎉")

#url = 'https://github.com/t-anderson21/blog-project/blob/main/full_data.csv' # update this...
#df = pd.read_csv(url)
full_df = pd.read_csv("full_data.csv")
full_df['Date'] = pd.to_datetime(full_df['Date'])

# Define a function to apply background gradient to columns
def background_gradient(df):
    return df.style.background_gradient(cmap='Blues')

# Display the head of the DataFrame with style shading the columns
st.dataframe(background_gradient(full_df.tail()))

# filtered data for after 2019
filtered_df = full_df[(full_df['Date'].dt.year >= 2019)]


# add header of dataset on one of the pages??
print(full_df.head())

st.divider()




# Allow user to select the variable
selected_variable = st.selectbox("Select Variable", ['CIVPART', 'CPI', 'GDP', 'Nominal GDP', 'Unemployment Rate'])
st.header(f'Trends of {selected_variable} over the last 5 years')

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

st.divider()

st.header('Correlation Matrix')

## Display Correlation Matrix
corr_matrix = full_df.corr()

# Set up the matplotlib figure
# fig, ax = plt.subplots(figsize=(10, 8))

# Plot the heatmap
# sns.heatmap(corr_matrix, annot=True, cmap='YlGnBu', ax=ax)

# Add title
# ax.set_title('Correlation Matrix Heatmap')

# Display the heatmap in Streamlit
# st.pyplot(fig)

# Display the correlation matrix DataFrame
st.write("Correlation Matrix:", corr_matrix)

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









# Add Sources button at the bottom
