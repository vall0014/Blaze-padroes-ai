import streamlit as st
from datetime import datetime, timedelta
import random

def obter_ultimos_padroes():
    cores = ["vermelho", "preto", "branco"]
    return [random.choice(cores) for _ in range(30)]

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
    if len(cores) >= 1 and cores[-1] == "branco":
        prob_sair_branco = "MÉDIA"
    if len(cores) >= 2 and cores[-1] == "branco" and cores[-2] == "branco":
        prob_sair_branco = "ALTA"

    return {
        "mercado_bom": branco_detectado,
        "risco_los": "MÉDIO" if branco_detectado else "ALTO",
        "probabilidade_branco": prob_sair_branco
    }

def gerar_entradas():
    agora = datetime.now()
    entradas = []
    for i in range(20):
        minuto = agora + timedelta(minutes=i + 1)
        cor = "PRETO" if random.random() > 0.5 else "VERMELHO"
        entradas.append((minuto.strftime("%H:%M"), cor))
    return entradas

def main():
    st.set_page_config(page_title="Blaze Estratégias", layout="centered")
    st.title("Entradas Estratégicas para os Próximos 20 Minutos")

    cores = obter_ultimos_padroes()
    analise = analisar_padrao(cores)

    # Alerta de risco
    if analise["risco_los"] == "ALTO":
        st.warning("ATENÇÃO: Mercado com ALTO risco de LOS!")
    elif analise["risco_los"] == "MÉDIO":
        st.info("Mercado com risco MODERADO.")

    st.markdown(f"**Mercado Bom para Operar?** {'✅ SIM' if analise['mercado_bom'] else '❌ NÃO'}")
    st.markdown(f"**Risco de LOS:** `{analise['risco_los']}`")
    st.markdown(f"**Probabilidade de Branco:** `{analise['probabilidade_branco']}`")

    # Botão manual para atualizar
    if st.button("🔄 Atualizar Entradas"):
        st.session_state.entradas = gerar_entradas()

    if "entradas" not in st.session_state:
        st.session_state.entradas = gerar_entradas()

    st.subheader("Entradas Estratégicas para os Próximos 20 Minutos")
    for hora, cor in st.session_state.entradas:
        st.markdown(f"**{hora} → {cor}** | Estratégia com base nos últimos padrões")

if __name__ == "__main__":
    main()
