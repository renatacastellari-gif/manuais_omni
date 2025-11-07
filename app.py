import streamlit as st

# Configuração da página
st.set_page_config(page_title="Conciliações dos Impostos", page_icon="🟪")

# Senha fixa
PASSWORD = "minhasenha123"

# Inicializa estado de login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 🔒 Esconde a barra lateral com CSS se não estiver logado
if not st.session_state.logged_in:
    hide_sidebar = """
        <style>
        [data-testid="stSidebar"] {display: none;}
        </style>
    """
    st.markdown(hide_sidebar, unsafe_allow_html=True)

# Se não estiver logado, pede senha
if not st.session_state.logged_in:
    st.markdown("<h2 style='text-align:center; color:#9B4DCC;'>🔒 Acesso Restrito</h2>", unsafe_allow_html=True)
    senha = st.text_input("Digite a senha:", type="password")
    if st.button("Entrar"):
        if senha == PASSWORD:
            st.session_state.logged_in = True
            st.success("✅ Acesso liberado! Agora você pode navegar pelas páginas.")
            st.rerun()
        else:
            st.error("❌ Senha incorreta.")
else:
    # 🔓 Conteúdo protegido
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image('teste.svg', width=300)

    st.markdown("""
    <h2 style='text-align:center; color:#FFA500 ; font-family:Montserrat; font-weight:700;'>
    📘 MANUAIS
    </h2>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='background-color:#f3f0fa; padding:20px; border-radius:10px;'>
        <h4 style='color:#6A1B9A;'>Guia de apoio para os colaboradores</h4>
        <p style='color:#333; font-size:16px;'>
        Seja bem-vindo(a) à Página de Manuais dos Colaboradores.<br><br>
        Este espaço foi criado para reunir os principais manuais, orientações e procedimentos que apoiam o dia a dia dos colaboradores.<br><br>
        Aqui você encontrará informações úteis sobre processos internos, ferramentas utilizadas, boas práticas e responsabilidades de cada área.<br><br>
        Nosso objetivo é facilitar o acesso ao conhecimento, promover autonomia e garantir que todos tenham os recursos necessários para desempenhar suas atividades com excelência.<br><br>
        Explore os conteúdos disponíveis e, em caso de dúvidas ou sugestões, entre em contato com o time responsável.
        </p>
    </div>
    """, unsafe_allow_html=True)

