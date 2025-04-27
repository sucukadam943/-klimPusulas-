import streamlit as st
from datetime import datetime
from utils import local_css, info_card, stat_card
from database import run_query, create_tables

local_css("styles.css")

st.title("İklim Taahhütleri")

st.markdown("""
    İklim değişikliğiyle mücadelede bireysel taahhütlerinizi belirleyin ve ilerlemenizi takip edin.
    Her küçük adım, büyük değişimlere yol açabilir!
""")

# Veritabanı tablosunu oluştur
run_query("""
CREATE TABLE IF NOT EXISTS iklim_taahhutleri (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kullanici TEXT NOT NULL,
    taahhut TEXT NOT NULL,
    kategori TEXT NOT NULL,
    baslangic_tarihi DATE DEFAULT CURRENT_DATE,
    tamamlandi INTEGER DEFAULT 0
)
""")

# Kullanıcı bilgileri
kullanici_adi = st.text_input("İsminiz")

# Taahhüt kategorileri
kategoriler = {
    "Enerji": [
        "Enerji tasarruflu ampuller kullanacağım",
        "Kullanılmayan cihazları fişten çekeceğim",
        "Evde yenilenebilir enerji sistemleri kuracağım",
        "Klimayı daha az kullanacağım"
    ],
    "Ulaşım": [
        "Toplu taşıma kullanacağım",
        "Bisiklet kullanacağım",
        "Araç paylaşımı yapacağım",
        "Elektrikli araca geçeceğim"
    ],
    "Atık Yönetimi": [
        "Geri dönüşüm yapacağım",
        "Tek kullanımlık plastikleri azaltacağım",
        "Kompost yapacağım",
        "Atık miktarımı azaltacağım"
    ],
    "Su Kullanımı": [
        "Duş süresini kısaltacağım",
        "Yağmur suyu toplayacağım",
        "Su tasarruflu cihazlar kullanacağım",
        "Bahçe sulamayı optimize edeceğim"
    ],
    "Tüketim": [
        "Yerel ürünler satın alacağım",
        "İkinci el ürünleri tercih edeceğim",
        "Sürdürülebilir markaları destekleyeceğim",
        "Gıda israfını azaltacağım"
    ]
}

# Yeni taahhüt oluşturma
with st.expander("Yeni Taahhüt Ekle"):
    with st.form("yeni_taahhut_formu"):
        kategori = st.selectbox("Kategori", list(kategoriler.keys()))
        taahhut = st.selectbox("Taahhüdünüz", kategoriler[kategori])
        ekle = st.form_submit_button("Taahhüt Ekle")
        
        if ekle and kullanici_adi and taahhut:
            result = run_query(
                "INSERT INTO iklim_taahhutleri (kullanici, taahhut, kategori) VALUES (?, ?, ?)",
                (kullanici_adi, taahhut, kategori)
            )
            if result is True:
                st.success("Taahhüdünüz başarıyla eklendi!")
            else:
                st.error("Bir hata oluştu. Lütfen tekrar deneyin.")
        elif ekle:
            st.warning("Lütfen isminizi girin.")

# Mevcut taahhütleri görüntüle
if kullanici_adi:
    st.subheader("Taahhütleriniz")
    
    taahhutler = run_query(
        "SELECT * FROM iklim_taahhutleri WHERE kullanici = ? ORDER BY baslangic_tarihi DESC",
        (kullanici_adi,)
    )
    
    if taahhutler and isinstance(taahhutler, list):
        for t in taahhutler:
            with st.container():
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"**{t['taahhut']}** ({t['kategori']})")
                    st.caption(f"Başlangıç: {t['baslangic_tarihi']}")
                with col2:
                    if not t['tamamlandi']:
                        if st.button("✓ Tamamlandı", key=f"btn_{t['id']}"):
                            run_query(
                                "UPDATE iklim_taahhutleri SET tamamlandi = 1 WHERE id = ?",
                                (t['id'],)
                            )
                            st.rerun()  # Changed from st.experimental_rerun()
                    else:
                        st.success("Tamamlandı! 🌟")
                st.markdown("---")
    else:
        info_card(
            "Henüz Taahhüt Yok",
            "Yukarıdaki 'Yeni Taahhüt Ekle' butonunu kullanarak bir taahhütte bulunabilirsiniz."
        )

# İstatistikler
st.subheader("Topluluk İstatistikleri")

# Kategori bazında taahhüt sayıları
kategori_istatistikleri = run_query("""
    SELECT kategori, 
           COUNT(*) as toplam_taahhut,
           SUM(tamamlandi) as tamamlanan_taahhut
    FROM iklim_taahhutleri 
    GROUP BY kategori
""")

if kategori_istatistikleri and isinstance(kategori_istatistikleri, list):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        toplam_taahhut = sum(k['toplam_taahhut'] for k in kategori_istatistikleri)
        stat_card(str(toplam_taahhut), "Toplam Taahhüt")
    
    with col2:
        tamamlanan = sum(k['tamamlanan_taahhut'] for k in kategori_istatistikleri)
        stat_card(str(tamamlanan), "Tamamlanan Taahhüt")
    
    with col3:
        aktif = toplam_taahhut - tamamlanan
        stat_card(str(aktif), "Aktif Taahhüt")

# Motivasyon mesajları
st.markdown("### 💚 Bilgi ve Motivasyon")

info_card(
    "Küçük Adımlar, Büyük Değişimler",
    "Her taahhüt, sürdürülebilir bir gelecek için atılmış bir adımdır. "
    "Bireysel eylemlerimiz, toplumsal değişimin temelini oluşturur."
)

# Öneriler
st.sidebar.markdown("### İpuçları")
st.sidebar.markdown("""
- Gerçekçi hedefler belirleyin
- İlerlemenizi düzenli olarak takip edin
- Başarılarınızı kutlayın
- Zorluklarla karşılaştığınızda pes etmeyin
- Deneyimlerinizi toplulukla paylaşın
""")