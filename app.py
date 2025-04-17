import streamlit as st
from PIL import Image
import numpy as np
import cv2
import io
import datetime
from collections import Counter

st.set_page_config(page_title="Analisador de Padrões - Blaze IA", layout="centered")
st.title("Analisador de Padrões - Blaze (Double) com IA")
st.markdown("Envie o print do histórico de cores (Double) da Blaze abaixo:")

uploaded_file = st.file_uploader("Envie o print (.png, .jpg ou .jpeg)", type=["png", "jpg", "jpeg"])

# Tolerâncias aproximadas de cor (BGR)
COLOR_RANGES = {
    "vermelho": ([0, 0, 130], [80, 80, 255]),
    "preto": ([0, 0, 0], [60, 60, 60]),
    "branco": ([200, 200, 200], [255, 255, 255])
}

def detect_color(bgr_pixel):
    for color, (lower, upper) in COLOR_RANGES.items():
        if all(lower[i] <= bgr_pixel[i] <= upper[i] for i in range(3)):
            return color
    return "indefinido"

def process_image(image):
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    h, w, _ = img.shape
    step_x = w // 13
    step_y = h // 15
    detected = []

    for y in range(3, h, step_y):
        for x in range(3, w, step_x):
            bgr = img[y, x]
            cor = detect_color(bgr)
            detected.append(cor)

    return detected

def analisar_padroes(sequencia):
    if not sequencia:
        return [], {}

    contagem = Counter(sequencia[-100:])  # últimas 100 jogadas
    total = sum(contagem.values())
    prob = {cor: f"{(contagem[cor] / total) * 100:.1f}%" for cor in contagem}

    # Previsão simples baseada nos últimos 10
    ultimos = sequencia[-10:]
    sugestao = Counter(ultimos).most_common(1)[0][0]

    return sugestao, prob

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Histórico recebido", use_column_width=True)

    st.write("Processando imagem...")
    resultado = process_image(image)

    # Limpa "indefinidos" do final
    resultado = [r for r in resultado if r in ["vermelho", "preto", "branco"]]

    if resultado:
        st.success(f"{len(resultado)} jogadas detectadas.")
        st.write("Sequência (mais antiga → mais recente):")
        st.code(", ".join(resultado), language="text")

        sugestao, probabilidades = analisar_padroes(resultado)
        st.markdown("### **Próxima sugestão de entrada:**")
        st.markdown(f"**Cor provável:** `{sugestao.upper()}`")

        st.markdown("### **Probabilidades nas últimas 100 jogadas:**")
        for cor, pct in probabilidades.items():
            st.write(f"{cor.capitalize()}: {pct}")

        agora = datetime.datetime.now().strftime("%H:%M:%S")
        st.caption(f"Última análise: {agora}")
    else:
        st.warning("Não foi possível detectar jogadas válidas na imagem.")
