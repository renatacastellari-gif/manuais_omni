import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Manuais",
    page_icon="🟣",
)

# Logo centralizado
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("teste.svg", width=300)


st.markdown("""
<h2 style="
    color:#FFFDD0;
    font-family:'Montserrat',sans-serif;
    font-weight:700;
    text-align:center;
    border-bottom:2px solid #FFA500;
    padding-bottom:8px;
    margin-bottom:20px;">
📘 Manuais
</h2>
""", unsafe_allow_html=True)


# Nome da colaboradora
st.markdown("**`Guia de apoio para os colaboradores`**")

# Introdução
st.markdown("""
###  Bem-vindo(a) à Página de Manuais dos Colaboradores

Este espaço foi criado para reunir os principais manuais, orientações e procedimentos que apoiam o dia a dia dos colaboradores.  
Aqui você encontrará informações úteis sobre processos internos, ferramentas utilizadas, boas práticas e responsabilidades de cada área.

Nosso objetivo é facilitar o acesso ao conhecimento, promover autonomia e garantir que todos tenham os recursos necessários para desempenhar suas atividades com excelência.

Explore os conteúdos disponíveis e, em caso de dúvidas ou sugestões, entre em contato com o time responsável.
""")
