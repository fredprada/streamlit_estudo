import streamlit as st

# Configurar o layout para "wide"
st.set_page_config(layout="wide")

st.write('testeeeee')

st.button("Reset", type="primary")
if st.button("se gostou da um joinhao"):
    st.write("ai sim")
else:
    st.write("Goodbye")
