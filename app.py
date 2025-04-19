import streamlit as st
from historico import analisar_padroes

st.set_page_config(page_title="Blaze Padrões com IA", layout="centered")
st.title("Blaze Padrões com IA")
st.markdown("Analise inteligente de cores e padrões com base no histórico do Double.")

# Input manual do histórico
historico_input = st.text_area("Cole aqui o histórico recente do Double (ex: vermelho,preto,branco...)", height=150)

if st.button("Analisar"):
    if historico_input.strip() == "":
        st.warning("Por favor, cole o histórico para análise.")
    else:
        resultado = analisar_padroes(historico_input)
        st.success("Análise completa!")
        st.write(resultado)