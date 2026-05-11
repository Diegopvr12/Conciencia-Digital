import streamlit as st

def main():
    st.title("🧠 Test de Conciencia Digital")
    st.write("Responde a todas las preguntas a continuación para obtener tu diagnóstico.")

    # Usamos un formulario para agrupar todas las preguntas
    with st.form("test_digital"):
        
        # --- SECCIÓN 1: SEGURIDAD ---
        st.subheader("1. Seguridad en la Red")
        p1 = st.radio("¿Utilizas la misma contraseña para todos tus servicios?", 
                      ["Siempre", "A veces", "Nunca"])
        
        p2 = st.radio("¿Tienes activada la verificación en dos pasos (2FA)?", 
                      ["Sí, en todo", "Solo en lo importante", "No sé qué es eso"])

        # --- SECCIÓN 2: PRIVACIDAD ---
        st.subheader("2. Privacidad y Datos")
        p3 = st.select_slider("¿Qué tan seguido revisas los permisos de tus apps?", 
                              options=["Nunca", "Rara vez", "Frecuentemente", "Siempre"])

        # --- SECCIÓN 3: BIENESTAR (Agrega tantas como necesites) ---
        st.subheader("3. Bienestar Digital")
        p4 = st.number_input("¿Cuántas horas pasas frente a la pantalla al día?", min_value=0, max_value=24)

        # Botón de envío único
        submitted = st.form_submit_button("Obtener Resultados")

    if submitted:
        # Lógica de cálculo de resultados
        puntos = 0
        if p1 == "Nunca": puntos += 10
        if p2 == "Sí, en todo": puntos += 10
        
        st.success(f"¡Test completado! Tu puntuación es: {puntos}")
        # Aquí puedes agregar lógica para mostrar gráficos o consejos personalizados

if __name__ == "__main__":
    main()
