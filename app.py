import streamlit as st
import requests
from datetime import datetime, timedelta

st.set_page_config(page_title="Blaze Padrões com IA", layout="centered")

st.title("Padrões Blaze com IA")
st.markdown("**Uma análise inteligente de núcleos e padrões com base no histórico do Double.**")

# Botão de análise
if st.button("Analisar", type="primary"):
    try:
        # Pega o histórico do Double (últimas 100 jogadas)
        response = requests.get("https://blaze.com/api/roulette_games/recent")
        data = response.json()

        # Filtra apenas jogos do modo 'double'
        double_games = [j for j in data if j.get("game_type") == "double"]
        cores = []
        horarios = []

        for jogo in double_games:
            cor = jogo.get("color")  # 0=vermelho, 1=preto, 2=branco
            horario = datetime.fromisoformat(jogo.get("created_at").replace("Z", "+00:00")) - timedelta(hours=3)
            horarios.append(horario.strftime("%H:%M"))
            if cor == 0:
                cores.append("vermelho")
            elif cor == 1:
                cores.append("preto")
            else:
                cores.append("branco")

        # Exibe o histórico recente com horário
        st.subheader("Histórico recente com horário:")
        for i in range(len(cores)):
            st.markdown(f"**{horarios[i]}** → {cores[i]}")

        # Estratégia básica baseada em repetição simples
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
        st.error("Erro ao acessar o histórico da Blaze. Tente novamente em instantes.")
        st.code(str(e))
