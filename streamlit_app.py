import streamlit as st

# 1. Configuración de la página (DEBE SER LA PRIMERA LÍNEA DE STREAMLIT)
st.set_page_config(page_title="Conciencia Digital", layout="centered")

# 2. Estilos (Corregido para evitar el TypeError de indentación)
st.markdown("""
<style>
    .stRadio {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e6e9ef;
        margin-bottom: 10px;
    }
    .main {
        background-color: #f8f9fa;
    }
</style>
""", unsafe_content_html=True)

# --- TU TEST EXTENDIDO ---
st.title("🛡️ Test de Conciencia Digital")
st.write("Responde todas las preguntas para evaluar tu comportamiento en línea.")

# Usamos un formulario para que el test sea largo y se envíe al final
with st.form("mi_test_unico"):
    
    st.subheader("Sección 1: Seguridad y Contraseñas")
    p1 = st.radio("1. ¿Qué tan compleja es tu contraseña principal?", 
                  ["Fácil (nombre, fecha)", "Media (letras y números)", "Alta (símbolos, mayúsculas y larga)"])
    
    p2 = st.radio("2. ¿Usas autenticación de dos pasos (el código que llega al móvil)?", 
                  ["Nunca", "Solo en algunas apps", "En todas mis cuentas"])

    st.subheader("Sección 2: Privacidad")
    p3 = st.radio("3. ¿Quién puede ver tu foto de perfil en redes sociales?", 
                  ["Todo el mundo", "Solo mis amigos", "Nadie / Solo yo"])
    
    p4 = st.radio("4. ¿Sueles aceptar las cookies de todas las páginas sin leer?", 
                  ["Sí, siempre", "A veces", "No, las rechazo o configuro"])

    st.subheader("Sección 3: Bienestar y Huella")
    p5 = st.radio("5. ¿Buscas tu nombre en Google para ver qué aparece?", 
                  ["Nunca lo he hecho", "Lo hice una vez", "Lo hago periódicamente"])
    
    # Aquí puedes seguir añadiendo p6, p7, p8... hasta que sea tan largo como quieras.
    
    # Botón final
    submit = st.form_submit_button("Finalizar Test")

if submit:
    st.balloons()
    st.success("¡Test completado con éxito!")
    # Aquí calculas el resultado
    total = 0
    if "Alta" in p1: total += 20
    if "todas" in p2: total += 20
    
    st.metric("Tu puntuación", f"{total}/100")
