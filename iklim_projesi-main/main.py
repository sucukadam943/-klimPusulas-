import streamlit as st
from database import create_tables, run_query
from utils import image_with_caption, info_card

# Ensure database tables exist
create_tables()

# Streamlit page settings
st.set_page_config(
    page_title="İklim Değişikliği Bilgi Portalı",
    page_icon="🌍",
    layout="wide"
)

# CSS'in doğru dosya yoluyla çağrılması
st.markdown(
    """<style>
        @import url('/styles.css'); /* veya dosya yolunu doğrudan verebilirsiniz */
    </style>""", 
    unsafe_allow_html=True
)

# Title
st.title("İklim Değişikliği Bilgi Portalı")

# Description
st.markdown("""
    İklim değişikliği, dünyamızın karşı karşıya olduğu en büyük çevresel sorunlardan biridir. 
    Bu portal, iklim değişikliği hakkında temel bilgileri, güncel verileri ve çözüm önerilerini 
    sunmayı amaçlamaktadır.
""")

# Create columns for the main content
col1, col2 = st.columns(2)

with col1:
    image_with_caption(
        "https://images.unsplash.com/photo-1532601224476-15c79f2f7a51-",
        "Kuraklığın etkileri - Çölleşme"
    )
    info_card(
        "İklim Değişikliği Nedir?",
        "İklim değişikliği, uzun vadeli hava durumu örüntülerinde meydana gelen değişiklikleri ifade eder. "
        "Bu değişiklikler doğal süreçlerden kaynaklanabilir, ancak son yüzyılda insan faaliyetleri "
        "nedeniyle hızlanmıştır."
    )

with col2:
    image_with_caption(
        "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05",
        "Sağlıklı ekosistem örneği"
    )
    info_card(
        "Neden Önemli?",
        "İklim değişikliği, ekosistemler, insan sağlığı, gıda güvenliği ve ekonomi üzerinde ciddi "
        "etkilere sahiptir. Bu sorunla mücadele etmek, gelecek nesillerin yaşam kalitesi için "
        "kritik öneme sahiptir."
    )

# New interactive features section
st.markdown("### Yeni İnteraktif Özellikler")

# Create columns for interactive links
col3, col4, col5 = st.columns(3)

with col3:
    st.markdown("""
    🌱 **Proje Fikirleri**
    - İklim fikirleri paylaşın
    - Topluluk projelerine katılın
    - Fikirlere oy verin
    """)
    # Use button for navigating to pages
    if st.button("Proje Fikirlerine Git"):
        st.experimental_rerun()  # Or use a custom redirect method

with col4:
    st.markdown("""
    👣 **Karbon Ayak İzi**
    - Kişisel etkinizi ölçün
    - Çözüm önerileri alın
    - İlerlemenizi takip edin
    """)
    # Same for other links
    if st.button("Karbon Hesaplayıcı"):
        st.experimental_rerun()

with col5:
    st.markdown("""
    📰 **İklim Haberleri**
    - Güncel iklim haberleri
    - Veri görselleştirmeleri
    - İklim verileri aracı
    """)
    if st.button("İklim Haberlerine Git"):
        st.experimental_rerun()

# Highlighted Topics Section
st.markdown("### Öne Çıkan Konular")

col6, col7, col8 = st.columns(3)

with col6:
    st.markdown("""
    🌡️ **Sıcaklık Artışı**
    - Küresel sıcaklık artışı
    - Aşırı hava olayları
    - Kuraklık riskleri
    """)

with col7:
    st.markdown("""
    🌊 **Deniz Seviyesi**
    - Buzulların erimesi
    - Kıyı bölgeleri tehdidi
    - Okyanus asitlenmesi
    """)

with col8:
    st.markdown("""
    🌱 **Ekosistem**
    - Biyoçeşitlilik kaybı
    - Orman yangınları
    - Türlerin yok olması
    """)
