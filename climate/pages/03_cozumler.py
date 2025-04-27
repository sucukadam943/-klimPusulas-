import streamlit as st
from utils import local_css, info_card

local_css("styles.css")

st.title("İklim Değişikliği ile Mücadele")

st.markdown("""
    İklim değişikliği ile mücadelede hem bireysel hem de toplumsal düzeyde yapabileceğimiz 
    birçok şey var. İşte bazı önemli adımlar:
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Bireysel Çözümler")
    
    st.markdown("""
    <div class="tip-card">
        <h4>🚶‍♂️ Ulaşım</h4>
        <ul>
            <li>Toplu taşıma kullanın</li>
            <li>Bisiklet veya yürüyüş tercih edin</li>
            <li>Elektrikli araçlara geçiş yapın</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="tip-card">
        <h4>🏠 Ev ve Enerji</h4>
        <ul>
            <li>Enerji tasarruflu cihazlar kullanın</li>
            <li>Yenilenebilir enerji tercih edin</li>
            <li>İzolasyon yaptırın</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### Toplumsal Çözümler")
    
    st.markdown("""
    <div class="tip-card">
        <h4>🌱 Sürdürülebilirlik</h4>
        <ul>
            <li>Geri dönüşüm yapın</li>
            <li>Tek kullanımlık ürünlerden kaçının</li>
            <li>Yerel ve mevsimsel gıdalar tüketin</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="tip-card">
        <h4>📢 Farkındalık</h4>
        <ul>
            <li>İklim değişikliği hakkında bilgi edinin</li>
            <li>Çevrenizdekileri bilinçlendirin</li>
            <li>Çevre projelerine destek olun</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("### Sürdürülebilir Yaşam İpuçları")

info_card(
    "Enerji Tasarrufu",
    "Kullanmadığınız elektronik cihazları kapatın, LED ampuller kullanın ve doğal "
    "aydınlatmadan maksimum faydalanın."
)

info_card(
    "Su Tasarrufu",
    "Daha kısa duş alın, damlatmayan muslukları tamir edin ve yağmur suyunu biriktirin."
)

info_card(
    "Atık Yönetimi",
    "Atıklarınızı ayrıştırın, kompost yapın ve tekrar kullanılabilir ürünleri tercih edin."
)

# Add new solution categories after existing content
st.markdown("### İleri Düzey Çözümler")

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="tip-card">
        <h4>🏢 İş Dünyası Çözümleri</h4>
        <ul>
            <li>Karbon ayak izini azaltan tedarik zincirleri</li>
            <li>Uzaktan çalışma politikaları</li>
            <li>Sürdürülebilir ofis uygulamaları</li>
            <li>Yeşil enerji yatırımları</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="tip-card">
        <h4>🌳 Doğa Temelli Çözümler</h4>
        <ul>
            <li>Ağaçlandırma projeleri</li>
            <li>Kentsel yeşil alanlar</li>
            <li>Toprak karbon tutumu</li>
            <li>Mangrov restorasyonu</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="tip-card">
        <h4>💡 Teknolojik Çözümler</h4>
        <ul>
            <li>Karbon yakalama teknolojileri</li>
            <li>Akıllı şebeke sistemleri</li>
            <li>Enerji verimliliği teknolojileri</li>
            <li>Yapay zeka destekli iklim modelleme</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="tip-card">
        <h4>🏛️ Politik Çözümler</h4>
        <ul>
            <li>Karbon vergisi uygulamaları</li>
            <li>Yenilenebilir enerji teşvikleri</li>
            <li>Sürdürülebilir kentsel planlama</li>
            <li>İklim dostu yasalar</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Add more info cards
info_card(
    "Gıda Sistemleri",
    "Bitki bazlı beslenmeye ağırlık verin, yerel üreticileri destekleyin ve gıda israfını azaltın."
)

info_card(
    "Yatırımlar",
    "Fosil yakıtlardan uzaklaşın, yeşil tahviller ve sürdürülebilir yatırım fonlarını değerlendirin."
)
