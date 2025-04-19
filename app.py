import streamlit as st
from datetime import datetime, timedelta
import time
import random

st.set_page_config(page_title="Blaze Padrões com IA", layout="centered")

st.title("Análise Automática - Blaze Double")

# Estilização
st.markdown(
    """
    <style>
        .big-font {
            font-size:24px !important;
        }
        .status-box {
            background-color: #4a4a4a;
            padding: 10px;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Simula uma análise baseada em padrões (substituir com lógica real depois)
def analisar():
    st.subheader("Diagnóstico do Mercado Atual")

    risco = random.choice(["BAIXO", "MÉDIO", "ALTO"])
    mercado_bom = "✅ SIM" if risco in ["BAIXO", "MÉDIO"] else "❌ NÃO"
    prob_branco = random.choice(["BAIXA", "MÉDIA", "ALTA", "DESCONHECIDA"])

    if risco == "ALTO":
        st.warning("ATENÇÃO: Mercado com ALTO risco de LOS!")
    else:
        st.success("Mercado estável para operações.")

    st.markdown(f"""
        - **Mercado Bom para Operar?** {mercado_bom}  
        - **Risco de LOS:** `{risco}`  
        - **Probabilidade de Branco:** `{prob_branco}`  
    """)

    st.subheader("Entradas Estratégicas para os Próximos 20 Minutos")

    hora_atual = datetime.utcnow() - timedelta(hours=3)  # Ajustado para horário de Brasília
    for i in range(20):
        horario = (hora_atual + timedelta(minutes=i)).strftime("%H:%M")
        cor = random.choice(["PRETO", "VERMELHO"])
        estrategia = f"{horario} → **{cor}** | Estratégia com base nos últimos padrões"
        st.markdown(f"- {estrategia}")

# Interface principal
st.info("Clique no botão abaixo para atualizar a análise com base no histórico atual.")

if st.button("Atualizar Análise"):
    with st.spinner("Analisando padrões do mercado..."):
        analisar()
        time.sleep(1)
