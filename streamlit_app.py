import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Conciencia Digital V2", layout="wide")

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #4CAF50; color: white; }
    </style>
    """, unsafe_content_html=True)

# --- NAVEGACIÓN (Manteniendo lo que tenías) ---
with st.sidebar:
    st.title("🛡️ Menú Principal")
    app_mode = st.selectbox("Selecciona una sección:", ["Inicio", "Test de Conciencia Digital", "Recursos", "Sobre nosotros"])

# --- SECCIÓN: INICIO ---
if app_mode == "Inicio":
    st.header("Bienvenido a Conciencia Digital")
    st.write("Tu portal para aprender sobre seguridad, privacidad y bienestar en el mundo online.")
    st.info("Te recomendamos empezar por el **Test de Conciencia Digital** para evaluar tu nivel actual.")

# --- SECCIÓN: EL TEST (EL CÓDIGO EXCLUSIVO QUE PEDISTE) ---
elif app_mode == "Test de Conciencia Digital":
    st.header("🧠 Test Integral de Conciencia Digital")
    st.write("Responde con sinceridad. Este test evalúa 4 pilares clave de tu vida digital.")

    with st.form("test_principal"):
        # --- BLOQUE 1: SEGURIDAD ---
        st.subheader("1. Seguridad Técnica")
        s1 = st.radio("¿Utilizas un gestor de contraseñas o claves únicas para cada sitio?", ["No, uso la misma para todo", "Uso variaciones similares", "Sí, cada cuenta tiene una clave robusta y única"])
        s2 = st.radio("¿Actualizas el software de tu móvil y PC apenas sale la notificación?", ["Nunca", "A veces", "Siempre, por seguridad"])
        s3 = st.radio("¿Sabes identificar un correo de 'Phishing' (suplantación de identidad)?", ["No estoy seguro", "He oído algo", "Sí, sé revisar el remitente y los enlaces"])

        st.divider()

        # --- BLOQUE 2: PRIVACIDAD ---
        st.subheader("2. Privacidad de Datos")
        p1 = st.radio("¿Lees los términos y condiciones antes de instalar una App?", ["Nunca", "Solo por encima", "Reviso los permisos de acceso"])
        p2 = st.selection_toggle("¿Tienes tus perfiles de redes sociales en modo 'Privado'?", value=False)
        p3 = st.radio("¿Qué haces si una web te pide cookies?", ["Aceptar todo", "Solo las necesarias", "Las configuro manualmente"])

        st.divider()

        # --- BLOQUE 3: BIENESTAR DIGITAL ---
        st.subheader("3. Salud y Bienestar")
        b1 = st.slider("¿Cuántas horas antes de dormir dejas de usar pantallas?", 0, 4, 1)
        b2 = st.radio("¿Sientes ansiedad si olvidas el teléfono en casa?", ["Mucha", "Un poco", "Nada, me siento libre"])

        # BOTÓN DE ENVÍO
        enviado = st.form_submit_button("Finalizar Test y Ver Resultados")

    if enviado:
        # Lógica de cálculo (puedes personalizar los puntos)
        score = 0
        if "robusta" in s1: score += 25
        if "Siempre" in s2: score += 25
        if "Privado" in p2: score += 25
        if b1 >= 2: score += 25

        st.balloons()
        st.subheader(f"Tu Nivel de Conciencia Digital: {score}/100")
        
        if score <= 40:
            st.error("⚠️ Nivel Bajo: Tu identidad digital está en riesgo. Revisa nuestra sección de Recursos.")
        elif score <= 75:
            st.warning("⚖️ Nivel Medio: Vas por buen camino, pero tienes brechas de seguridad importantes.")
        else:
            st.success("🛡️ Nivel Alto: ¡Eres un experto digital! Sigue así y ayuda a otros.")

# --- SECCIÓN: RECURSOS ---
elif app_mode == "Recursos":
    st.header("📚 Biblioteca de Aprendizaje")
    st.write("- [Guía de contraseñas seguras](https://es.wikipedia.org/wiki/Contraseña)")
    st.write("- [Cómo evitar estafas en WhatsApp](https://www.osi.es)")

# --- SECCIÓN: SOBRE NOSOTROS ---
elif app_mode == "Sobre nosotros":
    st.header("Acerca del Proyecto")
    st.write("Conciencia Digital V2 es una iniciativa para educar a ciudadanos digitales responsables.")
