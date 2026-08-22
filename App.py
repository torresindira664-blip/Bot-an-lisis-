import streamlit as st
import json
import os
from datetime import datetime
from motor.analizador import analizar_tema

ARCHIVO_HISTORIAL = "datos/historial.json"


def guardar_analisis(resultado):
    if os.path.exists(ARCHIVO_HISTORIAL):
        with open(ARCHIVO_HISTORIAL, "r", encoding="utf-8") as archivo:
            historial = json.load(archivo)
    else:
        historial = []

    resultado["fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    historial.append(resultado)

    with open(ARCHIVO_HISTORIAL, "w", encoding="utf-8") as archivo:
        json.dump(historial, archivo, indent=4, ensure_ascii=False)


st.title("🤖 Bot de Análisis")

st.write("Escribe un tema y el bot generará un análisis.")

consulta = st.text_input("¿Qué quieres analizar?")

if consulta:
    resultado = analizar_tema(consulta)

    guardar_analisis(resultado)

    st.subheader("📊 Resultado del análisis")

    st.write("### 🏷️ Categoría")
    st.write(resultado["categoria"])

    st.write("### ⭐ Puntuación de oportunidad")
    st.write(str(resultado["puntuacion"]) + "/100")

    st.write("### 📌 Resumen")
    st.write(resultado["resumen"])

    st.write("### 📈 Tendencias principales")
    for item in resultado["tendencias"]:
        st.write("• " + item)

    st.write("### ⚠️ Posibles riesgos")
    for item in resultado["riesgos"]:
        st.write("• " + item)

    st.write("### 💡 Recomendación")
    st.write(resultado["recomendacion"])
