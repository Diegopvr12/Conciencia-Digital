import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Conciencia Digital V2", layout="centered")

# 2. Título e Introducción
st.title("🛡️ Test de Conciencia Digital")
st.write("Responde este cuestionario completo para conocer tu nivel de seguridad y bienestar online.")

# 3. El Test Único (Formulario largo)
with st.form("test_extenso"):
    st.subheader("Sección 1: Seguridad")
    q1 = st.radio("1. ¿Tus contraseñas incluyen mayúsculas, números y símbolos?", ["No", "Solo algunas", "Sí, todas"])
    q2 = st.radio("2. ¿Usas la misma contraseña para redes sociales y el banco?", ["Sí", "Casi siempre", "No, son diferentes"])
    q3 = st.radio("3. ¿Tienes activado el código de verificación en tu WhatsApp?", ["No", "No sé qué es", "Sí, está activo"])
    
    st.divider()
    
    st.subheader("Sección 2: Privacidad")
    q4 = st.radio("4. ¿Quién puede ver lo que publicas en Facebook/Instagram?", ["Público", "Amigos de mis amigos", "Solo mis amigos"])
    q5 = st.radio("5. ¿Aceptas solicitudes de amistad de personas que no conoces?", ["Sí, siempre", "A veces", "Nunca"])
    q6 = st.radio("6. ¿Revisas los permisos que piden las Apps al instalarlas?", ["Nunca", "Rara vez", "Siempre"])
    
    st.divider()
    
    st.subheader("Sección 3: Bienestar Digital")
    q7 = st.radio("7. ¿Usas el móvil mientras comes con otras personas?", ["Siempre", "A veces", "Nunca"])
    q8 = st.radio("8. ¿Te sientes ansioso si no puedes revisar tus notificaciones?", ["Mucho", "Un poco", "Nada"])
    q9 = st.radio("9. ¿Revisas el móvil apenas te despiertas por la mañana?", ["Sí", "A veces", "No, me tomo mi tiempo"])
    q10 = st.radio("10. ¿Crees que el tiempo que pasas en internet es excesivo?", ["Sí", "Tal vez", "No, está controlado"])

    # Botón de envío
    enviado = st.form_submit_button("Finalizar y ver resultado")

# 4. Lógica de Resultados
if enviado:
    # Sistema de puntos simple
    puntos = 0
    # Sumamos puntos si la respuesta es la tercera opción (la más segura/sana)
    respuestas = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    for r in respuestas:
        if r in ["Sí, todas", "No, son diferentes", "Sí, está activo", "Solo mis amigos", "Nunca", "Siempre", "Nada", "No, me tomo mi tiempo", "No, está controlado"]:
            puntos += 10
        elif r in ["Solo algunas", "Casi siempre", "Amigos de mis amigos", "A veces", "Un poco", "Tal vez"]:
            puntos += 5

    st.balloons()
    st.header(f"Tu puntuación: {puntos}/100")
    
    if puntos >= 80:
        st.success("¡Excelente! Tienes una conciencia digital muy alta.")
    elif puntos >= 50:
        st.warning("Buen trabajo, pero tienes puntos ciegos que mejorar.")
    else:
        st.error("Cuidado: Tu nivel de conciencia digital es bajo. Revisa tus hábitos.")
