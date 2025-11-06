import streamlit as st

st.set_page_config(page_title="Manual de Conciliação", layout="wide")

st.title("📘 Manual de Conciliação com Imagens")

st.markdown("### 📥 Baixe o arquivo original:")
with open("Apresentação conciliação5.ppsx", "rb") as file:
    st.download_button(
        label="📎 Baixar apresentação",
        data=file,
        file_name="Apresentação conciliação.ppsx",  # Nome correto
        mime="application/vnd.openxmlformats-officedocument.presentationml.slideshow"  # MIME para PPSX
    )

st.markdown("### 🖼️ Visualização dos slides:")
st.image("slide_01.png", caption="Slide 1 - Conciliação")
st.image("slide_02.png", caption="Slide 2 - Relatório CORBIZ")
