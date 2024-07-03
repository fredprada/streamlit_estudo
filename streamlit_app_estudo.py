import streamlit as st
import time

# Configurar o layout para "wide"
st.set_page_config(layout="wide")

st.write('testeeeee')

seconds = st.selectbox('Segundos da animação', [5, 10, 20])

# # Botão para resetar contador
# if st.button('resetar'):
#     st.session_state['contador'] = 0

# Inicializar o contador no estado do Streamlit
if 'contador' not in st.session_state:
    st.session_state['contador'] = 0

# Função para incrementar o contador de 1 em 1 até 60, intervalado de acordo com `seconds`
def incrementar_contador(seconds):
    st.session_state['contador'] = 0
    placeholder = st.empty()
    interval = seconds / 60  # Intervalo de tempo em segundos para cada incremento
    for i in range(st.session_state['contador'], 61):
        st.session_state['contador'] = i
        placeholder.write(f"vc clicou esse tanto {st.session_state['contador']}")
        time.sleep(interval)
        # Utilize o placeholder para evitar st.experimental_rerun()
        if st.session_state['contador'] >= 60:
            break

# Botão para iniciar o incremento do contador
if st.button("clica"):
    incrementar_contador(seconds)
