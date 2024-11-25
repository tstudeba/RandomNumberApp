import streamlit as st
import random

# Set the range
min_value = 1  
max_value = 1000  

# Add custom CSS for colors
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff; /* Light blue background */
        color: #333333; /* Dark gray text color */
    }
    .stButton>button {
        background-color: #4CAF50; /* Green button */
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #45a049; /* Darker green on hover */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit app
st.title("🎲 Random Number Generator")

# Display range
st.write(f"Generating a random number between **{min_value}** and **{max_value}**.")

# Button to generate a random number
if st.button("Generate"):
    random_number = random.randint(min_value, max_value)
    st.success(f"🎉 Random number: {random_number}")
    