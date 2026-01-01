import streamlit as st
import urllib.parse

# Sayfa yapılandırması
st.set_page_config(
    page_title="A101 Kampanya Bildirimleri",
    page_icon="🛒",
    layout="centered"
)

# =============================================================================
# GOOGLE ANALYTICS
# =============================================================================
st.markdown("""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-HWYGLZYYF4"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-HWYGLZYYF4');
</script>
""", unsafe_allow_html=True)

# =============================================================================
# KVKK METİN VERSİYONLARI
# =============================================================================
AYDINLATMA_METNI_VERSIYON = "v1.0"
ACIK_RIZA_METNI_VERSIYON = "v1.0"

# =============================================================================
# CSS STİLLERİ
# =============================================================================
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #E31E24;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .store-name {
        text-align: center;
        color: #333;
        font-size: 22px;
        font-weight: 600;
        margin-bottom: 20px;
        padding: 15px;
        background: linear-gradient(135deg, #fff5f5 0%, #ffe0e0 100%);
        border-radius: 10px;
        border-left: 4px solid #E31E24;
    }
    .info-text {
        text-align: center;
        color: #555;
        font-size: 16px;
        margin-bottom: 25px;
        line-height: 1.6;
    }
    .footer {
        text-align: center;
        color: #888;
        font-size: 11px;
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid #eee;
    }
    .versiyon-bilgi {
        font-size: 10px;
        color: #aaa;
        text-align: right;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# MAĞAZA LİSTESİ
# =============================================================================
MAGAZALAR = {
    "H283": "Fabrikalar Kepez",
    "C820": "Kemerağzı Muratpaşa",
    "J506": "Yahya Kemal Kepez",
    "2454": "Bahçelievler Muratpaşa",
    "B548": "Hamidiye Muratpaşa",
    "0396": "Köroğlu Muratpaşa",
    "F296": "Cahit Sıtkı Muratpaşa",
    "I023": "Balbey Muratpaşa",
    "E180": "Aydınlıkevler Muratpaşa",
    "4282": "Kara Yusuf Kepez",
    "I824": "Yalı Muratpaşa",
    "H519": "Üçyol Kepez",
    "D706": "Suphi Türel Kepez",
    "D587": "Düden Park Muratpaşa",
    "G874": "Mustafa Koç Camii Kepez",
    "1715": "Çağlayan Muratpaşa",
    "C007": "15 Temmuz Kepez",
    "6667": "Hastane Cad Kepez",
    "J218": "15 Katlılar Kepez",
    "1125": "Portakalçiçeği Muratpaşa",
    "C241": "Rasih Kaplan Cd Kepez",
}

# WhatsApp Business numarası
WHATSAPP_NUMBER = "905399311842"

# =============================================================================
# KVKK METİNLERİ
# =============================================================================
AYDINLATMA_METNI = """
**ÜYE MÜŞTERİ AYDINLATMA METNİ**

Yeni Mağazacılık A.Ş.("A101") olarak, veri sorumlusu sıfatıyla, özel hayatın gizliliğinin temeli olan kişisel verilerin korunmasını sadece mevzuata uyum sağlama kapsamında değerlendirmemekte, yaklaşımımızın temeline insana verdiğimiz değeri koymaktayız.

**İŞLENEN KİŞİSEL VERİLERİNİZ**

- **İletişim:** Telefon numarası (WhatsApp)
- **Pazarlama:** Ticari elektronik ileti ret/onay bilgileri
- **Lokasyon:** Mağaza tercihi

**KİŞİSEL VERİLERİNİZİN İŞLENME AMAÇLARI**

Kişisel verileriniz; kampanya, reklam, teklif ve pazarlama faaliyetlerinin gerçekleştirilmesi, ticari elektronik ileti gönderilmesi amaçlarıyla işlenmektedir.

**KİŞİSEL VERİLERİNİZİN ÜÇÜNCÜ KİŞİLERLE PAYLAŞILMASI**

Kişisel verileriniz; yurt içi ve yurt dışı hizmet tedarikçileri ile pazarlama, kampanya faaliyetlerinin gerçekleştirilmesi amacıyla paylaşılabilmektedir.

**İLGİLİ KİŞİNİN HAKLARI**

6698 sayılı Kanun'un 11. maddesi kapsamındaki taleplerinizi kvkk@a101.com.tr e-posta adresine iletebilirsiniz.

**Veri Sorumlusu:** Yeni Mağazacılık A.Ş.
**Adres:** Burhaniye Mah. Nagehan Sok. No: 4B/1 Üsküdar/İstanbul
**Mersis No:** 0948042376200016
"""

ACIK_RIZA_METNI = """
**AÇIK RIZA METNİ**

A101 tarafından, seçmiş olduğum mağazaya özel kampanya, indirim ve fırsatlardan WhatsApp aracılığıyla haberdar edilmem amacıyla telefon numaramın işlenmesine ve tarafıma ticari elektronik ileti gönderilmesine açık rızamla onay veriyorum.

**Listeden çıkmak için WhatsApp üzerinden "ÇIKIŞ" yazmam yeterlidir.**

Açık rızamı dilediğim zaman geri alabileceğimi biliyorum.
"""

# =============================================================================
# ANA UYGULAMA
# =============================================================================

# URL'den mağaza kodunu al
query_params = st.query_params
magaza_kodu = query_params.get("m", "").upper()

# Logo ve başlık
st.markdown('<p class="main-header">🛒 A101</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#666; margin-bottom:20px;">Kampanya Bildirimleri</p>', unsafe_allow_html=True)

# Mağaza kontrolü
if not magaza_kodu:
    st.error("⚠️ Geçersiz erişim. Lütfen mağazadaki QR kodu okutunuz.")
    st.stop()

if magaza_kodu not in MAGAZALAR:
    st.warning(f"⚠️ Mağaza bulunamadı: {magaza_kodu}")
    st.info("Lütfen mağaza personeliyle iletişime geçiniz.")
    st.stop()

magaza_adi = MAGAZALAR[magaza_kodu]

# GA'ya mağaza bilgisi gönder
st.markdown(f"""
<script>
  gtag('event', 'magaza_ziyaret', {{
    'magaza_kodu': '{magaza_kodu}',
    'magaza_adi': '{magaza_adi}'
  }});
</script>
""", unsafe_allow_html=True)

# Mağaza bilgisi
st.markdown(f'<div class="store-name">📍 {magaza_kodu} - {magaza_adi} Mağazası</div>', unsafe_allow_html=True)

# Açıklama
st.markdown("""
<p class="info-text">
    🎉 Size özel kampanya ve indirimleri<br>
    <strong>WhatsApp üzerinden anında</strong> bildireceğiz!
</p>
""", unsafe_allow_html=True)

# Avantajlar
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("✅ **Özel indirimler**")
with col2:
    st.markdown("✅ **Hemen haberdar ol**")
with col3:
    st.markdown("✅ **Anlık bildirim**")

st.markdown("---")

# KVKK Aydınlatma Metni
with st.expander("📄 Kişisel Verilerin Korunması Aydınlatma Metni", expanded=False):
    st.markdown(AYDINLATMA_METNI)
    st.markdown(f'<p class="versiyon-bilgi">Versiyon: {AYDINLATMA_METNI_VERSIYON}</p>', unsafe_allow_html=True)

# Açık Rıza Metni
with st.expander("📄 Açık Rıza Metni", expanded=False):
    st.markdown(ACIK_RIZA_METNI)
    st.markdown(f'<p class="versiyon-bilgi">Versiyon: {ACIK_RIZA_METNI_VERSIYON}</p>', unsafe_allow_html=True)

st.markdown("")

# Onay checkbox'ları
onay_aydinlatma = st.checkbox(
    f"Kişisel Verilerin Korunması Aydınlatma Metni'ni ({AYDINLATMA_METNI_VERSIYON}) okudum, anladım.",
    key="aydinlatma"
)

onay_ticari = st.checkbox(
    f"Ticari elektronik ileti almayı ve Açık Rıza Metni'ni ({ACIK_RIZA_METNI_VERSIYON}) kabul ediyorum.",
    key="ticari"
)

st.markdown("")

# WhatsApp butonu
if onay_aydinlatma and onay_ticari:
    # WhatsApp mesajı
    mesaj = f"Merhaba, {magaza_kodu} {magaza_adi} mağazasındaki kampanyalardan WhatsApp üzerinden haberdar olmak istiyorum."
    encoded_mesaj = urllib.parse.quote(mesaj)
    whatsapp_link = f"https://wa.me/{WHATSAPP_NUMBER}?text={encoded_mesaj}"

    st.markdown(f'''
        <a href="{whatsapp_link}" target="_blank" onclick="gtag('event', 'whatsapp_tiklama', {{'magaza_kodu': '{magaza_kodu}', 'magaza_adi': '{magaza_adi}'}});" style="
            display: block;
            background-color: #25D366;
            color: white;
            padding: 15px 30px;
            text-decoration: none;
            border-radius: 30px;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4);
        ">
            💬 WhatsApp ile Katıl
        </a>
    ''', unsafe_allow_html=True)

    st.markdown("")
    st.success("✅ Butona tıklayarak WhatsApp'a yönlendirileceksiniz.")

    # Çıkış bilgisi
    st.info("ℹ️ Listeden çıkmak için WhatsApp'ta **ÇIKIŞ** yazmanız yeterlidir.")

else:
    st.markdown('''
        <div style="
            display: block;
            background-color: #ccc;
            color: #666;
            padding: 15px 30px;
            border-radius: 30px;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            cursor: not-allowed;
        ">
            💬 WhatsApp ile Katıl
        </div>
    ''', unsafe_allow_html=True)

    st.markdown("")
    st.info("☝️ Devam etmek için yukarıdaki onay kutularını işaretleyiniz.")

# Footer
st.markdown(f"""
<div class="footer">
    Yeni Mağazacılık A.Ş. © 2025<br>
    Bu hizmet A101 mağazaları tarafından sunulmaktadır.<br>
    İletişim: 0850 822 99 00<br><br>
    <span style="font-size:9px; color:#bbb;">
    Aydınlatma Metni: {AYDINLATMA_METNI_VERSIYON} | Açık Rıza: {ACIK_RIZA_METNI_VERSIYON}
    </span>
</div>
""", unsafe_allow_html=True)
