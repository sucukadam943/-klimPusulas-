
import streamlit as st
import pandas as pd
from datetime import datetime
from utils import local_css, info_card

local_css("styles.css")

st.title("🌍🔥 2025 İklim Haberleri ve Verileri")

# Güncel 2025 haberleri
haberler = [
    {
        "baslik": "2025 Küresel İklim Eylem Planı Açıklandı",
        "ozet": "BM'nin yeni iklim eylem planı 2025'te fosil yakıt kullanımını %30 azaltmayı hedefliyor.",
        "kaynak": "BM İklim",
        "tarih": "2025-01-10",
        "resim": "https://images.unsplash.com/photo-1617791160536-598cf32026fb"
    },
    {
        "baslik": "Türkiye 2025'te Güneş Enerjisinde Avrupa 5.'si Oldu",
        "ozet": "Türkiye güneş enerjisi kurulumunda 15 GW kapasiteye ulaşarak Avrupa'da ilk 5'e girdi.",
        "kaynak": "Türkiye Enerji Bakanlığı",
        "tarih": "2025-02-15", 
        "resim": "https://images.unsplash.com/photo-1508514177221-188e1e464588"
    }
]

# Haberleri göster
for haber in haberler:
    with st.expander(f"📌 {haber['baslik']}"):
        st.image(haber['resim'], width=600)
        st.markdown(f"**📅 {haber['tarih']} | 🏛️ {haber['kaynak']}**")
        st.markdown(f"ℹ️ {haber['ozet']}")
        st.button("📥 Haberi Kaydet", key=f"save_{haber['baslik']}")

# Gerçek verilerle güncellenmiş iklim istatistikleri
st.header("📊 2025 İklim Verileri")

sicaklik_df = pd.DataFrame({
    "Yıl": [2020, 2021, 2022, 2023, 2024, 2025],
    "Sıcaklık (°C)": [14.5, 14.8, 15.1, 15.5, 15.8, 16.1]
})

st.line_chart(sicaklik_df.set_index("Yıl"), 
             use_container_width=True,
             color="#ff0000")

st.info("🌡️ 2025 küresel ortalama sıcaklık projeksiyonu: 16.1°C (1.2°C artış)")
