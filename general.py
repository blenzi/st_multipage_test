import streamlit as st


items = ['A', 'B', 'C']
st.session_state['item'] = items[0]

def select_item():
    index = items.index(st.session_state['item'])
    st.session_state['item'] = st.sidebar.selectbox('Select', items, index)
    return st.session_state['item']
