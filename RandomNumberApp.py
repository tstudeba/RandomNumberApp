import streamlit as st
import random

st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff;
        color: #333333;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🎲 Random Number Generator")

# User inputs for range
st.subheader("Choose your range:")
min_value = st.number_input("Enter the minimum value:", value=1, step=1)
max_value = st.number_input("Enter the maximum value:", value=1000, step=1)

if min_value >= max_value:
    st.error("The minimum value must be less than the maximum value.")
else:
    if st.button("Generate"):
        random_number = random.randint(min_value, max_value)
        st.success(f"🎉 Random number: {random_number}")
