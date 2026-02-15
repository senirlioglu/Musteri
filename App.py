import streamlit as st
import uuid
import requests

# Sayfa yapılandırması
st.set_page_config(
    page_title="A101 Kampanya Bildirimleri",
    page_icon="🛒",
    layout="centered"
)

# =============================================================================
# GOOGLE ANALYTICS - Measurement Protocol (Server-Side)
# =============================================================================
GA_MEASUREMENT_ID = "G-HWYGLZYYF4"
GA_API_SECRET = "l9IxqofASTe3cO2wfaX8sg"

def ga_mp(event_name: str, params: dict = None):
    """Server-side GA4 event gönder (Measurement Protocol)"""
    try:
        if "ga_client_id" not in st.session_state:
            st.session_state.ga_client_id = f"{uuid.uuid4()}.{uuid.uuid4().int % 10**10}"

        url = f"https://www.google-analytics.com/mp/collect?measurement_id={GA_MEASUREMENT_ID}&api_secret={GA_API_SECRET}"
        payload = {
            "client_id": st.session_state.ga_client_id,
            "events": [{"name": event_name, "params": params or {}}]
        }
        requests.post(url, json=payload, timeout=3)
    except:
        pass  # GA hatası uygulamayı durdurmasın

# =============================================================================
# KVKK METİN VERSİYONLARI
# =============================================================================
AYDINLATMA_METNI_VERSIYON = "v2.0"
ACIK_RIZA_METNI_VERSIYON = "v2.0"

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
    "0396": "Köroğlu Muratpaşa",
    "1125": "Portakalçiçeği Muratpaşa",
    "1441": "Tonguç",
    "1715": "Çağlayan Muratpaşa",
    "2454": "Bahçelievler Muratpaşa",
    "3812": "Gazi Bulvarı",
    "4282": "Kara Yusuf Kepez",
    "4667": "Orduevi",
    "5490": "Gençlik",
    "6667": "Hastane Cad Kepez",
    "8243": "Güvenlik",
    "8574": "Düden Şelalesi",
    "8971": "Kayıkent",
    "9395": "Ömer Buyrukçu Cd",
    "B130": "Kamile Çömlekçi",
    "B548": "Hamidiye Muratpaşa",
    "C007": "15 Temmuz Kepez",
    "C241": "Rasih Kaplan Cd Kepez",
    "C760": "Ermenek",
    "C820": "Kemerağzı Muratpaşa",
    "D483": "Güzeloluk",
    "D587": "Düden Park Muratpaşa",
    "D705": "Molla Gürani",
    "D706": "Suphi Türel Kepez",
    "E046": "Sosyal Güvenlik",
    "E180": "Aydınlıkevler Muratpaşa",
    "E351": "İsmet Gökşen",
    "F296": "Cahit Sıtkı Muratpaşa",
    "F488": "Aşıkveysel",
    "G874": "Mustafa Koç Camii Kepez",
    "H283": "Fabrikalar Kepez",
    "H519": "Üçyol Kepez",
    "H950": "Turgay Koca",
    "I023": "Balbey Muratpaşa",
    "I566": "Nirvana",
    "I693": "Farabi",
    "I824": "Yalı Muratpaşa",
    "J218": "15 Katlılar Kepez",
    "J365": "Kapalı Yol",
    "J433": "IşıkCaddesi",
    "J506": "Yahya Kemal Kepez",
    "J751": "Yeni Niğdeli Parkı",
}

# =============================================================================
# WHATSAPP KANAL LİNKLERİ (20 Mağaza Pilot)
# =============================================================================
MAGAZA_KANAL_LINK = {
    "H283": "https://whatsapp.com/channel/0029VbCZbtH42DcaK503cM29",
    "J506": "https://whatsapp.com/channel/0029VbBME1L7dmeR8B1v0d0f",
    "4282": "https://whatsapp.com/channel/0029Vb6m1CVLY6cxjBHF340Y",
    "H519": "https://whatsapp.com/channel/0029Vb7bLrI0bIdrrrRx712C",
    "D706": "https://whatsapp.com/channel/0029VbCOoxUGOj9eM2sPg51T",
    "G874": "https://whatsapp.com/channel/0029Vb6hQor545uznDbLoB0R",
    "C007": "https://whatsapp.com/channel/0029VbCPH4hGehEPyK9koP2u",
    "6667": "https://whatsapp.com/channel/0029VbBxKdz2Jl8BioUmG707",
    "J218": "https://whatsapp.com/channel/0029Vb7MFSSH5JLveladfU1a",
    "C820": "https://whatsapp.com/channel/0029Vb7SWcYBA1etXR24542S",
    "2454": "https://whatsapp.com/channel/0029VbC1ox9Fy72LKSdLG113",
    "B548": "https://whatsapp.com/channel/0029Vb7XBW7GE56kN6MDlC3r",
    "0396": "https://whatsapp.com/channel/0029VbC0Zl12phHD5Rm0Qb07",
    "F296": "https://whatsapp.com/channel/0029VbBSAZo3mFY0PEdgV10w",
    "I023": "https://whatsapp.com/channel/0029VbCCpSAD38CYoBAT3J3p",
    "E180": "https://whatsapp.com/channel/0029VbBbr1kC1Fu5sPodMT0X",
    "I824": "https://whatsapp.com/channel/0029VbBth2N9Bb664kmNGQ10",
    "D587": "https://whatsapp.com/channel/0029Vb6iPplBVJl5EEtP9A2y",
    "1715": "https://whatsapp.com/channel/0029VbBllw84Y9lqjZMMGB16",
    "1125": "https://whatsapp.com/channel/0029Vb77PDv6hENzj3UVAo2U",
}

