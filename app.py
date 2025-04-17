import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Blaze Padrões com IA", layout="centered")

st.title("Padrões Blaze com IA")
st.markdown("**Uma análise inteligente de padrões com base no histórico recente do Double.**")

st.markdown("### Informe os últimos resultados (da direita pra esquerda, exemplo: preto, vermelho, vermelho, branco)")

input_text = st.text_input("Digite as cores separadas por vírgula").lower()

if st.button("Analisar"):
    try:
        cores = [cor.strip() for cor in input_text.split(",") if cor.strip() in ["vermelho", "preto", "branco"]]
        if not cores:
            st.warning("Insira ao menos uma cor válida (vermelho, preto ou branco).")
        else:
            st.markdown("#### Histórico recebido:")
            st.write(cores)

            ultima_cor = cores[0]
            contagem = cores.count(ultima_cor)

            st.markdown("---")
            st.subheader("Sugestão de entrada:")

            if ultima_cor == "vermelho":
                sugestao = "Preto"
            elif ultima_cor == "preto":
                sugestao = "Vermelho"
            else:
                sugestao = "Aguardar próximo resultado (saiu branco)"

            st.success(f"Com base no último resultado, a próxima cor sugerida é: **{sugestao}**")
    except Exception as e:
        st.error("Erro na análise. Verifique os dados inseridos.")
        st.code(str(e))import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Blaze Padrões com IA", layout="centered")

st.title("Padrões Blaze com IA")
st.markdown("**Uma análise inteligente de padrões com base no histórico recente do Double.**")

st.markdown("### Informe os últimos resultados (da direita pra esquerda, exemplo: preto, vermelho, vermelho, branco)")

input_text = st.text_input("Digite as cores separadas por vírgula").lower()

if st.button("Analisar"):
    try:
        cores = [cor.strip() for cor in input_text.split(",") if cor.strip() in ["vermelho", "preto", "branco"]]
        if not cores:
            st.warning("Insira ao menos uma cor válida (vermelho, preto ou branco).")
        else:
            st.markdown("#### Histórico recebido:")
            st.write(cores)

            ultima_cor = cores[0]
            contagem = cores.count(ultima_cor)

            st.markdown("---")
            st.subheader("Sugestão de entrada:")

            if ultima_cor == "vermelho":
                sugestao = "Preto"
            elif ultima_cor == "preto":
                sugestao = "Vermelho"
            else:
                sugestao = "Aguardar próximo resultado (saiu branco)"

            st.success(f"Com base no último resultado, a próxima cor sugerida é: **{sugestao}**")
    except Exception as e:
        st.error("Erro na análise. Verifique os dados inseridos.")
        st.code(str(e))import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Blaze Padrões com IA", layout="centered")

st.title("Padrões Blaze com IA")
st.markdown("**Uma análise inteligente de padrões com base no histórico recente do Double.**")

st.markdown("### Informe os últimos resultados (da direita pra esquerda, exemplo: preto, vermelho, vermelho, branco)")

input_text = st.text_input("Digite as cores separadas por vírgula").lower()

if st.button("Analisar"):
    try:
        cores = [cor.strip() for cor in input_text.split(",") if cor.strip() in ["vermelho", "preto", "branco"]]
        if not cores:
            st.warning("Insira ao menos uma cor válida (vermelho, preto ou branco).")
        else:
            st.markdown("#### Histórico recebido:")
            st.write(cores)

            ultima_cor = cores[0]
            contagem = cores.count(ultima_cor)

            st.markdown("---")
            st.subheader("Sugestão de entrada:")

            if ultima_cor == "vermelho":
                sugestao = "Preto"
            elif ultima_cor == "preto":
                sugestao = "Vermelho"
            else:
                sugestao = "Aguardar próximo resultado (saiu branco)"

            st.success(f"Com base no último resultado, a próxima cor sugerida é: **{sugestao}**")
    except Exception as e:
        st.error("Erro na análise. Verifique os dados inseridos.")
        st.code(str(e))
