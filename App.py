import streamlit as st

st.title("🤖 Bot de Análisis")

st.write("Escribe un tema y el bot generará un análisis básico.")

consulta = st.text_input("¿Qué quieres analizar?")

if consulta:
    st.subheader("📊 Resultado del análisis")

    st.write("**Tema analizado:**")
    st.write(consulta)

    st.write("### 📌 Resumen")
    st.write("Se está evaluando la información relacionada con este tema.")

    st.write("### 📈 Tendencias principales")
    st.write("- Identificar cambios recientes del mercado.")
    st.write("- Observar oportunidades relacionadas.")
    st.write("- Analizar el comportamiento de usuarios.")

    st.write("### ⚠️ Posibles riesgos")
    st.write("- Falta de información actualizada.")
    st.write("- Cambios en la demanda o competencia.")

    st.write("### 💡 Recomendación")
    st.write("Investigar más datos antes de tomar decisiones.")
