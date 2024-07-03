import streamlit as st

# Configurar o layout para "wide"
st.set_page_config(layout="wide")

st.write('testeeeee')

# Inicializar o contador no estado do Streamlit
if 'contador' not in st.session_state:
    st.session_state['contador'] = 0

# Botão para incrementar o contador
if st.button("Se gostou, dá um joinha!"):
    st.session_state['contador'] += 1

st.write(f"vc clicou esse tanto {st.session_state['contador']}")
