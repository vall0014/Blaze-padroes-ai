import streamlit as st
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pytz

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

# Função de análise estratégica
def analisar_padrao(cores):
    if len(cores) < 1:
        return {
            "mercado_bom": False,
            "risco_los": "ALTO",
            "probabilidade_branco": "DESCONHECIDA"
        }

    ult_brancos = [i for i, c in enumerate(cores) if c == "branco"]
    branco_detectado = len(ult_brancos) > 0

    prob_sair_branco = "BAIXA"
    if len(cores) >= 2 and cores[-1] == "branco":
        prob_sair_branco = "MÉDIA"
        if cores[-2] == "branco":
            prob_sair_branco = "ALTA"

    return {
        "mercado_bom": branco_detectado,
        "risco_los": "MÉDIO" if branco_detectado else "ALTO",
        "probabilidade_branco": prob_sair_branco
    }

# Geração da próxima sequência de cores
def gerar_estrategia():
    fuso_brasilia = pytz.timezone("America/Sao_Paulo")
    agora = datetime.now(fuso_brasilia)

    cores = get_latest_colors()
    if isinstance(cores, str):
        return cores, None

    analise = analisar_padrao(cores)
    entradas = []

    for i in range(20):
        horario = (agora + timedelta(minutes=i)).strftime("%H:%M")
        if analise["probabilidade_branco"] == "ALTA":
            cor = "branco"
        elif len(cores) > 0 and cores[-1] == "preto":
            cor = "vermelho"
        else:
            cor = "preto"
        observacao = "Estratégia com base nos últimos padrões"
        entradas.append((horario, cor, observacao))

    return analise, entradas

# Streamlit UI
st.set_page_config(page_title="Blaze Padrões com IA", layout="wide")
st.title("Análise Automática - Blaze Double")

# Botão para atualizar as entradas
if st.button("Atualizar Estratégias Agora"):
    analise, entradas = gerar_estrategia()

    if isinstance(analise, str):
        st.error(analise)
    else:
        st.subheader("Diagnóstico do Mercado Atual")

        # ALERTA de risco
        if analise["risco_los"] == "ALTO":
            st.warning("ATENÇÃO: Mercado com ALTO risco de LOS!")
        elif analise["risco_los"] == "MÉDIO":
            st.info("Mercado com risco MÉDIO, cuidado nas entradas.")
        else:
            st.success("Mercado com baixo risco, bom momento para operar!")

        # ALERTA de branco
        if analise["probabilidade_branco"] == "ALTA":
            st.warning("ALERTA: Alta chance de BRANCO nas próximas jogadas!")
        elif analise["probabilidade_branco"] == "MÉDIA":
            st.info("Chance MÉDIA de branco. Fique atento.")

        st.markdown(f"""
        - **Mercado Bom para Operar?** {'✅ SIM' if analise['mercado_bom'] else '❌ NÃO'}
        - **Risco de LOS:** `{analise['risco_los']}`
        - **Probabilidade de Branco:** `{analise['probabilidade_branco']}`
        """)

        st.subheader("Entradas Estratégicas para os Próximos 20 Minutos")
        for h, cor, obs in entradas:
            st.write(f"**{h}** → **{cor.upper()}** | {obs}")
else:
    st.info("Clique no botão acima para gerar as estratégias atualizadas.")
