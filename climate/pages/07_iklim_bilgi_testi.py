import streamlit as st
import random
from utils import local_css, info_card

local_css("styles.css")

st.title("İklim Bilgi Testi")

st.markdown("""
    İklim değişikliği hakkındaki bilgilerinizi test edin! Bu test, temel kavramları 
    ve güncel konuları içermektedir. Her soruyu dikkatlice okuyun ve en uygun cevabı seçin.
""")

# Soru havuzu
sorular = [
    {
        "soru": "Sera gazı etkisine en çok katkıda bulunan gaz hangisidir?",
        "secenekler": ["Karbondioksit (CO₂)", "Metan (CH₄)", "Azot oksit (N₂O)", "Ozon (O₃)"],
        "dogru_cevap": "Karbondioksit (CO₂)",
        "aciklama": "Karbondioksit, insan faaliyetleri sonucu en çok salınan sera gazıdır ve küresel ısınmaya en büyük katkıyı yapar."
    },
    {
        "soru": "Aşağıdakilerden hangisi yenilenebilir enerji kaynağı değildir?",
        "secenekler": ["Güneş enerjisi", "Kömür", "Rüzgar enerjisi", "Jeotermal enerji"],
        "dogru_cevap": "Kömür",
        "aciklama": "Kömür, fosil yakıtlar kategorisinde yer alır ve yenilenemez enerji kaynaklarındandır."
    },
    {
        "soru": "Paris Anlaşması'nın temel hedefi nedir?",
        "secenekler": [
            "Küresel sıcaklık artışını 2°C'nin altında tutmak",
            "Tüm fosil yakıtları yasaklamak",
            "Tüm ülkelerde nükleer enerjiyi yaygınlaştırmak",
            "Ozon tabakasını korumak"
        ],
        "dogru_cevap": "Küresel sıcaklık artışını 2°C'nin altında tutmak",
        "aciklama": "Paris Anlaşması, küresel sıcaklık artışını 2°C'nin altında tutmayı ve mümkünse 1.5°C ile sınırlamayı hedefler."
    },
    {
        "soru": "Hangi sektör küresel sera gazı emisyonlarına en çok katkıda bulunur?",
        "secenekler": ["Enerji üretimi", "Tarım", "Ulaşım", "Endüstriyel üretim"],
        "dogru_cevap": "Enerji üretimi",
        "aciklama": "Enerji üretimi, özellikle fosil yakıtların yakılması yoluyla, en büyük sera gazı emisyon kaynağıdır."
    },
    {
        "soru": "Aşağıdakilerden hangisi iklim değişikliğinin bir sonucu değildir?",
        "secenekler": [
            "Deniz seviyesinin yükselmesi",
            "Ozon tabakasının incelmesi",
            "Buzulların erimesi",
            "Aşırı hava olaylarının artması"
        ],
        "dogru_cevap": "Ozon tabakasının incelmesi",
        "aciklama": "Ozon tabakasının incelmesi, CFC gazlarının etkisiyle oluşur ve doğrudan iklim değişikliğiyle ilgili değildir."
    }
]

# Test başlatma butonu
if "test_basladi" not in st.session_state:
    st.session_state.test_basladi = False
    st.session_state.puan = 0
    st.session_state.cevaplanan = 0
    st.session_state.sorular = []

def testi_baslat():
    st.session_state.test_basladi = True
    st.session_state.puan = 0
    st.session_state.cevaplanan = 0
    st.session_state.sorular = random.sample(sorular, len(sorular))

if not st.session_state.test_basladi:
    st.button("Testi Başlat", on_click=testi_baslat)
else:
    # Test arayüzü
    if st.session_state.cevaplanan < len(sorular):
        soru = st.session_state.sorular[st.session_state.cevaplanan]
        
        with st.form(f"soru_{st.session_state.cevaplanan}"):
            st.subheader(f"Soru {st.session_state.cevaplanan + 1}/{len(sorular)}")
            st.write(soru["soru"])
            
            cevap = st.radio(
                "Cevabınızı seçin:",
                soru["secenekler"],
                key=f"soru_{st.session_state.cevaplanan}_radio"
            )
            
            submitted = st.form_submit_button("Cevabı Kontrol Et")
        
        if submitted:
            if cevap == soru["dogru_cevap"]:
                st.success("Doğru cevap! 🎉")
                st.session_state.puan += 1
            else:
                st.error(f"Yanlış cevap. Doğru cevap: {soru['dogru_cevap']}")
            
            info_card(
                "Açıklama",
                soru["aciklama"]
            )
            
            st.session_state.cevaplanan += 1
            st.rerun()
    
    if st.session_state.cevaplanan >= len(sorular):
        st.success(f"Test tamamlandı! Puanınız: {st.session_state.puan}/{len(sorular)}")
        
        # Başarı mesajı
        basari_yuzdesi = (st.session_state.puan / len(sorular)) * 100
        if basari_yuzdesi >= 80:
            mesaj = "Harika! İklim değişikliği konusunda oldukça bilgilisiniz! 🌟"
        elif basari_yuzdesi >= 60:
            mesaj = "İyi! Temel konulara hakimsiniz, ama daha da geliştirebilirsiniz. 📚"
        else:
            mesaj = "İklim değişikliği hakkında daha fazla bilgi edinmeye ne dersiniz? 🌱"
        
        st.markdown(f"### {mesaj}")
        
        # Tüm soruların açıklamalarını göster
        st.subheader("Tüm Soruların Açıklamaları")
        for i, soru in enumerate(st.session_state.sorular):
            with st.expander(f"Soru {i+1}: {soru['soru']}"):
                st.write(f"**Doğru Cevap:** {soru['dogru_cevap']}")
                st.write(f"**Açıklama:** {soru['aciklama']}")

# Test bittiğinde gösterilecek yeniden başlatma butonu
if st.session_state.cevaplanan >= len(sorular):
    if st.button("Testi Tekrar Başlat"):
        testi_baslat()
        st.rerun()