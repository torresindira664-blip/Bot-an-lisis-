import streamlit as st
from motor.analizador import analizar_tema

st.title("🤖 Bot de Análisis")

st.write("Escribe un tema y el bot generará un análisis.")

consulta = st.text_input("¿Qué quieres analizar?")

if consulta:
    resultado = analizar_tema(consulta)

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
