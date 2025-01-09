import streamlit as st 

text = st.text_input(label="Enter sometext")

if st.button(label="Show text"):
    st.write(text)