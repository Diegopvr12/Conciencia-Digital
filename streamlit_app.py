import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Conciencia Digital", layout="wide")

# CSS para eliminar márgenes y el scroll de Streamlit si fuera necesario
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    iframe {display: block;}
</style>
""", unsafe_allow_html=True)

# Carga y renderizado
with open('conciencia-digital-v2.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# scrolling=False para usar el scroll de la web, ajusta height según tu HTML
components.html(html_content, height=2500, scrolling=False)

# Aquí aparecerá tu autenticador automáticamente al final del HTML
