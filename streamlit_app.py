import streamlit as st
import streamlit.components.v1 as components

# 1. Configuración de la página
st.set_page_config(
    page_title="Conciencia Digital",
    page_icon="🧠",
    layout="wide"
)

# 2. CSS para limpiar Streamlit y permitir el scroll principal
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Eliminamos espacios en blanco para que el HTML fluya mejor */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }

        /* Quitamos el scroll interno del iframe por si acaso */
        iframe {
            overflow: hidden;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Lectura del archivo HTML
try:
    with open('conciencia-digital-v2.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
except FileNotFoundError:
    st.error("No se encontró el archivo HTML.")
    st.stop()

# 4. Renderizado
# 'scrolling=False' elimina la barra del componente.
# 'height' debe ser igual o mayor al largo de tu diseño para que Streamlit use su propio scroll.
components.html(html_content, height=8000, scrolling=False)
