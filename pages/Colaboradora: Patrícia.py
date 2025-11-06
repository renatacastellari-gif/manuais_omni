import streamlit as st

st.set_page_config(page_title="Manuais", page_icon="🟣")

# Colunas para centralizar o primeiro logo
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("teste.svg", width=300)

# Adicionar outro logo abaixo (centralizado também)
col4, col5, col6 = st.columns([1, 2, 1])
with col5:
    st.image("logo2.png", width=250)  # Substitua pelo nome do segundo arquivo
