import streamlit as st
import pandas as pd
import pygwalker as pyg

st.set_page_config(
    page_title='Biblioteca PygWalker',
    page_icon=':snake:',
    layout='wide',
    initial_sidebar_state='expanded',
)

df = pd.read_excel('CARROS.xlsx')

st.title('Biblioteca PygWalker')
st.subheader('Ferramenta de geração de gráfico')

pyg.walk(df, env='Streamlit', dark='dark')
