import streamlit as st

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Simkopdes Merah Putih",
    page_icon="🇮🇩",
    layout="wide"
)

# --- 2. CSS CUSTOM (AGAR TAMPILAN KEREN) ---
# Ini adalah "bumbu rahasia" untuk membuat background gambar dan kotak transparan
st.markdown("""
<style>
    /* Mengatur Font agar lebih mirip web resmi */
    html, body, [class*="css"] {
        font-family: 'Helvetica', 'Arial', sans-serif;
    }
    
    /* Style untuk HERO SECTION (Gambar Latar Belakang Utama) */
    .hero-container {
        background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("https://images.unsplash.com/photo-1562654501-a0ccc0fc3fb1?q=80&w=1932&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        padding: 80px 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }
    
    .hero-title {
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    .stat-box {
        background-color: rgba(255, 255, 255, 0.2);
        padding: 20px;
        border-radius: 10px;
        margin: 20px auto;
        backdrop-filter: blur(5px);
        max-width: 800px;
    }
    
    .big-number {
        font-size: 48px;
        font-weight: 800;
        color: #ffffff;
    }
    
    .label-text {
        font-size: 16px;
        color: #f0f0f0;
    }

    /* Style untuk Kartu Berita */
    .news-card {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1);
        transition: 0.3s;
        height: 100%;
        color: black;
    }
    .news-card:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }
    .news-date {
        color: #888;
        font-size: 12px;
    }
    .news-title {
        font-weight: bold;
        font-size: 18px;
        margin-top: 5px;
        color: #2c3e50;
    }
    
    /* Menghilangkan padding bawaan Streamlit agar lebih full */
    .block-container {
        padding-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. MENU NAVIGASI (Model Tabs mirip Web) ---
# Menggunakan Tabs agar mirip menu navbar di atas
menu_utama = st.tabs(["🏠 Beranda", "📰 Berita", "📊 Statistik", "📞 Kontak", "🔐 Masuk"])

# ==========================
# HALAMAN BERANDA (HERO)
# ==========================
with menu_utama[0]:
    # --- HERO SECTION DENGAN HTML ---
    # Kita pakai HTML manual di sini agar bisa pasang background image
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">Koperasi Desa/Kelurahan Merah Putih</div>
        <p>Membangun Ekonomi Kerakyatan Berlandaskan Gotong Royong</p>
        
        <div class="stat-box">
            <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
                <div>
                    <div class="big-number">83.762</div>
                    <div class="label-text">Jumlah Desa/Kelurahan</div>
                </div>
                <div>
                    <div class="big-number">83.181</div>
                    <div class="label-text">Koperasi Berbadan Hukum</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- PENCARIAN KOPERASI ---
    st.markdown("### 🔍 Cari Koperasi")
    col_search, col_btn = st.columns([4, 1])
    with col_search:
        cari = st.text_input("", placeholder="Ketik nama koperasi atau lokasi...", label_visibility="collapsed")
    with col_btn:
        st.button("Cari", type="primary", use_container_width=True)

    st.divider()

    # --- BERITA TERBARU (Kartu Grid) ---
    st.subheader("Warta Koperasi Merah Putih")
    
    col1, col2, col3 = st.columns(3)

    # Berita 1
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Palace_of_Bogor_Indonesia.jpg/640px-Palace_of_Bogor_Indonesia.jpg", use_container_width=True)
        st.markdown("""
        <div class="news-card">
            <div class="news-date">21 Juli 2025</div>
            <div class="news-title">Presiden Resmikan 80.000 Kopdes Merah Putih</div>
            <p>Momentum kebangkitan ekonomi desa dimulai hari ini dengan peresmian serentak.</p>
        </div>
        """, unsafe_allow_html=True)

    # Berita 2
    with col2:
        st.image("https://cdn.antaranews.com/cache/1200x800/2024/02/10/antarafoto-kampanye-akbar-prabowo-gibran-100224-adm-19.jpg", use_container_width=True)
        st.markdown("""
        <div class="news-card">
            <div class="news-date">22 Juli 2025</div>
            <div class="news-title">Peluncuran Digitalisasi Koperasi</div>
            <p>Sistem baru memungkinkan anggota memantau SHU langsung dari Handphone.</p>
        </div>
        """, unsafe_allow_html=True)

    # Berita 3
    with col3:
        st.image("https://images.unsplash.com/photo-1556740758-90de2742e1e2?q=80&w=1000", use_container_width=True)
        st.markdown("""
        <div class="news-card">
            <div class="news-date">23 Juli 2025</div>
            <div class="news-title">Pelatihan UMKM Anggota Koperasi</div>
            <p>Meningkatkan kualitas produk lokal agar mampu bersaing di pasar global.</p>
        </div>
        """, unsafe_allow_html=True)

# ==========================
# HALAMAN LAINNYA (Placeholder)
# ==========================
with menu_utama[1]:
    st.title("Halaman Berita")
    st.write("Daftar berita lengkap akan muncul di sini.")

with menu_utama[2]:
    st.title("Data Statistik")
    st.metric("Total Aset", "Rp 500 Miliar")

with menu_utama[3]:
    st.title("Hubungi Kami")
    st.text_input("Nama")
    st.text_area("Pesan")
    st.button("Kirim")

with menu_utama[4]:
    st.title("Login Anggota")
    st.text_input("Username")
    st.text_input("Password", type="password")
    st.button("Masuk")

# Footer
st.markdown("<br><hr><center>© 2026 Koperasi Merah Putih - Membangun Desa</center>", unsafe_allow_html=True)
