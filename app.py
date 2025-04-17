import streamlit as st
from PIL import Image
import numpy as np
import cv2
import datetime

st.set_page_config(page_title="Analisador Blaze - Double", layout="centered")

st.title("Analisador de Padrões - Blaze Double com Imagem")

st.markdown(
    """
    Faça upload do print com o histórico de jogadas da Blaze (Double). O sistema vai analisar automaticamente as cores e prever as próximas entradas com maior probabilidade.
    """
)

# --- Função para detectar cor dominante de uma bolinha ---
def detectar_cor(bolinha):
    hsv = cv2.cvtColor(bolinha, cv2.COLOR_BGR2HSV)
    avg_color = np.average(hsv.reshape(-1, 3), axis=0)
    h, s, v = avg_color

    if s < 50 and v > 200:
        return "branco"
    elif h < 10 or h > 160:
        return "vermelho"
    elif 10 < h < 50:
        return "preto"
    else:
        return "indefinido"

# --- Função principal para processar imagem e extrair sequência ---
def processar_imagem(imagem):
    img = np.array(imagem)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    altura, largura, _ = img.shape
    bolinhas = []
    num_linhas = 7
    num_colunas = 10
    margem_sup = 90
    margem_esq = 90
    passo_x = (largura - 2 * margem_esq) // num_colunas
    passo_y = (altura - 2 * margem_sup) // num_linhas
    raio = 20

    for linha in range(num_linhas):
        for coluna in range(num_colunas):
            x = margem_esq + coluna * passo_x
            y = margem_sup + linha * passo_y
            bolinha = img[y - raio:y + raio, x - raio:x + raio]
            if bolinha.shape[0] == 0 or bolinha.shape[1] == 0:
                continue
            cor = detectar_cor(bolinha)
            bolinhas.append(cor)

    return bolinhas

# --- Função de previsão com base na sequência ---
def prever_proximas_cores(sequencia, minutos=10):
    ultimos = sequencia[-20:]
    contagem = {"vermelho": 0, "preto": 0, "branco": 0}
    for cor in ultimos:
        if cor in contagem:
            contagem[cor] += 1

    total = sum(contagem.values())
    if total == 0:
        return "Não foi possível prever"

    probabilidades = {cor: round((qtd / total) * 100, 2) for cor, qtd in contagem.items()}
    sugestao = max(probabilidades, key=probabilidades.get)

    return sugestao, probabilidades

# --- Upload da imagem ---
arquivo = st.file_uploader("Envie o print do histórico da Blaze", type=["png", "jpg", "jpeg"])

if arquivo:
    imagem = Image.open(arquivo)
    st.image(imagem, caption="Imagem recebida", use_column_width=True)

    with st.spinner("Analisando imagem..."):
        resultado = processar_imagem(imagem)
        st.success("Imagem processada com sucesso!")
        st.markdown("### Últimas cores detectadas:")
        st.code(", ".join(resultado[-30:]))

        sugestao, probabilidades = prever_proximas_cores(resultado)

        st.markdown("### Previsão para os próximos 10 minutos:")
        st.write(f"**Sugestão mais provável:** `{sugestao.upper()}`")
        st.write("**Probabilidades:**")
        st.json(probabilidades)
