import streamlit as st
import os
from database import create_tables, run_query
import pandas as pd
import plotly.express as px

# Ensure database tables exist
create_tables()

# Set page configuration
st.set_page_config(
    page_title="İklim Pusulası",
    page_icon="🌍",
    layout="wide"
)

# Load custom CSS
with open(os.path.join(os.path.dirname(__file__), "styles.css")) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Main page content
st.title("🌍✨ İklim Pusulası: İklim Değişikliği Bilgi ve Eylem Platformu")

st.markdown("""
<div style="background: linear-gradient(135deg, #e3f2fd, #bbdefb); padding: 2rem; border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); animation: fadeIn 1s ease-in-out;">
    <h2 style="color: #0d47a1;">✨👋 Platformumuza Hoş Geldiniz!</h2>
    
    <p>İklim Pusulası, iklim değişikliği hakkında bilgi edinmek, güncel verileri takip etmek ve 
    çözüm önerilerini keşfetmek isteyenler için tasarlanmış kapsamlı bir platformdur.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
### 🚀 Bu platformda neler bulabilirsiniz?

- 🌱 İklim değişikliğinin nedenleri ve etkileri hakkında bilimsel bilgiler
- 📊 Güncel iklim verileri ve istatistikler
- 💡 Bireysel ve toplumsal çözüm önerileri
- 🔥 İklim dostu proje fikirleri
- 👣 Karbon ayak izi hesaplama aracı
- 📰 Güncel iklim haberleri
""")
st.sidebar.markdown("### İpuçları")
st.sidebar.markdown("""
- Gerçekçi hedefler belirleyin
- İlerlemenizi düzenli olarak takip edin
- Başarılarınızı kutlayın
- Zorluklarla karşılaştığınızda pes etmeyin
- Deneyimlerinizi toplulukla paylaşın
""")
st.sidebar.markdown("### Ekstra İpuçları")
st.sidebar.markdown("""
- İklim değişikliği hakkında güncel bilgileri takip edin
- Çevre dostu ürünler kullanın
- Enerji tasarrufu yapın
- Topluluk etkinliklerine katılın
""")
# Example visualization
st.subheader("Global Temperature Change")
data = pd.DataFrame({
    'Year': [2000, 2005, 2010, 2015, 2020],
    'Temperature Change': [0.24, 0.35, 0.47, 0.62, 0.85]
})
fig = px.line(data, x='Year', y='Temperature Change', title='Global Temperature Change Over Years')
st.plotly_chart(fig)

# Accurate climate visualization
st.subheader("Global Temperature Change (NASA Data)")
real_data = pd.DataFrame({
    'Year': [1880, 1900, 1920, 1940, 1960, 1980, 2000, 2020],
    'Temperature Anomaly (°C)': [-0.20, -0.16, -0.25, 0.10, -0.02, 0.20, 0.42, 0.98]
})
fig = px.line(
    real_data, 
    x='Year', 
    y='Temperature Anomaly (°C)',
    title='Global Temperature Anomaly (1880-2020)',
    markers=True
)
fig.update_layout(
    yaxis_title="Temperature Anomaly (°C)",
    xaxis_title="Year",
    hovermode="x unified"
)
st.plotly_chart(fig)
st.caption("Data source: [NASA Global Temperature](https://climate.nasa.gov/vital-signs/global-temperature/)")

# Additional accurate visualization
st.subheader("CO₂ Concentration (ppm)")
co2_data = pd.DataFrame({
    'Year': [1960, 1980, 2000, 2020],
    'CO₂ Concentration': [317, 339, 369, 414]
})
fig2 = px.bar(
    co2_data,
    x='Year',
    y='CO₂ Concentration',
    title='Atmospheric CO₂ Concentration (1960-2020)'
)
st.plotly_chart(fig2)
st.caption("Data source: [NOAA CO₂ Trends](https://gml.noaa.gov/ccgg/trends/) and [ClimatePositions](https://climatepositions.com/co2-in-the-atmosphere-since-1960/)")
