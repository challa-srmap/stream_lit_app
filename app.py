import streamlit as st

st.write("""
# Largest of 3 Numbers

App finds the largest number of 3 User entered numbers
""")

st.header("User Input: Enter 3 numbers")

num1 = st.number_input("Number1:")
num2 = st.number_input("Number2:")
num3 = st.number_input("Number3:")


st.subheader("The Largest of the 3 Entered Numbers is:")
if num1>num2 and num1 > num1:
  st.write(num1)
elif num2>num1 and num2>num3:
  st.write(num2)
elif num3>num1 and num3>num2:
  st.write(num3)