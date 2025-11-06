import streamlit as st

st.set_page_config(page_title="Manuais", page_icon="🟣")

# Logo
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("teste.png", width=300)  # Use PNG para evitar erro

# Título estilizado
st.markdown("""
<h2 style="
    color:#9B4DCC;
    font-family:'Montserrat',sans-serif;
    font-weight:700;
    text-align:center;
    border-bottom:2px solid #FFA500;
    padding-bottom:8px;
    margin-bottom:20px;">
📘 Manuais
</h2>
""", unsafe_allow_html=True)

st.markdown("**`Colaboradora: Patricia`**")

# Botões de download
st.markdown("### 📥 Baixe os Manuais:")

# Organizando em colunas para ficar bonito
col_a, col_b = st.columns(2)

# Primeira coluna
with col_a:
    with open("Apresentação conciliação5.ppsx", "rb") as file:
        st.download_button("📥 Conciliação", file, "Apresentacao_Conciliacao.ppsx",
                           mime="application/vnd.openxmlformats-officedocument.presentationml.slideshow")

    with open("contabilizacao_folha.ppsx", "rb") as file:
        st.download_button("📥 Contabilização de Folha", file, "Contabilizacao_Folha.ppsx",
                           mime="application/vnd.openxmlformats-officedocument.presentationml.slideshow")

    with open("Transacoes_contabeis.ppsx", "rb") as file:
        st.download_button("📥 Transações Contábeis", file, "Transacoes_Contabeis.ppsx",
                           mime="application/vnd.openxmlformats-officedocument.presentationml.slideshow")

# Segunda coluna
with col_b:
    with open("Proposta_pagamento.ppsx", "rb") as file:
        st.download_button("📥 Proposta de Pagamento", file, "Proposta_Pagamento.ppsx",
                           mime="application/vnd.openxmlformats-officedocument.presentationml.slideshow")

    with open("manual_criacao_miro.ppsx", "rb") as file:
        st.download_button("📥 Manual de Criação de Miro", file, "Manual_Criacao_Miro.ppsx",
                           mime="application/vnd.openxmlformats-officedocument.presentationml.slideshow")

    with open("entrada_importacao.ppsx", "rb") as file:
        st.download_button("📥 Entrada de Importação", file, "Entrada_Importacao.ppsx",
                           mime="application/vnd.openxmlformats-officedocument.presentationml.slideshow")
