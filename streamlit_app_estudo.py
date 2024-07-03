import streamlit as st
import time
import numpy as np
import pandas as pd

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
    x_data = list(range(61))
    y_data = [None] * 61  # Inicializar com Nones

    # Desenhar o gráfico inicial com limites fixos
    initial_data = pd.DataFrame({
        'x': x_data,
        'y': y_data
    })
    chart = chart_placeholder.line_chart(initial_data.set_index('x'))

    for i in range(61):
        st.session_state['contador'] = i
        placeholder.write(f"vc clicou esse tanto {st.session_state['contador']}")
        
        # Atualizar dados do gráfico
        y_data[i] = np.random.rand()  # Adicionar valor aleatório
        
        # Criar gráfico usando pandas e Streamlit
        data = pd.DataFrame({
            'x': x_data,
            'y': y_data
        })
        chart.line_chart(data.set_index('x'))
        
        time.sleep(interval)
        
        if st.session_state['contador'] >= 60:
            break

# Botão para iniciar o incremento do contador
if st.button("clica"):
    incrementar_contador(seconds)

# Exibir valor atual do contador
st.write(f"show")
