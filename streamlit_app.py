import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Conciencia Digital",
    page_icon="🧠",
    layout="wide"
)

# Ocultar elementos de Streamlit
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
        overflow: hidden;
    }
    .main {
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

with open('conciencia-digital-v2.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Calcular altura dinámica del contenido
html_height = html_content.count('\n') * 20

# Mostrar HTML con altura ajustada
components.html(html_content, height=html_height, scrolling=False)
