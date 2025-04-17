import streamlit as st

# Função para analisar padrões e sugerir próxima cor
def analisar_e_prever(sequencia):
    padroes = []
    proxima_cor = "Sem sugestão"

    for i in range(len(sequencia) - 2):
        trio = sequencia[i:i+3]
        if trio == ["vermelho", "vermelho", "preto"]:
            padroes.append(f"Detectado padrão: V-V-P na posição {i+1}")
        elif trio == ["preto", "preto", "vermelho"]:
            padroes.append(f"Detectado padrão: P-P-V na posição {i+1}")
        elif trio == ["vermelho", "vermelho", "vermelho"]:
            padroes.append(f"Detectado padrão: V-V-V na posição {i+1}")
        elif trio == ["preto", "preto", "preto"]:
            padroes.append(f"Detectado padrão: P-P-P na posição {i+1}")
        elif "branco" in trio:
            padroes.append(f"Aviso: Branco detectado na posição {i+1}")

    ultimos = sequencia[-3:]
    
    # Lógica para sugerir a próxima cor com base nos últimos 3
    if ultimos == ["vermelho", "vermelho", "preto"]:
        proxima_cor = "Sugestão: Jogar VERMELHO"
    elif ultimos == ["preto", "preto", "vermelho"]:
        proxima_cor = "Sugestão: Jogar PRETO"
    elif ultimos == ["vermelho", "vermelho", "vermelho"]:
        proxima_cor = "Sugestão: Jogar PRETO"
    elif ultimos == ["preto", "preto", "preto"]:
        proxima_cor = "Sugestão: Jogar VERMELHO"
    elif "branco" in ultimos:
        proxima_cor = "Sugestão: Jogar PRETO (após branco)"

    return padroes, proxima_cor

# Interface do app
st.set_page_config(page_title="Blaze Padrões com IA", layout="centered")
st.title("Blaze Padrões com IA - Versão Manual com Sugestão")

st.write("Digite a sequência recente de cores do jogo Blaze Double.")
st.write("Exemplo: vermelho, preto, vermelho, branco, preto")

entrada = st.text_input("Sequência de cores (separadas por vírgula):")

if st.button("Analisar"):
    if entrada:
        cores = [cor.strip().lower() for cor in entrada.split(",")]
        padroes, sugestao = analisar_e_prever(cores)

        if padroes:
            st.subheader("Padrões encontrados:")
            for p in padroes:
                st.write(f"- {p}")
        else:
            st.info("Nenhum padrão detectado.")

        st.subheader("Sugestão da próxima cor:")
        st.success(sugestao)

    else:
        st.warning("Por favor, insira uma sequência de cores.")
