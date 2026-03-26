import streamlit as st
import base64
import os

st.set_page_config(
    page_title="GuruSales — Flight Accounting",
    page_icon="✈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default UI chrome
st.markdown("""
<style>
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }
    iframe { border: none !important; }
</style>
""", unsafe_allow_html=True)

# Load the HTML file
html_path = os.path.join(os.path.dirname(__file__), "gurusales.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Render full-screen
st.components.v1.html(html_content, height=900, scrolling=True)
