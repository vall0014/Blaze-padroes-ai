import streamlit as st
from collections import Counter

st.set_page_config(page_title="Analisador Manual - Blaze IA", layout="centered")
st.title("Analisador Manual de Padrões - Blaze (Double)")

st.markdown("Cole abaixo a sequência das últimas cores (ex: vermelho, preto, branco...)")

entrada = st.text_area("Cole aqui a sequência (separe por vírgula)", height=200)

def analisar(sequencia):
    contagem = Counter(sequencia[-100:])  # últimas 100
    total = sum(contagem.values())
    probabilidades = {cor: f"{(contagem[cor]/total)*100:.1f}%" for cor in contagem}

    ultimos_10 = sequencia[-10:]
    sugestao = Counter(ultimos_10).most_common(1)[0][0]

    # Análise de momento
    tendencia = ""
    if ultimos_10.count(sugestao) >= 5:
        tendencia = "Tendência forte detectada!"
    elif len(set(ultimos_10)) == 1:
        tendencia = "Cuidado: padrão fixo!"
    elif ultimos_10[-1] != sugestao:
        tendencia = "Possível reversão"
    else:
        tendencia = "Momento estável"

    # Previsões simples para próximas 3 jogadas
    previsoes = []
    for i in range(1, 4):
        base = sequencia[-(10+i):-i]
        if base:
            cor = Counter(base).most_common(1)[0][0]
            previsoes.append(cor)
        else:
            previsoes.append("indefinido")

    return sugestao, probabilidades, tendencia, previsoes

if entrada:
    lista = [i.strip().lower() for i in entrada.split(",") if i.strip().lower() in ["vermelho", "preto", "branco"]]

    if len(lista) < 10:
        st.warning("Digite ao menos 10 resultados para a IA analisar.")
    else:
        sugestao, probs, tendencia, futuras = analisar(lista)

        st.markdown("### Próxima sugestão de entrada:")
        st.success(f"**Cor sugerida:** `{sugestao.upper()}`")

        st.markdown("### Probabilidades das últimas 100 jogadas:")
        for cor, pct in probs.items():
            st.write(f"{cor.capitalize()}: {pct}")

        st.markdown("### Análise do Momento:")
        st.info(tendencia)

        st.markdown("### Previsão para próximas 3 entradas:")
        for i, cor in enumerate(futuras, 1):
            st.write(f"Entrada {i}: `{cor.upper()}`")
