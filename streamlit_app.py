import streamlit as st
import streamlit.components.v1 as components

# 1. Configuración de la página
st.set_page_config(
    page_title="Conciencia Digital",
    page_icon="🧠",
    layout="wide"
)

# 2. Inyección de CSS para limpiar la interfaz de Streamlit
st.markdown("""
    <style>
        /* Oculta elementos innecesarios de Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Elimina márgenes y paddings del contenedor principal */
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
            margin: 0 !important;
        }

        /* Bloquea el scroll de la aplicación Streamlit */
        .stApp {
            overflow: hidden;
            position: fixed;
            width: 100%;
            height: 100%;
        }

        /* Estilo para que el iframe ocupe toda la pantalla */
        iframe {
            width: 100vw;
            height: 100vh;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Lectura del archivo HTML
try:
    with open('conciencia-digital-v2.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
except FileNotFoundError:
    st.error("No se encontró el archivo 'conciencia-digital-v2.html'. Verifica el nombre.")
    st.stop()

# 4. Renderizado del componente
# Usamos scrolling=True para que el scroll viva DENTRO del iframe
components.html(html_content, height=2000, scrolling=True)
