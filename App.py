import streamlit as st

st.title("🤖 Bot de Análisis")

st.write("Escribe una consulta y el bot analizará la información.")

consulta = st.text_input("¿Qué quieres analizar?")

if consulta:
    st.subheader("Resultado del análisis:")
    st.write("Estoy procesando la consulta:")
    st.write(consulta)
    st.info("Esta es la primera versión del motor de análisis.")
