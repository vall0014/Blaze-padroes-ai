import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

# Função para carregar o histórico
def carregar_historico():
    try:
        df = pd.read_csv("historico.csv")
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df
    except:
        return pd.DataFrame(columns=["timestamp", "cor"])

# Função para detectar padrão forte
def detectar_padroes(df):
    ultimos = df.tail(6)['cor'].tolist()
    if ultimos.count("branco") >= 2:
        return "evitar"
    if ultimos[-3:] == ["vermelho", "vermelho", "vermelho"]:
        return "preto"
    if ultimos[-3:] == ["preto", "preto", "preto"]:
        return "vermelho"
    return "neutro"

# Função de sugestão com limite de entradas
def sugerir_entradas(df):
    entradas = []
    limite = 10
    entrada = 0
    while entrada < limite:
        padrao = detectar_padroes(df)
        if padrao == "evitar":
            entradas.append(("Pular", "Horário ruim por muitos brancos"))
            df = df.iloc[1:]
            continue
        elif padrao in ["vermelho", "preto"]:
            horario = datetime.now() + timedelta(minutes=entrada)
            entradas.append((horario.strftime("%H:%M"), padrao.upper(), "Padrão detectado"))
            entrada += 1
        else:
            entradas.append(("Pular", "Sem padrão forte"))
            entrada += 1
        df = df.iloc[1:]
    return entradas

# Interface Streamlit
st.set_page_config(page_title="Blaze Padrões com IA", layout="centered")
st.title("Blaze Padrões com IA")
st.markdown("Análise de padrões inteligentes com limite de entradas")

df = carregar_historico()
if df.empty:
    st.warning("Histórico não encontrado ou vazio.")
else:
    resultados = sugerir_entradas(df)
    for item in resultados:
        if item[0] == "Pular":
            st.info(f"[PULO] - {item[1]}")
        else:
            st.success(f"{item[0]} | Entrada sugerida: {item[1]} ({item[2]})")
