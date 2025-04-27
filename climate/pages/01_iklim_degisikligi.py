import streamlit as st
from utils import local_css, image_with_caption, info_card

local_css("styles.css")

st.title("🌍🔥 İklim Değişikliği Hakkında")

st.markdown("""
<div style='background: linear-gradient(135deg, #e8f5e9, #c8e6c9); padding:20px; border-radius:15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
    <span style="font-size:1.5em;">🌎🔥</span> İklim değişikliği, dünya genelinde sıcaklık ve hava koşullarındaki uzun vadeli değişimleri 
    ifade eder. Bu değişimler doğal süreçlerden kaynaklanabilir, ancak <span style='color:#d32f2f; font-weight:bold'>19. yüzyıldan bu yana 
    gözlemlenen değişimlerin ana nedeni insan faaliyetleridir.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

image_with_caption(
    "https://images.unsplash.com/photo-1628257834696-6eb08710c0c4",
    "🔥 Çevre kirliliği - Fotoğraf: Elle Leontiev"
)

col1, col2 = st.columns(2)

with col1:
    info_card(
        "☁️ Sera Gazı Etkisi",
        "Sera gazları, güneşten gelen ısının atmosferde tutulmasına neden olur..."
    )
    
    info_card(
        "🏭 İnsan Faaliyetleri",
        "Fosil yakıtların kullanımı, ormansızlaşma..."
    )

with col2:
    info_card(
        "🌪️ Küresel Etkiler",
        "İklim değişikliği; kuraklık, sel..."
    )
    
    info_card(
        "🇹🇷 Türkiye'deki Etkiler",
        "Türkiye, iklim değişikliğinden önemli ölçüde etkilenen..."
    )

st.markdown("""
<div style='background-color:#f5f5f5; padding:20px; border-radius:10px; margin-top:20px;'>
    <h3 style='color:#2e7d32; animation: pulse 2s infinite'>🚀💪 Harekete Geçin!</h3>
    <p>İklim değişikliğiyle mücadele etmek için <a href='/Cozumler' style='color:#1e88e5; font-weight:bold'>Çözümler</a> sayfamızı ziyaret edebilirsiniz.</p>
</div>
""", unsafe_allow_html=True)