# =============================================================================
# KVKK METİNLERİ (v2.0 - Kanal modeli için güncellendi)
# =============================================================================
AYDINLATMA_METNI = """
**KANAL TAKİPÇİSİ AYDINLATMA METNİ**

Yeni Mağazacılık A.Ş.("A101") olarak, veri sorumlusu sıfatıyla, özel hayatın gizliliğinin temeli olan kişisel verilerin korunmasını sadece mevzuata uyum sağlama kapsamında değerlendirmemekte, yaklaşımımızın temeline insana verdiğimiz değeri koymaktayız.

**İŞLENEN KİŞİSEL VERİLERİNİZ**

- **Pazarlama:** Kanal takip tercihi
- **Lokasyon:** Mağaza tercihi

**KİŞİSEL VERİLERİNİZİN İŞLENME AMAÇLARI**

WhatsApp kanalı üzerinden kampanya ve duyuruların paylaşılması amacıyla mağaza tercih bilginiz işlenmektedir.

**KİŞİSEL VERİLERİNİZİN ÜÇÜNCÜ KİŞİLERLE PAYLAŞILMASI**

Kanal hizmeti Meta (WhatsApp) platformu üzerinden sunulmaktadır.

**İLGİLİ KİŞİNİN HAKLARI**

6698 sayılı Kanun'un 11. maddesi kapsamındaki taleplerinizi kvkk@a101.com.tr e-posta adresine iletebilirsiniz.

**Veri Sorumlusu:** Yeni Mağazacılık A.Ş.
**Adres:** Burhaniye Mah. Nagehan Sok. No: 4B/1 Üsküdar/İstanbul
**Mersis No:** 0948042376200016
"""

ACIK_RIZA_METNI = """
**AÇIK RIZA METNİ**

A101 tarafından, seçmiş olduğum mağazaya özel kampanya, indirim ve fırsatlardan WhatsApp kanalı aracılığıyla haberdar edilmem amacıyla kanal takipçisi olmayı kabul ediyorum.

**Kanaldan ayrılmak için WhatsApp'ta kanalı takipten çıkabilir veya bildirimleri sessize alabilirsiniz.**

Kanalı dilediğim zaman takipten çıkabileceğimi biliyorum.
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

# Mağaza bilgisi
st.markdown(f'<div class="store-name">📍 {magaza_kodu} - {magaza_adi} Mağazası</div>', unsafe_allow_html=True)

# Açıklama
st.markdown("""
<p class="info-text">
    🎉 Kanalı takip ederek<br>
    <strong>kampanya duyurularını anında</strong> görün!
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
    f"Kanal takipçisi olmayı ve Açık Rıza Metni'ni ({ACIK_RIZA_METNI_VERSIYON}) kabul ediyorum.",
    key="ticari"
)

st.markdown("")

# WhatsApp Kanal butonu
if onay_aydinlatma and onay_ticari:
    kanal_link = MAGAZA_KANAL_LINK.get(magaza_kodu)

    if not kanal_link:
        st.error("⚠️ Bu mağaza için kanal henüz tanımlı değil. Lütfen mağaza personeliyle iletişime geçiniz.")
        st.stop()

    # GA Server-Side: Onay verildi eventi (KVKK uyumlu, sadece 1 kez)
    if "ga_consent_sent" not in st.session_state:
        ga_mp("magaza_ziyaret", {
            "magaza_kodu": magaza_kodu,
            "magaza_adi": magaza_adi
        })
        st.session_state.ga_consent_sent = True

    # WhatsApp butonu
    st.markdown(f'''
        <a href="{kanal_link}" target="_blank" style="
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
            📢 WhatsApp Kanalını Takip Et
        </a>
    ''', unsafe_allow_html=True)

    st.markdown("")
    st.success("✅ Butona tıklayarak kanala yönlendirileceksiniz. Takip ederek kampanyaları duyuru olarak alırsınız.")

    # Çıkış bilgisi
    st.info("ℹ️ İstediğiniz zaman kanaldan ayrılabilir veya bildirimleri sessize alabilirsiniz.")

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
            📢 WhatsApp Kanalını Takip Et
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
