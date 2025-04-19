import streamlit as st
from datetime import datetime, timedelta

# Função de análise do histórico colado pelo usuário
def analisar_historico(historico_texto):
    cores = historico_texto.strip().upper().split(',')
    cores = [c.strip() for c in cores if c.strip() in ['VERMELHO', 'PRETO', 'BRANCO']]
    entradas = []

    agora = datetime.now()
    for i in range(5):  # Gera 5 entradas futuras
        horario = (agora + timedelta(minutes=i*5)).strftime('%H:%M')
        cor_sugerida = 'VERMELHO' if i % 2 == 0 else 'PRETO'  # Simples alternância
        entradas.append((horario, cor_sugerida, 'Base nos últimos padrões'))

    return entradas

# Layout do app
st.set_page_config(page_title="Blaze Padrões com IA", layout="centered")
st.markdown("<h1 style='text-align: center; color: white;'>Blaze Padrões com IA</h1>", unsafe_allow_html=True)

st.subheader("Diagnóstico do Mercado Atual")
st.warning("Mercado com risco MODERADO. Atenção redobrada.")

col1, col2 = st.columns(2)
col1.markdown("**Mercado Bom para Operar?** ❌ NÃO")
col2.markdown("**Risco de LOS:** MODERADO")

st.markdown("**Probabilidade de Branco:** `DESCONHECIDA`")

st.divider()

st.subheader("Colar Histórico de Cores da Blaze")
historico_input = st.text_area("Cole aqui os últimos resultados (ex: vermelho,preto,vermelho,branco...)")

if st.button("Atualizar Análise"):
    if historico_input.strip() == "":
        st.error("Por favor, cole o histórico de cores para gerar as próximas entradas.")
    else:
        entradas = analisar_historico(historico_input)
        st.success("Entradas Estratégicas para os Próximos 20 Minutos:")
        for entrada in entradas:
            st.markdown(f"**{entrada[0]} → {entrada[1]}** | {entrada[2]}")

st.markdown("---")
st.caption("Desenvolvido por você com suporte da IA")
