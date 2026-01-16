import streamlit as st
import pandas as pd
import numpy as np
import urllib.parse  # Library untuk mengubah teks menjadi format link WA

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Koperasi Merah Putih",
    page_icon="🇮🇩",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS KOSTUM (Agar lebih berwarna) ---
st.markdown("""
<style>
    [data-testid="stMetricValue"] {
        font-size: 24px;
        color: #D32F2F;
    }
    .stHeader {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 10px;
    }
    /* Tombol WA Custom */
    .stLinkButton {
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/921/921356.png", width=100) # Icon Koperasi
    st.title("Koperasi Merah Putih")
    st.write("📍 *Maju Bersama Anggota*")
    st.divider()
    menu = st.radio("Menu Utama", ["🏠 Dashboard", "ℹ️ Tentang Kami", "💸 Simulasi Pinjaman", "📞 Hubungi Admin"])
    st.info("💡 **Info:** Rapat Anggota Tahunan akan diadakan bulan depan.")

# --- HALAMAN DASHBOARD ---
if menu == "🏠 Dashboard":
    st.markdown("<h1 style='text-align: center; color: #D32F2F;'>🇮🇩 Selamat Datang Anggota!</h1>", unsafe_allow_html=True)
    st.write("Berikut adalah performa koperasi kita secara *real-time*.")
    
    # Metrik Baris Atas
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Anggota", "1,250", "+12 bln ini")
    col2.metric("Total Aset", "Rp 5.2 M", "+5%")
    col3.metric("SHU Tahun Lalu", "Rp 350 Jt", "Stabil")
    col4.metric("Bunga Pinjaman", "1.2%", "Flat/Bulan")

    st.divider()

    # Grafik Pertumbuhan (Data Dummy)
    st.subheader("📈 Pertumbuhan Aset Koperasi (5 Tahun Terakhir)")
    
    chart_data = pd.DataFrame({
        'Tahun': ['2021', '2022', '2023', '2024', '2025'],
        'Aset (Miliar)': [2.5, 3.1, 3.8, 4.5, 5.2]
    })
    st.bar_chart(chart_data.set_index('Tahun'), color="#D32F2F")

    # Info Terkini
    with st.expander("📢 Pengumuman Penting (Klik untuk membuka)"):
        st.write("""
        1. Pembagian SHU akan dilakukan tanggal 20 Januari.
        2. Tersedia paket Sembako Murah mulai minggu depan.
        3. Harap perbarui data KTP di admin.
        """)

# --- HALAMAN TENTANG KAMI ---
elif menu == "ℹ️ Tentang Kami":
    st.title("Profil Koperasi")
    
    tab1, tab2, tab3 = st.tabs(["Visi & Misi", "Struktur Organisasi", "Sejarah"])
    
    with tab1:
        st.subheader("Visi")
        st.success("Menjadi soko guru perekonomian anggota yang mandiri dan bermartabat.")
        st.subheader("Misi")
        st.markdown("""
        * ✅ Memberikan pelayanan simpan pinjam yang mudah.
        * ✅ Mengembangkan unit usaha sektor riil.
        * ✅ Transparansi dalam pengelolaan keuangan.
        """)
        
    with tab2:
        st.subheader("Pengurus Periode 2024-2029")
        col_a, col_b = st.columns(2)
        with col_a:
            st.write("**Ketua:** Bpk. Susanto")
            st.write("**Sekretaris:** Ibu Ani")
        with col_b:
            st.write("**Bendahara:** Bpk. Budi")
            st.write("**Pengawas:** Ibu Susi")
            
    with tab3:
        st.write("Koperasi ini didirikan pada tahun 1998 dengan modal awal semangat gotong royong...")

# --- HALAMAN SIMULASI PINJAMAN ---
elif menu == "💸 Simulasi Pinjaman":
    st.title("Kalkulator Pinjaman")
    st.write("Gunakan fitur ini untuk memperkirakan cicilan bulanan Anda.")

    with st.container(border=True): 
        col_input, col_result = st.columns([1, 1])
        
        with col_input:
            jumlah_pinjaman = st.number_input("Jumlah Pinjaman (Rp)", min_value=1000000, max_value=50000000, step=500000, value=5000000)
            tenor = st.slider("Jangka Waktu (Bulan)", 3, 36, 12)
            bunga_persen = 1.2 # Bunga 1.2% per bulan
            
        # Hitungan
        bunga_nominal = jumlah_pinjaman * (bunga_persen / 100)
        cicilan_pokok = jumlah_pinjaman / tenor
        total_angsuran = cicilan_pokok + bunga_nominal
        
        with col_result:
            st.subheader("Estimasi Angsuran")
            st.metric("Angsuran per Bulan", f"Rp {total_angsuran:,.0f}")
            st.write(f"*Rincian: Pokok Rp {cicilan_pokok:,.0f} + Bunga Rp {bunga_nominal:,.0f}*")
            
            st.info("Simulasi ini hanya perkiraan. Hubungi Admin untuk info resmi.")

# --- HALAMAN KONTAK (MODIFIKASI WHATSAPP) ---
elif menu == "📞 Hubungi Admin":
    st.title("Layanan Pelanggan")
    
    col1, col2 = st.columns(2)
    with col1:
        # Gambar ilustrasi Customer Service
        st.image("https://cdn-icons-png.flaticon.com/512/3082/3082383.png", width=300)
    
    with col2:
        st.subheader("Kirim Pesan via WhatsApp")
        st.write("Isi formulir di bawah ini, lalu klik tombol untuk terhubung ke WhatsApp Admin.")
        
        with st.form("form_wa"):
            nama = st.text_input("Nama Anda")
            pesan = st.text_area("Pesan / Pertanyaan")
            
            # Tombol Submit di dalam Form
            submitted = st.form_submit_button("Siapkan Pesan")
            
        if submitted:
            if nama and pesan:
                # 1. Format Nomor HP (Ganti 08 jadi 628)
                nomor_wa = "6282349024863"
                
                # 2. Buat Template Pesan
                text_wa = f"Halo Admin Koperasi, saya *{nama}*.\n\nSaya ingin menyampaikan:\n_{pesan}_"
                
                # 3. Encode teks agar bisa masuk URL (mengubah spasi jadi %20, dst)
                text_encoded = urllib.parse.quote(text_wa)
                
                # 4. Buat Link
                link_wa = f"https://wa.me/{nomor_wa}?text={text_encoded}"
                
                # 5. Tampilkan Tombol Link Besar
                st.success("Pesan siap dikirim! Klik tombol di bawah ini:")
                st.link_button("🚀 KIRIM PESAN KE WHATSAPP SEKARANG", link_wa, type="primary")
            else:
                st.error("Mohon isi Nama dan Pesan terlebih dahulu.")
                
    st.divider()
    st.markdown("<center>Dibuat dengan ❤️ oleh Tim IT Koperasi Merah Putih</center>", unsafe_allow_html=True)