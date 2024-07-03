import streamlit as st
import time

# Configurar o layout para "wide"
st.set_page_config(layout="wide")

st.write('testeeeee')

# Inicializar o contador no estado do Streamlit
if 'contador' not in st.session_state:
    st.session_state['contador'] = 0

# Função para incrementar o contador de 1 em 1 até 60, intervalado em 1s
def incrementar_contador():
    placeholder = st.empty()
    for i in range(st.session_state['contador'], 61):
        st.session_state['contador'] = i
        placeholder.write(f"vc clicou esse tanto {st.session_state['contador']}")
        time.sleep(1)
        # Utilize o placeholder para evitar st.experimental_rerun()
        if st.session_state['contador'] >= 60:
            break

# Botão para iniciar o incremento do contador
if st.button("clica"):
    incrementar_contador()

st.write(f"vc clicou esse tanto {st.session_state['contador']}")
