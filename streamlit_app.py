import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Conciencia Digital",
    page_icon="🧠",
    layout="wide"
)

# Leer el archivo HTML
with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Mostrar el HTML a pantalla completa
components.html(html_content, height=800, scrolling=True)
