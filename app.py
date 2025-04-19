import streamlit as st
from datetime import datetime, timedelta
import pytz
import random

st.set_page_config(page_title="Análise Blaze Double", layout="centered")
st.title("Análise Automática - Blaze Double")
st.subheader("Diagnóstico do Mercado Atual")

# Função simulada de diagnóstico
def diagnostico_do_mercado():
    risco = random.choice(["ALTO", "MODERADO", "BAIXO"])
    mercado_bom = risco == "BAIXO"
    return risco, mercado_bom

# Botão manual para atualizar
if st.button("Atualizar Análise"):
    risco, mercado_bom = diagnostico_do_mercado()

    if risco == "ALTO":
        st.warning("ATENÇÃO: Mercado com ALTO risco de LOS!")
    elif risco == "MODERADO":
        st.info("Mercado com risco MODERADO. Atenção redobrada.")
    else:
        st.success("Mercado com BAIXO risco. Bom momento para operar!")

    st.markdown(f"""
    - Mercado Bom para Operar? {'✅ SIM' if mercado_bom else '❌ NÃO'}
    - Risco de LOS: **{risco}**
    - Probabilidade de Branco: `DESCONHECIDA`
    """)

    st.subheader("Entradas Estratégicas para os Próximos 20 Minutos")

    # Horário de Brasília
    fuso_brasilia = pytz.timezone("America/Sao_Paulo")
    agora = datetime.now(fuso_brasilia)

    cores_possiveis = ["PRETO", "VERMELHO"]

    for i in range(20):
        horario = agora + timedelta(minutes=i)
        cor_sugerida = random.choice(cores_possiveis)
        estrategia = "Estratégia com base nos últimos padrões"
        st.markdown(f"**{horario.strftime('%H:%M')}** → **{cor_sugerida}** | {estrategia}")
else:
    st.info("Clique no botão acima para gerar a análise manualmente.")
