import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
from utils import local_css, info_card, stat_card

local_css("styles.css")

st.title("Hava Durumu ve İklim Göstergeleri")

st.markdown("""
    Yerel hava durumu ve iklim göstergelerini takip edin. Bu veriler, günlük hava koşullarını
    ve uzun vadeli iklim değişikliği etkilerini anlamanıza yardımcı olur.
""")

# Şehir seçimi
sehir = st.selectbox(
    "Şehir seçin:",
    ["İstanbul", "Ankara", "İzmir", "Antalya", "Bursa", "Adana", "Konya", "Trabzon"]
)

# API anahtarı (kullanıcıların kendi anahtarlarını eklemesi gerekir)
API_KEY = st.secrets.get("OPENWEATHER_API_KEY", "")

if not API_KEY:
    st.warning(
        "OpenWeather API anahtarı bulunamadı. Hava durumu verileri için bir API anahtarı gereklidir. "
        "Lütfen .streamlit/secrets.toml dosyasına OPENWEATHER_API_KEY ekleyin."
    )
    demo_mode = True
else:
    demo_mode = False

# Demo verileri
demo_data = {
    "İstanbul": {"temp": 18, "humidity": 65, "wind_speed": 12, "description": "Parçalı bulutlu"},
    "Ankara": {"temp": 15, "humidity": 55, "wind_speed": 8, "description": "Açık"},
    "İzmir": {"temp": 22, "humidity": 70, "wind_speed": 15, "description": "Güneşli"},
    "Antalya": {"temp": 25, "humidity": 75, "wind_speed": 10, "description": "Güneşli"},
    "Bursa": {"temp": 17, "humidity": 68, "wind_speed": 9, "description": "Bulutlu"},
    "Adana": {"temp": 24, "humidity": 72, "wind_speed": 11, "description": "Açık"},
    "Konya": {"temp": 16, "humidity": 58, "wind_speed": 13, "description": "Parçalı bulutlu"},
    "Trabzon": {"temp": 19, "humidity": 78, "wind_speed": 14, "description": "Yağmurlu"}
}

# Hava durumu verilerini al
def get_weather_data(city):
    if demo_mode:
        return demo_data[city]
    else:
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city},TR&appid={API_KEY}&units=metric&lang=tr"
            response = requests.get(url)
            data = response.json()
            
            return {
                "temp": round(data["main"]["temp"]),
                "humidity": data["main"]["humidity"],
                "wind_speed": round(data["wind"]["speed"] * 3.6),  # m/s to km/h
                "description": data["weather"][0]["description"]
            }
        except Exception as e:
            st.error(f"Hava durumu verileri alınamadı: {e}")
            return demo_data[city]

# Hava durumu verilerini göster
weather_data = get_weather_data(sehir)

# Hava durumu kartları
col1, col2, col3 = st.columns(3)

with col1:
    stat_card(
        f"{weather_data['temp']}°C",
        "Sıcaklık"
    )

with col2:
    stat_card(
        f"%{weather_data['humidity']}",
        "Nem"
    )

with col3:
    stat_card(
        f"{weather_data['wind_speed']} km/s",
        "Rüzgar Hızı"
    )

# Hava durumu açıklaması
st.markdown(f"**Güncel Durum:** {weather_data['description']}")

# İklim değişikliği göstergeleri
st.subheader("İklim Değişikliği Göstergeleri")

# Demo veriler - son 7 günün sıcaklık değişimi
tarihler = [(datetime.now() - timedelta(days=x)).strftime('%Y-%m-%d') for x in range(7)][::-1]
sicakliklar = [weather_data['temp'] + round((i - 3) * 0.5, 1) for i in range(7)]

# Sıcaklık değişimi grafiği
df_sicaklik = pd.DataFrame({
    'Tarih': tarihler,
    'Sıcaklık (°C)': sicakliklar
})

fig_sicaklik = px.line(
    df_sicaklik,
    x='Tarih',
    y='Sıcaklık (°C)',
    title=f'{sehir} Son 7 Gün Sıcaklık Değişimi'
)
st.plotly_chart(fig_sicaklik, use_container_width=True)

# İklim bilgileri
st.markdown("### Bölgesel İklim Bilgileri")

# Demo veriler - yıllık ortalama değerler
yillik_veriler = {
    "İstanbul": {"yagis": 820, "sicaklik": 15.1, "nem": 72},
    "Ankara": {"yagis": 387, "sicaklik": 12.0, "nem": 60},
    "İzmir": {"yagis": 695, "sicaklik": 17.9, "nem": 63},
    "Antalya": {"yagis": 1059, "sicaklik": 18.7, "nem": 64},
    "Bursa": {"yagis": 707, "sicaklik": 14.4, "nem": 69},
    "Adana": {"yagis": 647, "sicaklik": 19.1, "nem": 66},
    "Konya": {"yagis": 320, "sicaklik": 11.5, "nem": 59},
    "Trabzon": {"yagis": 831, "sicaklik": 14.6, "nem": 74}
}

yillik_data = yillik_veriler[sehir]

info_card(
    "Yıllık Ortalama Değerler",
    f"Yağış: {yillik_data['yagis']} mm/yıl\n"
    f"Sıcaklık: {yillik_data['sicaklik']}°C\n"
    f"Nem: %{yillik_data['nem']}"
)

# İklim değişikliği etkileri
st.markdown("### İklim Değişikliği Etkileri")

info_card(
    "Bölgesel Etkiler",
    "İklim değişikliği, bölgenizdeki hava olaylarının sıklığını ve şiddetini etkileyebilir. "
    "Sıcak hava dalgaları, şiddetli yağışlar ve kuraklık gibi ekstrem hava olaylarının "
    "artması beklenmektedir."
)

# Öneriler
st.markdown("### Öneriler")

info_card(
    "İklim Değişikliğiyle Mücadele",
    "- Enerji tasarrufu yapın\n"
    "- Toplu taşıma kullanın\n"
    "- Su tasarrufu yapın\n"
    "- Geri dönüşüme önem verin\n"
    "- Yeşil alanları koruyun"
)