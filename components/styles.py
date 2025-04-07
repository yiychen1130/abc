import streamlit as st
import os

def load_css():
    """Load custom CSS from the static/css directory"""
    # Get the absolute path to the CSS file
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    css_file = os.path.join(current_dir, "static", "css", "style.css")
    
    # Check if the file exists
    if os.path.exists(css_file):
        with open(css_file, "r") as f:
            css = f.read()
            st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    else:
        st.warning(f"CSS file not found: {css_file}")
        
def apply_custom_css():
    """Apply custom CSS styles directly"""
    st.markdown("""
    <style>
    @import url('static/css/style.css');
    </style>
    """, unsafe_allow_html=True) 