import streamlit as st

# Configurar o layout para "wide"
st.set_page_config(layout="wide")

st.write('testeeeee')
contador=0
if st.button("se gostou da um joinhao"):
    contador = +1
    
st.write(contador)
