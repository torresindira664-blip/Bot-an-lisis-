def analizar_tema(tema):
    tema = tema.lower()

    if "ropa" in tema or "moda" in tema:
        categoria = "Mercado de moda y productos"
        tendencias = [
            "Compras por redes sociales",
            "Personalización de productos",
            "Mayor interés por marcas con identidad"
        ]
        riesgos = [
            "Alta competencia",
            "Cambios rápidos en gustos del consumidor"
        ]
        recomendacion = "Analizar clientes ideales y diferenciar la marca."

    elif "curso" in tema or "educacion" in tema:
        categoria = "Mercado de educación digital"
        tendencias = [
            "Crecimiento del aprendizaje online",
            "Contenido especializado",
            "Comunidades de aprendizaje"
        ]
        riesgos = [
            "Mucha oferta de cursos",
            "Necesidad de generar confianza"
        ]
        recomendacion = "Crear contenido de valor y una propuesta diferente."

    elif "negocio" in tema or "empresa" in tema:
        categoria = "Análisis de negocio"
        tendencias = [
            "Digitalización de servicios",
            "Ventas por internet",
            "Automatización de procesos"
        ]
        riesgos = [
            "Competencia creciente",
            "Mala planificación"
        ]
        recomendacion = "Validar la idea antes de invertir recursos."

    else:
        categoria = "Análisis general"
        tendencias = [
            "Cambios del mercado",
            "Nuevas oportunidades",
            "Comportamiento de usuarios"
        ]
        riesgos = [
            "Falta de información específica",
            "Cambios en la demanda"
        ]
        recomendacion = "Investigar más datos sobre el tema."

    return {
        "categoria": categoria,
        "resumen": f"Análisis inicial sobre {tema}.",
        "tendencias": tendencias,
        "riesgos": riesgos,
        "recomendacion": recomendacion
    }
