import streamlit as st
from general import select_item


st.write("# Welcome to the first page!")

item = select_item()
st.write(f'Selected item: {item}')
