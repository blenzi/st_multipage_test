import streamlit as st
from general import select_item


st.write("# Welcome to Streamlit! 👋")

item = select_item()
st.write(f'Selected item: {item}')
