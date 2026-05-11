import streamlit as st

# 1. Configuración de página
st.set_page_config(page_title="Conciencia Digital V2", page_icon="🛡️", layout="centered")

# 2. Estilos CSS (Corregidos para evitar el TypeError)
st.markdown("""
<style>
    .main { background-color: #f0f2f6; }
    .stRadio > label { font-weight: bold; color: #1f77b4; }
    .stForm { border: 2px solid #d1d5db; padding: 20px; border-radius: 15px; background: white; }
</style>
""", unsafe_content_html=True)

# 3. Encabezado principal
st.title("🛡️ Test de Conciencia Digital")
st.markdown("---")
st.write("Bienvenido al test integral. Responde con sinceridad para evaluar tu madurez digital en seguridad, privacidad y comportamiento.")

# 4. El Test Único y Extenso
with st.form("test_conciencia_digital"):
    
    st.header("Sección 1: Seguridad y Blindaje")
    
    p1 = st.radio("1. ¿Qué estrategia usas para tus contraseñas?", 
                  ["Uso la misma en varias cuentas", "Uso variaciones de una palabra común", "Uso un gestor de contraseñas con claves únicas y complejas"])
    
    p2 = st.radio("2. ¿Tienes activado el Segundo Factor de Autenticación (2FA)?", 
                  ["No, me parece molesto", "Solo en mi correo principal", "Sí, en todas mis cuentas importantes (RRSS, Banco, Email)"])

    p3 = st.radio("3. ¿Cómo reaccionas ante un correo que te pide 'actualizar datos' urgentemente?", 
                  ["Hago clic para ver qué es", "Lo ignoro", "Verifico el remitente y reporto si es sospechoso"])

    st.markdown("---")
    st.header("Sección 2: Privacidad y Huella")
    
    p4 = st.radio("4. Al instalar una App, ¿qué permisos sueles conceder?", 
                  ["Acepto todo para entrar rápido", "Solo los que me parecen lógicos", "Reviso y deniego accesos innecesarios (micrófono, contactos, etc.)"])

    p5 = st.radio("5. ¿Con qué frecuencia revisas quién puede ver tus publicaciones en redes sociales?", 
                  ["Nunca", "Una vez al año", "Frecuentemente reviso mis ajustes de privacidad"])

    p6 = st.radio("6. ¿Compartes fotos de otros (amigos/familia) sin preguntarles primero?", 
                  ["Sí, siempre", "A veces", "Nunca sin su consentimiento"])

    st.markdown("---")
    st.header("Sección 3: Bienestar y Ética")

    p7 = st.radio("7. ¿Cuántas horas antes de dormir dejas de usar dispositivos electrónicos?", 
                  ["Menos de 15 minutos", "Entre 30 y 60 minutos", "Más de una hora"])

    p8 = st.radio("8. Si ves una noticia impactante en redes, ¿qué haces antes de compartirla?", 
                  ["La comparto de inmediato", "La leo completa pero no verifico", "Busco la fuente original para confirmar si es real"])

    p9 = st.radio("9. ¿Sientes ansiedad o estrés cuando no tienes acceso a internet?", 
                  ["Mucha", "Un poco", "Nada, disfruto la desconexión"])

    p10 = st.radio("10. ¿Utilizas herramientas de control de tiempo de pantalla?", 
                   ["No", "Las tengo pero no las miro", "Sí, para limitar mi uso diario"])

    # Botón de envío
    enviar = st.form_submit_button("Finalizar Test y Obtener Diagnóstico")

# 5. Lógica de resultados
if enviar:
    # Cálculo simple de puntos (0, 5, 10 según la respuesta)
    puntos = 0
    respuestas_correctas = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
    
    # Lógica: La última opción siempre suma más puntos en este diseño
    for r in respuestas_correctas:
        if "complejas" in r or "todas" in r or "Verifico" in r or "deniego" in r or "Frecuentemente" in r or "Nunca" in r or "Más de una hora" in r or "Busco la fuente" in r or "Nada" in r or "Sí" in r:
            puntos += 10
        elif "A veces" in r or "Solo" in r or "variaciones" in r:
            puntos += 5

    st.balloons()
    st.markdown("---")
    st.subheader(f"Tu puntuación final: {puntos} / 100")

    if puntos <= 40:
        st.error("🚨 **Nivel Crítico:** Tu conciencia digital es baja. Estás expuesto a riesgos graves de seguridad y privacidad.")
    elif puntos <= 75:
        st.warning("⚠️ **Nivel Intermedio:** Tienes buenos hábitos, pero aún hay brechas que los ciberdelincuentes podrían aprovechar.")
    else:
        st.success("🛡️ **Nivel Experto:** ¡Felicidades! Eres un ciudadano digital consciente y responsable.")
