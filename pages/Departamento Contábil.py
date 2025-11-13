
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
📔
</h2>
""", unsafe_allow_html=True)
 
("""**`Departamento Contábil`** """)
 
 
st.markdown("### 📥 Baixe o Manual:")

# 📄 Download do PDF
with open("Untitled Tutorial.pdf", "rb") as file:
    st.download_button(
        label="📥 FB60 Lançamentos Impostos",
        data=file,
        file_name="FB60 Lançamentos Impostos.pdf",
        mime="application/pdf"
    )
