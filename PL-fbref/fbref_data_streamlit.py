# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 17:57:06 2023

@author: basus
"""

import streamlit as st
import pandas as pd
import numpy as np


st.write("Uber pickups in NYC")

DATA_URL = 'D:\Study\scrape-bs\\'

@st.cache_data
def load_data(stat):
    data = pd.read_csv(DATA_URL + stat)
    return data

def display_data(data):
    # Create a text element and let the reader know the data is loading.
    data_load_state = st.text('Loading data...')
    # Notify the reader that the data was successfully loaded
    data_load_state.text("Done! (using st.cache_data)")
    st.subheader('Raw data')
    st.dataframe(data,width = 1000)

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

col1 , col2 = st.columns([0.2,0.8])

with st.container():    
    with col1:    
        if st.button('Standard stats'#,on_click = click_button
                     ):    
            # Load 10,000 rows of data into the dataframe.
            data = load_data('standard.csv')
            with col2:
                display_data(data)
        if st.button('Keeper stats'#,on_click = click_button
                     ):
            # Load 10,000 rows of data into the dataframe.
            data = load_data('keeper.csv')
            with col2:
                display_data(data)
        if st.button('Passing stats'#,on_click = click_button
                     ):
            # Load 10,000 rows of data into the dataframe.
            data = load_data('Passing.csv')
            with col2:
                display_data(data)
        if st.button('Possession stats'#,on_click = click_button
                     ):
            # Load 10,000 rows of data into the dataframe.
            data = load_data('possession.csv')
            with col2:
                display_data(data)
        if st.button('Defense stats'#,on_click = click_button
                     ):
            # Load 10,000 rows of data into the dataframe.
            data = load_data('Defense.csv')
            with col2:
                display_data(data)
        if st.button('Shot creating actions stats'#,on_click = click_button
                     ):
            # Load 10,000 rows of data into the dataframe.
            data = load_data('gca.csv')
            with col2:
                display_data(data)
