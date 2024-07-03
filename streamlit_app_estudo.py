import streamlit as st
import time

# Configurar o layout para "wide"
st.set_page_config(layout="wide")

st.write('testeeeee')

# Inicializar o contador e o estado de execução no estado do Streamlit
if 'contador' not in st.session_state:
    st.session_state['contador'] = 0
if 'executando' not in st.session_state:
    st.session_state['executando'] = False

# Função para incrementar o contador de 1 em 1 até 60, intervalado em 0.1s
def incrementar_contador():
    placeholder = st.empty()
    while st.session_state['executando'] and st.session_state['contador'] < 60:
        st.session_state['contador'] += 1
        placeholder.write(f"vc clicou esse tanto {st.session_state['contador']}")
        time.sleep(0.5)
        st.experimental_rerun()  # Recarregar a página para atualizar a interface

# Botão para iniciar o incremento do contador
if st.button("clica"):
    st.session_state['executando'] = True
    incrementar_contador()

# Botão para parar o incremento do contador
if st.button("para"):
    st.session_state['executando'] = False

st.write(f"vc clicou esse tanto {st.session_state['contador']}")
