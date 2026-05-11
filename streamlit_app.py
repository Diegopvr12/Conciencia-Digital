import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Conciencia Digital",
    page_icon="🧠",
    layout="wide"
)

# 1. CSS optimizado: Quitamos el scroll del iframe y ajustamos espacios
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }

        /* Quitamos el scroll interno del iframe */
        iframe {
            overflow: hidden;
            display: block;
        }
    </style>
""", unsafe_allow_html=True)

# 2. Carga de tu HTML
try:
    with open('conciencia-digital-v2.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
except FileNotFoundError:
    st.error("No se encontró el archivo HTML.")
    st.stop()

# 3. Renderizado del HTML
# Ajusta el 'height' al tamaño real de tu contenido. 
# Si tu HTML mide 3000px, pon 3000. No pongas de más para que no sobre espacio.
components.html(html_content, height=3500, scrolling=False)

# 4. Tu autenticador (o cualquier cosa que vaya al final)
st.markdown("---") # Una línea divisoria opcional
with st.container():
    st.write("### Sección de Autenticación")
    # Aquí va el código de tu autenticador
    usuario = st.text_input("Usuario")
    clave = st.text_input("Contraseña", type="password")
    if st.button("Ingresar"):
        st.success("Validando...")
