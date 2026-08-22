def analizar_tema(tema):
    tema_original = tema
    tema = tema.lower()

    if "ropa" in tema or "moda" in tema or "infantil" in tema:
        categoria = "Mercado de ropa y moda infantil"
        resumen = "Análisis enfocado en productos de moda para niños."
        tendencias = [
            "Compras por redes sociales",
            "Diseños personalizados",
            "Preferencia por marcas con identidad"
        ]
        riesgos = [
            "Alta competencia",
            "Cambios en gustos de los clientes"
        ]
        recomendacion = "Crear una propuesta diferente y conocer bien al cliente ideal."

    elif "curso" in tema or "educacion" in tema:
        categoria = "Educación digital"
        resumen = "Análisis del mercado de cursos y aprendizaje online."
        tendencias = [
            "Mayor interés por aprender desde internet",
            "Cursos especializados",
            "Comunidades digitales"
        ]
        riesgos = [
            "Mucha competencia",
            "Necesidad de demostrar experiencia"
        ]
        recomendacion = "Crear contenido útil y diferenciar la oferta."

    elif "negocio" in tema or "empresa" in tema or "online" in tema:
        categoria = "Análisis de negocio online"
        resumen = "Análisis de oportunidades en negocios digitales."
        tendencias = [
            "Ventas por internet",
            "Uso de redes sociales",
            "Automatización de procesos"
        ]
        riesgos = [
            "Competencia creciente",
            "Falta de planificación"
        ]
        recomendacion = "Validar la idea antes de invertir."

    else:
        categoria = "Análisis general"
        resumen = "Análisis inicial del tema indicado."
        tendencias = [
            "Cambios del mercado",
            "Nuevas oportunidades",
            "Comportamiento de usuarios"
        ]
        riesgos = [
            "Información limitada",
            "Cambios en la demanda"
        ]
        recomendacion = "Investigar más información antes de decidir."

    return {
        "tema": tema_original,
        "categoria": categoria,
        "resumen": resumen,
        "tendencias": tendencias,
        "riesgos": riesgos,
        "recomendacion": recomendacion
    }
