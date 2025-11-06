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
    st.title("Acesso Restrito")
    senha = st.text_input("Digite a senha:", type="password")
    if st.button("Entrar"):
        if senha == PASSWORD:
            st.session_state.logged_in = True
            st.success("Acesso liberado! Agora você pode navegar pelas páginas.")
            st.rerun() # Recarrega a página para mostrar o menu
        else:
            st.error("Senha incorreta.")
else:
    # 🔒 Conteúdo protegido
    st.image('teste.svg', width=400) 
    st.title('Conciliações dos Impostos')
    ("""**`Competência: 09/2025`** """)
    st.write('💜 💜:purple_heart: 💜💜💜💜💜💜💜💜')

    st.markdown("""
    ## Seja bem vindo(a) à Página de Manuais dos Colaboradores
    

Este espaço foi criado para reunir os principais manuais, orientações e procedimentos que apoiam o dia a dia dos colaboradores.  
Aqui você encontrará informações úteis sobre processos internos, ferramentas utilizadas, boas práticas e responsabilidades de cada área.

Nosso objetivo é facilitar o acesso ao conhecimento, promover autonomia e garantir que todos tenham os recursos necessários para desempenhar suas atividades com excelência.

Explore os conteúdos disponíveis e, em caso de dúvidas ou sugestões, entre em contato com o time responsável.



            

                
             
 
""")

