import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Conciencia Digital",
    page_icon="🧠",
    layout="wide"
)

# Inyectamos CSS para ocultar el scroll de Streamlit y ajustar el contenedor
st.markdown("""
    <style>
        /* Oculta el menú y el header de Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Elimina el padding de la app para que el HTML ocupe todo */
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
            margin: 0 !important;
        }

        /* Oculta el scrollbar del contenedor principal de Streamlit */
        .stApp {
            overflow: hidden;
        }

        /* Asegura que el iframe no tenga bordes ni márgenes */
        iframe {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100vh;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# Carga tu archivo HTML
with open('conciencia-digital-v2.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# La clave aquí: height=None y scrolling=False (para que mande el HTML interno)
# O bien, usar un height que cubra el viewport (100vh)
components.html(html_content, height=2000, scrolling=True)lse)
