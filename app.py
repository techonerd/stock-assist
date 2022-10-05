import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(
    page_title="Stock Assist",
    page_icon="🔍",  # EP: how did they find a symbol?
    layout="wide",
    initial_sidebar_state="collapsed",
)
hide_st_style='''<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>'''
st.markdown(hide_st_style, unsafe_allow_html=True)
st.title('Predicting the Stocks Price')
st.markdown('Search your favourite stock and predict the price for the next 30 days')

# def search():
#     search = st.button("🔍")

c = st.container()
stock = c.text_input(label="stock_to_search", placeholder="Enter stock to search", label_visibility="hidden")
# if stock:
#     st.write("Searching for stock: ", stock)
