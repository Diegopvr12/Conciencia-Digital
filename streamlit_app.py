import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Conciencia Digital",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)

# Leer el contenido HTML
with open('conciencia-digital-v2.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Usar iframe con altura basada en el contenido del HTML
st.markdown(f"""
<iframe srcdoc="{html_content.replace('"', '&quot;')}" 
        style="width: 100%; height: 100vh; border: none; position: fixed; top: 0; left: 0;">
</iframe>
""", unsafe_allow_html=True)
