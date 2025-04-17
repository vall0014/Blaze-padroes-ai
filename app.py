import streamlit as st
from PIL import Image
import numpy as np
import cv2
from collections import Counter

st.set_page_config(page_title="Analisador Blaze por Imagem", layout="centered")
st.title("Blaze Double - Análise de Padrões (por imagem)")

uploaded_file = st.file_uploader("Envie o print do histórico da Blaze (Double)", type=["png", "jpg", "jpeg"])

def detectar_cor(media_rgb):
    r, g, b = media_rgb
    if abs(r - g) < 30 and abs(g - b) < 30 and r > 200:
        return 'branco'
    elif r > 150 and g < 80 and b < 80:
        return 'vermelho'
    elif r < 80 and g < 80 and b < 80:
        return 'preto'
    else:
        return 'indefinido'

def analisar_padroes(sequencia):
    contagem = Counter(sequencia[-100:])
    total = sum(contagem.values())
    probabilidades = {cor: f"{(contagem[cor]/total)*100:.1f}%" for cor in contagem}

    ultimos_10 = sequencia[-10:]
    sugestao = Counter(ultimos_10).most_common(1)[0][0]

    tendencia = ""
    if ultimos_10.count(sugestao) >= 5:
        tendencia = "Tendência forte"
    elif len(set(ultimos_10)) == 1:
        tendencia = "Cuidado: padrão fixo"
    else:
        tendencia = "Momento estável"

    previsoes = []
    for i in range(1, 4):
        base = sequencia[-(10+i):-i]
        if base:
            cor = Counter(base).most_common(1)[0][0]
            previsoes.append(cor)
        else:
            previsoes.append("indefinido")

    return sugestao, probabilidades, tendencia, previsoes

if uploaded_file:
    st.image(uploaded_file, caption="Imagem enviada", use_column_width=True)
    image = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(image)
    img_cv = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

    height, width, _ = img_cv.shape
    linhas = 6
    colunas = 30
    cor_detectada = []

    largura_bolinha = width // colunas
    altura_bolinha = height // linhas

    for i in range(linhas):
        for j in range(colunas):
            x = j * largura_bolinha
            y = i * altura_bolinha
            bolinha = img_cv[y+10:y+altura_bolinha-10, x+10:x+largura_bolinha-10]
            media_bgr = cv2.mean(bolinha)[:3]
            media_rgb = media_bgr[::-1]
            cor = detectar_cor(media_rgb)
            cor_detectada.append(cor)

    cor_detectada = [c for c in cor_detectada if c in ['vermelho', 'preto', 'branco']]

    if len(cor_detectada) < 10:
        st.warning("Poucas cores detectadas. Verifique a imagem enviada.")
    else:
        st.markdown("### Cores detectadas:")
        st.write(', '.join(cor_detectada[-50:]))

        sugestao, probs, tendencia, futuras = analisar_padroes(cor_detectada)

        st.markdown("### Próxima sugestão:")
        st.success(f"**Cor sugerida:** `{sugestao.upper()}`")

        st.markdown("### Probabilidades nas últimas 100 jogadas:")
        for cor, pct in probs.items():
            st.write(f"{cor.capitalize()}: {pct}")

        st.markdown("### Análise do Momento:")
        st.info(tendencia)

        st.markdown("### Previsão para próximas 3 entradas:")
        for i, cor in enumerate(futuras, 1):
            st.write(f"Entrada {i}: `{cor.upper()}`")
