import streamlit as st
import os

def local_css(file_name):
    """Load local CSS file"""
    css_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def image_with_caption(url, caption):
    """Display image with caption"""
    st.image(url, caption=caption, use_container_width=True)

def info_card(title, content):
    """Create an info card with title and content"""
    st.markdown(f"""
    <div class="info-card">
        <h3>{title}</h3>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)

def stat_card(number, label):
    """Create a statistic card with number and label"""
    st.markdown(f"""
    <div class="stat-card">
        <h2>{number}</h2>
        <p>{label}</p>
    </div>
    """, unsafe_allow_html=True)
