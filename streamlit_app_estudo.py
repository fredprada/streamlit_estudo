import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np

# Configurar o layout para "wide"
st.set_page_config(layout="wide")

st.write('testeeeee')

seconds = st.selectbox('Segundos da animação', [3, 5, 10, 15, 20, 30])

# Inicializar o contador no estado do Streamlit
if 'contador' not in st.session_state:
    st.session_state['contador'] = 0

# Função para incrementar o contador de 1 em 1 até 60, intervalado de acordo com `seconds`
def incrementar_contador(seconds):
    st.session_state['contador'] = 0
    placeholder = st.empty()
    chart_placeholder = st.empty()
    interval = seconds / 60  # Intervalo de tempo em segundos para cada incremento

    # Dados iniciais para o gráfico
    x_data = []
    y_data = []

    for i in range(61):
        st.session_state['contador'] = i
        placeholder.write(f"vc clicou esse tanto {st.session_state['contador']}")
        
        # Atualizar dados do gráfico
        x_data.append(i)
        y_data.append(np.random.rand())  # Adicionar valor aleatório

        # Criar gráfico
        fig, ax = plt.subplots()
        ax.plot(x_data, y_data, marker='o')
        ax.set_xlim(0, 60)
        ax.set_ylim(0, 1)

        # Exibir gráfico
        chart_placeholder.pyplot(fig)
        
        time.sleep(interval)
        
        if st.session_state['contador'] >= 60:
            break

# Botão para iniciar o incremento do contador
if st.button("clica"):
    incrementar_contador(seconds)

# Exibir valor atual do contador
st.write(f"vc clicou esse tanto {st.session_state['contador']}")
