import streamlit as st
from datetime import datetime
from utils import local_css, info_card
from database import run_query, create_tables

local_css("styles.css")

st.title("İklim Forumu")

st.markdown("""
    İklim değişikliği hakkında düşüncelerinizi paylaşın, sorular sorun ve toplulukla etkileşime geçin.
    Bu forum, iklim konusunda farkındalığı artırmak ve çözümler üretmek için bir platform sunmaktadır.
""")

# Veritabanı tablolarını oluştur
create_tables()

# Kullanıcı bilgileri
kullanici_adi = st.text_input("Kullanıcı Adınız")

# Yeni konu oluşturma formu
with st.expander("Yeni Konu Oluştur"):
    with st.form("yeni_konu_formu"):
        baslik = st.text_input("Konu Başlığı")
        yorum = st.text_area("Mesajınız")
        gonder = st.form_submit_button("Gönder")
        
        if gonder and kullanici_adi and baslik and yorum:
            result = run_query(
                "INSERT INTO forum_yorumlari (baslik, yorum, kullanici) VALUES (?, ?, ?)",
                (baslik, yorum, kullanici_adi)
            )
            if result is True:
                st.success("Konunuz başarıyla oluşturuldu!")
            else:
                st.error("Bir hata oluştu. Lütfen tekrar deneyin.")
        elif gonder:
            st.warning("Lütfen tüm alanları doldurun.")

# Forum konularını görüntüleme
st.subheader("Forum Konuları")

# Konuları veritabanından çek
konular = run_query("SELECT * FROM forum_yorumlari ORDER BY tarih DESC LIMIT 50")

if konular and isinstance(konular, list):
    for konu in konular:
        with st.container():
            st.markdown(f"### {konu['baslik']}")
            st.markdown(f"*{konu['kullanici']} tarafından {konu['tarih']}*")
            st.markdown(konu['yorum'])
            st.markdown("---")
else:
    info_card(
        "Henüz Konu Yok",
        "İlk konuyu siz açabilirsiniz! Yukarıdaki 'Yeni Konu Oluştur' butonunu kullanarak bir tartışma başlatın."
    )

# Forum kuralları
with st.sidebar:
    st.markdown("### Forum Kuralları")
    st.markdown("""
    1. Saygılı ve yapıcı bir dil kullanın
    2. Konu dışı paylaşımlardan kaçının
    3. Bilimsel verilere dayalı tartışmalar yapın
    4. Diğer kullanıcıların görüşlerine saygı gösterin
    5. Spam ve reklam içerikli paylaşım yapmayın
    """)
    
    st.markdown("### Popüler Konular")
    st.markdown("""
    - İklim Değişikliği ve Yerel Etkiler
    - Yenilenebilir Enerji Çözümleri
    - Sıfır Atık Yaşam
    - Sürdürülebilir Ulaşım
    - Enerji Verimliliği
    """)