import streamlit as st
from motor.analizador import analizar_tema

st.title("🤖 Bot de Análisis")

st.write("Escribe un tema y el bot generará un análisis.")

consulta = st.text_input("¿Qué quieres analizar?")

if consulta:
    resultado = analizar_tema(consulta)

    st.subheader("📊 Resultado del análisis")

    st.write("### 📌 Resumen")
    st.write(resultado["resumen"])

    st.write("### 📈 Tendencias principales")
    for tendencia in resultado["tendencias"]:
        st.write("- " + tendencia)

    st.write("### ⚠️ Posibles riesgos")
    for riesgo in resultado["riesgos"]:
        st.write("- " + riesgo)

    st.write("### 💡 Recomendación")
    st.write(resultado["recomendacion"])
