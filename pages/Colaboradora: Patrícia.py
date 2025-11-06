import streamlit as st

# Configuração da página
st.set_page_config(page_title="Manuais", page_icon="🟣", layout="wide")

# Primeiro logo centralizado
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo_principal.svg", width=300)  # Substitua pelo nome do primeiro logo

# Segundo logo abaixo, também centralizado
col4, col5, col6 = st.columns([1, 2, 1])
with col5:
    st.image("logo_secundario.png", width=250)  # Substitua pelo nome do segundo logo

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

# Informações adicionais
st.markdown("**`Colaboradora: Patricia`**")

# Botões de download organizados
st.markdown("### 📥 Baixe os Manuais:")

# Linha com dois botões lado a lado
col_a, col_b = st.columns(2)

with col_a:
    with open("Apresentação conciliação5.ppsx", "rb") as file:
        st.download_button(
            label="📥 Conciliação",
            data=file,
            file_name="Apresentação conciliação.ppsx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.slideshow"
        )

with col_b:
    with open("contabilização de folha de pagamento.ppsx", "rb") as file:
        st.download_button(
            label="📥 Folha de Pagamento",
            data=file,
            file_name="contabilização_folha.ppsx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.slideshow"
        )

# Se quiser adicionar mais botões, repita o padrão acima
