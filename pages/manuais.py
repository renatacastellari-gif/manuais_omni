
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Manual de Conciliação", layout="wide")

st.title("📘 Manual Interativo de Conciliação")

# Seções do processo
sections = [
    "1. Relatório CORBIZ",
    "2. Importação no EQUALS",
    "3. Conciliação Manual",
    "4. Tratamento de divergências",
    "5. Exportação para SAP",
    "6. Conciliação SAP",
    "7. Identificação de formas de pagamento",
    "8. Conciliação cartões WEB"
]

selected_section = st.sidebar.selectbox("Escolha a etapa:", sections)

# Exibição de conteúdo por etapa
if selected_section == "1. Relatório CORBIZ":
    st.header("📄 Relatório CORBIZ")
    st.markdown("""
    - Acesse: **Reportes/Ventas/Reporte por tipo de pago**
    - Informe a data desejada
    - Exporte para Excel e salve em: `contabilidade/Patricia/Equals`
    """)
    uploaded_file = st.file_uploader("📤 Faça upload do relatório CORBIZ (Excel)", type=["xlsx"])
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        st.dataframe(df)

elif selected_section == "2. Importação no EQUALS":
    st.header("📥 Importação no EQUALS")
    st.markdown("""
    - Acesse o sistema EQUALS
    - Clique em “clique aqui” e selecione o arquivo salvo
    """)

elif selected_section == "3. Conciliação Manual":
    st.header("🔍 Conciliação Manual")
    st.markdown("""
    - Selecione vendas internas/transações de pagamento
    - Informe o período
    - Verifique pedidos não conciliados e formas de pagamento no CORBIZ
    """)

elif selected_section == "4. Tratamento de divergências":
    st.header("⚠️ Tratamento de Divergências")
    st.markdown("""
    - Enviar e-mail ao CEDIS para confirmação
    - Solicitar autorização para lançamento do saldo
    - Realizar lançamento no SAP com texto: `Crear saldo contra R$...` ou `Crear saldo a favor R$...`
    """)

elif selected_section == "5. Exportação para SAP":
    st.header("📤 Exportação para SAP")
    st.markdown("""
    - Acesse Integração > Remessa para Integração
    - Selecione “Contas a Receber”
    - Informe a data e gere o arquivo
    - Baixe o Excel e trate os dados conforme instruções
    """)

elif selected_section == "6. Conciliação SAP":
    st.header("🔄 Conciliação SAP")
    st.markdown("""
    - Transação FBL3N
    - Conta: 1000218
    - Layout: Brasil COBR
    - Filtrar por “Chv. Ref. 1”
    """)

elif selected_section == "7. Identificação de formas de pagamento":
    st.header("💳 Identificação de Formas de Pagamento")
    st.markdown("""
    - Criar colunas com fórmulas:
        - `=DIREITA(Nro. Filiação; 7)`
        - `=ESQUERDA(Adquirente; 1)`
        - `=CONCATENAR(...)`
    - Trocar “P” por “C” nos parcelados
    """)

elif selected_section == "8. Conciliação cartões WEB":
    st.header("🌐 Conciliação Cartões WEB")
    st.markdown("""
    - Excluir chaves “BBB” e “9207490”
    - Conta SAP: 1000620 e 1000219
    """)

---

### 📦 Próximo passo

Posso gerar o código completo do app com base nessa estrutura e incluir:
- Upload e tratamento de arquivos
- Exportação para Excel
- Visualizações interativas

