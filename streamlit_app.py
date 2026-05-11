import streamlit as st

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
        margin: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

with open('conciencia-digital-v2.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

st.markdown(html_content, unsafe_allow_html=True)
