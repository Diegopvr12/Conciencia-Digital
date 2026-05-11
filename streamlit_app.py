import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Conciencia Digital",
    page_icon="🧠",
    layout="wide"
)

# Leer tu archivo HTML (sin extensión .html)
with open('conciencia-digital-v2', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Mostrar el HTML
components.html(html_content, height=800, scrolling=True)
