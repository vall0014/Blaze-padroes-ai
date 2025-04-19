import streamlit as st
import random

# Função para simular os últimos resultados
def obter_ultimos_padroes():
    cores = ["vermelho", "preto", "branco"]
    return [random.choice(cores) for _ in range(30)]

# Função principal
def main():
    st.set_page_config(page_title="Teste de Cores Blaze", layout="centered")
    st.title("Últimos Resultados (Simulação)")

    cores = obter_ultimos_padroes()

    st.subheader("Últimos 30 resultados:")
    st.write(cores)

    st.subheader("Contagem de Cores:")
    vermelho_count = cores.count("vermelho")
    preto_count = cores.count("preto")
    branco_count = cores.count("branco")

    st.markdown(f"**Vermelho:** {vermelho_count}")
    st.markdown(f"**Preto:** {preto_count}")
    st.markdown(f"**Branco:** {branco_count}")

if __name__ == "__main__":
    main()
