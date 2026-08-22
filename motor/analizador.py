def analizar_tema(tema):
    tema_original = tema
    tema = tema.lower()

    puntuacion = 50

    if "ropa" in tema or "moda" in tema or "infantil" in tema:
        categoria = "Mercado de ropa y moda infantil"
        puntuacion += 20
        resumen = "Análisis enfocado en productos de moda para niños."
        tendencias = [
            "Compras por redes sociales",
            "Diseños personalizados",
            "Marcas con identidad propia"
        ]
        riesgos = [
            "Alta competencia",
            "Cambios en gustos del consumidor"
        ]
        recomendacion = "Diferenciar la marca y conocer al cliente ideal."

    elif "curso" in tema or "educacion" in tema:
        categoria = "Educación digital"
        puntuacion += 25
        resumen = "Análisis del mercado de formación online."
        tendencias = [
            "Aprendizaje desde internet",
            "Cursos especializados",
            "Comunidades digitales"
        ]
        riesgos = [
            "Mucha competencia",
            "Necesidad de generar confianza"
        ]
        recomendacion = "Crear contenido de valor y una propuesta única."

    elif "negocio" in tema or "empresa" in tema or "online" in tema:
        categoria = "Negocio digital"
        puntuacion += 15
        resumen = "Análisis de oportunidades de negocio."
        tendencias = [
            "Ventas digitales",
            "Automatización",
            "Uso de redes sociales"
        ]
        riesgos = [
            "Competencia creciente",
            "Mala planificación"
        ]
        recomendacion = "Validar la idea y analizar el mercado."

    else:
        categoria = "Análisis general"
        resumen = "Evaluación inicial del tema."
        tendencias = [
            "Cambios del mercado",
            "Nuevas oportunidades",
            "Comportamiento de usuarios"
        ]
        riesgos = [
            "Información limitada",
            "Falta de datos específicos"
        ]
        recomendacion = "Recopilar más información."

    return {
        "tema": tema_original,
        "categoria": categoria,
        "puntuacion": puntuacion,
        "resumen": resumen,
        "tendencias": tendencias,
        "riesgos": riesgos,
        "recomendacion": recomendacion
    }
