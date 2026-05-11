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

with open('conciencia-digital-v2.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# La solución: height=0 y scrolling=True
components.html(html_content, height=0, scrolling=True)
