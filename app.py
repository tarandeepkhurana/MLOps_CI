# app.py
import streamlit as st
from utils import square, cube, fifth_power

st.title("Power Calculator")
n = st.number_input("Enter an integer", value=1, step=1)

st.write(f"The square of {n} is: {square(n)}")
st.write(f"The cube of {n} is: {cube(n)}")
st.write(f"The fifth power of {n} is: {fifth_power(n)}")
