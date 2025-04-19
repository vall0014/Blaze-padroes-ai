import streamlit as st
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime, timedelta

# Função para puxar o histórico do TipMiner
def get_latest_colors():
    url = "https://www.tipminer.com/br/historico/blaze/double"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        result_divs = soup.select('.col-6.col-sm-3.col-md-2.col-xl.result-item .result-icon')

        cores = []
        for item in result_divs[:20]:  # Pegamos só os últimos 20 resultados
            if "white" in item["class"]:
                cores.append("branco")
            elif "red" in item["class"]:
                cores.append("vermelho")
            elif "black" in item["class"]:
                cores.append("preto")

        return cores[::-1]  # Inverter: da esquerda p/ direita
    except Exception as e:
        return f"Erro ao puxar dados: {e}"

# Função de análise estratégica simples (teste)
def analisar_padrao(cores):
    ult_brancos = [i for i, c in enumerate(cores) if c == "branco"]
    branco_detectado = len(ult_brancos) > 0

    prob_sair_branco = "BAIXA"
    if cores[-1] == "branco":
        prob_sair_branco = "MÉDIA"
        if cores[-2] == "branco":
            prob_sair_branco = "ALTA"

    return {
        "mercado_bom": branco_detectado,
        "risco_los": "MÉDIO" if branco_detectado else "ALTO",
        "probabilidade_branco": prob_sair_branco
    }

# Geração da próxima sequência de cores (teste inicial)
def gerar_estrategia():
    cores = get_latest_colors()
    if isinstance(cores, str):
        return cores, None

    analise = analisar_padrao(cores)
    agora = datetime.now()
    entradas = []

    for i in range(20):
        horario = (agora + timedelta(minutes=i)).strftime("%H:%M")
        if analise["probabilidade_branco"] == "ALTA":
            cor = "branco"
        elif cores[-1] == "preto":
            cor = "vermelho"
        else:
            cor = "preto"
        observacao = "Estratégia com base nos últimos padrões"
        entradas.append((horario, cor, observacao))

    return analise, entradas

# Streamlit UI
st.set_page_config(page_title="Blaze Padrões com IA", layout="wide")
st.title("Análise Automática - Blaze Double")

placeholder = st.empty()

while True:
    with placeholder.container():
        analise, entradas = gerar_estrategia()

        if isinstance(analise, str):
            st.error(analise)
        else:
            st.subheader("Diagnóstico do Mercado Atual")
            st.write(f"**Mercado Bom para Operar?** {'Sim' if analise['mercado_bom'] else 'Não'}")
            st.write(f"**Risco de LOS?** {analise['risco_los']}")
            st.write(f"**Probabilidade de Branco?** {analise['probabilidade_branco']}")

            st.subheader("Entradas Estratégicas para os Próximos 20 Minutos")
            for h, cor, obs in entradas:
                st.write(f"**{h}** → **{cor.upper()}** | {obs}")

    time.sleep(60)  # Atualiza a cada minuto
