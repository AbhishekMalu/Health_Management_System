import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Create or load the DataFrame to store the data
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Year", "Sugar"])

# Streamlit app
st.title("Sugar Data Entry and Visualization")

# Data entry form
year = st.number_input("Year:", min_value=0, value=2023)
sugar = st.number_input("Sugar (g):", min_value=0)

if st.button("Add Data"):
    new_data = pd.DataFrame({"Year": [year], "Sugar": [sugar]})
    st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)

# Display the data table
st.subheader("Data Table")
st.write(st.session_state.data)

# Create and display the graph
st.subheader("Sugar Consumption Over Years")
plt.figure(figsize=(10, 6))
plt.plot(st.session_state.data["Year"], st.session_state.data["Sugar"], marker='o', linestyle='-')
plt.xlabel("Year")
plt.ylabel("Sugar (g)")
st.pyplot(plt)

# Save the data to a CSV file
if st.button("Save Data to CSV"):
    st.session_state.data.to_csv("sugar_data.csv", index=False)
    st.success("Data saved to sugar_data.csv")

# Load and display data from a CSV file
if st.button("Load Data from CSV"):
    loaded_data = pd.read_csv("sugar_data.csv")
    st.session_state.data = loaded_data
    st.write("Loaded Data:")
    st.write(loaded_data)
