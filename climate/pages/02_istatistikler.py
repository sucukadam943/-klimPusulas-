import streamlit as st
import plotly.express as px
import pandas as pd
from utils import local_css, stat_card

local_css("styles.css")

st.title("📊🌡️ İklim Değişikliği İstatistikleri")

# Örnek veri setleri
yillar = list(range(1990, 2024))
sicaklik_artisi = [round(0.2 * (i - 1990) + 13.5, 1) for i in yillar]
emisyon_degerleri = [round(2 * (i - 1990) + 300, 1) for i in yillar]

# Güncellenmiş veri setleri
yillar = list(range(1850, 2024, 10))  # 10 yıllık aralıklarla
sicaklik_artisi = [round(0.06 * (i - 1850)/10 + 13.5, 2) for i in yillar]  # 0.06°C artış/10 yıl
emisyon_degerleri = [round(280 + 2.5 * ((i - 1850)/10), 1) for i in yillar]  # 1850'de 280 ppm

# İstatistik kartları
col1, col2, col3 = st.columns(3)
with col1:
    stat_card("1.1°C", "Küresel Sıcaklık Artışı (1850'den beri)\nNASA verilerine göre")
with col2:
    stat_card("419 ppm", "Atmosferik CO₂ Seviyesi (2023)\nNOAA verilerine göre")
with col3:
    stat_card("3.4 mm/yıl", "Deniz Seviyesi Yükselme Hızı\nIPCC verilerine göre")

st.markdown("### 🌡️ Sıcaklık Değişimi Trendi")
df_sicaklik = pd.DataFrame({
    'Yıl': yillar,
    'Sıcaklık (°C)': sicaklik_artisi
})

fig_sicaklik = px.line(
    df_sicaklik, 
    x='Yıl', 
    y='Sıcaklık (°C)',
    title='Yıllara Göre Ortalama Sıcaklık Değişimi'
)
st.plotly_chart(fig_sicaklik, use_container_width=True)

st.markdown("### ☁️ Sera Gazı Emisyonları")
df_emisyon = pd.DataFrame({
    'Yıl': yillar,
    'CO₂ Emisyonu (Mt)': emisyon_degerleri
})

fig_emisyon = px.bar(
    df_emisyon,
    x='Yıl',
    y='CO₂ Emisyonu (Mt)',
    title='Yıllık CO₂ Emisyonları'
)
st.plotly_chart(fig_emisyon, use_container_width=True)
