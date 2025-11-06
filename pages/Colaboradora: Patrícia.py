import streamlit as st

st.set_page_config(page_title="Manual de Conciliação")

st.set_page_config(
    page_title="Manuais",
    page_icon="🟣",
)



col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("teste.svg", width=300)
    
# Título principal
st.markdown("""
<h2 style="
    color:#9B4DCC;
    font-family:'Montserrat',sans-serif;
    font-weight:700;
    text-align:center;
    border-bottom:2px solid #FFA500;
    padding-bottom:8px;
    margin-bottom:20px;">
📘Manuais
</h2>
""", unsafe_allow_html=True)

("""**`Colaboradora: Patricia`** """)



st.markdown("### 📥 Baixe o Manual:")
with open("Apresentação conciliação5.ppsx", "rb") as file:
    st.download_button(
        label="📥 Conciliação",
        data=file,
        file_name="Apresentação conciliação.ppsx",  # Nome correto
        mime="application/vnd.openxmlformats-officedocument.presentationml.slideshow"  # MIME para PPSX
    )

# segu
with open("contabilizacao_folha.ppsx", "rb") as file:
    st.download_button(
        label="📥 Contabilização de Folha",
        data=file,
        file_name="Contabilizacao_Folha.ppsx",
        mime="application/vnd.openxmlformats-officedocument.presentationml.slideshow"
    )
