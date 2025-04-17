import streamlit as st
from PIL import Image
import numpy as np
import cv2
from collections import Counter
import datetime

st.set_page_config(page_title="Analisador Blaze Double", layout="centered")

st.title("Analisador de Padrões - Blaze Double")
st.markdown("Faça upload de um print do histórico da Blaze para previsão das próximas jogadas.")

uploaded_file = st.file_uploader("Envie o print do histórico da Blaze", type=["png", "jpg", "jpeg"])

# Função para identificar a cor dominante de cada bolinha
def identificar_cores(img):
    img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    altura, largura, _ = img_cv.shape

    bolinhas = []
    step_x = largura // 20  # aprox. 20 bolinhas por linha

    for i in range(20):
        x = i * step_x + step_x // 2
        y = altura // 2

        if x >= largura:
            break

        cor_bgr = img_cv[y, x]
        cor_rgb = tuple(int(c) for c in cor_bgr[::-1])

        if cor_rgb[0] > 200 and cor_rgb[1] < 80 and cor_rgb[2] < 80:
            bolinhas.append("vermelho")
        elif cor_rgb[0] < 100 and cor_rgb[1] < 100 and cor_rgb[2] < 100:
            bolinhas.append("preto")
        elif cor_rgb[0] > 200 and cor_rgb[1] > 200 and cor_rgb[2] > 200:
            bolinhas.append("branco")
        else:
            bolinhas.append("indefinido")

    return bolinhas

# Lógica para prever próximas jogadas
def prever_jogadas(sequencia, minutos=10):
    entradas = minutos * 2
    contagem = Counter(sequencia)
    total = sum(contagem.values())
    probabilidades = {cor: round((qtd / total) * 100, 2) for cor, qtd in contagem.items()}

    cor_mais_frequente = max(probabilidades, key=probabilidades.get)
    previsao = [cor_mais_frequente] * entradas

    return previsao, probabilidades

if uploaded_file:
    imagem = Image.open(uploaded_file)
    st.image(imagem, caption="Imagem enviada", use_column_width=True)

    st.write("Analisando a imagem...")

    cores_identificadas = identificar_cores(imagem)
    st.write("Sequência detectada:")
    st.write(cores_identificadas)

    op_min = st.slider("Quantos minutos você quer prever?", 5, 20, 10)
    previsao, probabilidades = prever_jogadas([c for c in cores_identificadas if c != "indefinido"], op_min)

    st.subheader("Previsão para os próximos minutos:")
    st.write(previsao)

    st.subheader("Probabilidades atuais com base no histórico:")
    st.write(probabilidades)
