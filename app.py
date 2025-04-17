import streamlit as st

# Função para identificar padrões simples
def analisar_padroes(sequencia):
    padroes = []
    for i in range(len(sequencia) - 2):
        trio = sequencia[i:i+3]
        if trio == ["vermelho", "vermelho", "preto"]:
            padroes.append((i, "Padrão: Vermelho, Vermelho, Preto"))
        elif trio == ["preto", "preto", "vermelho"]:
            padroes.append((i, "Padrão: Preto, Preto, Vermelho"))
        elif trio == ["vermelho", "vermelho", "vermelho"]:
            padroes.append((i, "3 Vermelhos seguidos"))
        elif trio == ["preto", "preto", "preto"]:
            padroes.append((i, "3 Pretos seguidos"))
        elif "branco" in trio:
            padroes.append((i, "Atenção: Branco detectado"))
    return padroes

# Interface do app
st.set_page_config(page_title="Blaze Padrões com IA", layout="centered")
st.title("Blaze Padrões com IA - Versão Manual")

st.write("Digite a sequência recente de cores do jogo Blaze Double.")
st.write("Exemplo: vermelho, preto, vermelho, branco, preto")

entrada = st.text_input("Sequência de cores (separadas por vírgula):")

if st.button("Analisar"):
    if entrada:
        cores = [cor.strip().lower() for cor in entrada.split(",")]
        padroes_encontrados = analisar_padroes(cores)

        if padroes_encontrados:
            st.subheader("Padrões encontrados:")
            for indice, padrao in padroes_encontrados:
                st.write(f"Posição {indice + 1}: {padrao}")
        else:
            st.info("Nenhum padrão detectado.")
    else:
        st.warning("Por favor, insira uma sequência de cores.")
