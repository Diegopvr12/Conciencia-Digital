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
</style>
""", unsafe_allow_html=True)

with open('conciencia-digital-v2.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Altura suficiente para todo el contenido
components.html(html_content, height=20000, scrolling=False)
