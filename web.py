import streamlit as st

st.title("My Personal Information")

name = st.text_input("Enter Your Name", "Type Here")
age = st.number_input("Enter Your Age", min_value=0, max_value=120, value=18)
gender = st.radio("What is your gender?", ("Male", "Female", "Other"))

if st.button("Submit"):
    result = "Name: " + name + ", Age: " + str(age) + ", Gender: " + gender
    st.success(result)
