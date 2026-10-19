import streamlit as st
import time

# ==========================================
# 1. KONFIGURASI HALAMAN (PAGE CONFIG)
# ==========================================
# st.set_page_config digunakan untuk mengatur judul tab browser, ikon, dan tata letak halaman.
# Harus dipanggil di awal script sebelum elemen Streamlit lainnya.
st.set_page_config(
    page_title="ALSD IKI - Modul Streamlit",
    page_icon="🗞️",
    layout="wide"
)

# ==========================================
# 2. KOMPONEN TEKS & HEADING (TEXT ELEMENTS)
# ==========================================
# Digunakan untuk menampilkan judul, sub-judul, teks biasa, dan format markdown/LaTeX.
st.title("Judul Utama Applications & Dashboard")
st.header("Sub Judul: Algoritma dan Struktur Data")
st.subheader("Bagian: Elemen UI Interaktif")
st.text("Monospace text - Cocok untuk menampilkan teks mentah/keluaran konsol")
st.markdown("Format **tebal**, *miring*, dan persamaan matematika $\LaTeX$: $E = mc^2$")
st.caption("Keterangan/Caption: Teks berukuran kecil untuk memberikan informasi tambahan.")

# ==========================================
# 3. ELEMEN NOTIFIKASI & PESAN STATUS
# ==========================================
# Digunakan untuk memberikan umpan balik visual kepada pengguna (sukses, info, peringatan, error).
st.success("Berhasil! Operasi telah dieksekusi dengan benar.")
st.info("Informasi: Model eksekusi Streamlit berjalan secara Top-to-Bottom (Rerun).")
st.warning("Peringatan: Variabel lokal akan diriset setiap kali terjadi rerun kecuali menggunakan session_state.")
st.error("Error! Terjadi kesalahan input atau sistem.")

# ==========================================
# 4. FORM INPUT INTERAKTIF (WIDGETS)
# ==========================================
# Elemen antarmuka untuk menerima input dari pengguna.
st.subheader("Form Input Pengguna")

nama = st.text_input("Nama:", "Anonim")
umur = st.number_input("Usia:", min_value=0, max_value=100, value=20)
topik = st.selectbox("Topik Pelajaran:", ["Rekursif", "Stack", "Queue", "Sorting", "Tree"])
hobi = st.multiselect("Bahasa Pemrograman Pilihan:", ["Python", "C++", "Java", "Go"])
setuju = st.checkbox("Saya menyetujui syarat & ketentuan")
val = st.slider("Nilai N (Jumlah Iterasi):", min_value=1, max_value=50, value=10)

if st.button("Proses Data Input"):
    st.write(f"Menjalankan proses untuk **{nama}**, Usia: **{umur}**, Topik: **{topik}**, Nilai N: **{val}**")

# ==========================================
# 5. TAMPILAN MEDIA (MEDIA ELEMENTS)
# ==========================================
# Digunakan untuk menampilkan gambar, audio, atau video pada aplikasi.
st.subheader("Media Elements")
st.image("https://via.placeholder.com/300x100", caption="Ilustrasi Visual / Header Image")
# st.audio("suara.mp3") # Buka komentar jika memiliki file audio
# st.video("video.mp4") # Buka komentar jika memiliki file video

# ==========================================
# 6. LAYOUTING & STURKTUR HALAMAN
# ==========================================
# A. Sidebar Navigasi
st.sidebar.title("Navigasi Sidebar")
menu = st.sidebar.radio("Pilih Halaman:", ["Home", "Demo Stack & Rekursif", "Statistik"])

# B. Kolom Berdampingan (Columns)
st.subheader("Layout Kolom Berdampingan")
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    st.write("Area Utama Konten pada Kolom 1 (Lebar rasio 2)")
with col2:
    st.metric(label="FPS", value="60", delta="+2")
with col3:
    st.metric(label="Memory Usage", value="256 MB", delta="-12 MB")

# C. Tabulasi Konten (Tabs)
st.subheader("Tabulasi Konten")
t1, t2, t3 = st.tabs(["📊 Demo Interaktif", "💻 Kode Program", "📈 Grafik & Data"])
with t1:
    st.write("Area Demo Interaktif untuk pengguna.")
with t2:
    st.code("""
# Contoh Kode Python Rekursif
def faktorial(n):
    if n <= 1: 
        return 1
    return n * faktorial(n - 1)
""", language="python")
with t3:
    st.write("Menampilkan contoh Grafik Garis (Line Chart):")
    st.line_chart([10, 20, 15, 25, 40, 30])

# D. Expander Tersembunyi
with st.expander("Buka Detail Informasi Tambahan"):
    st.write("Ini adalah teks tersembunyi yang hanya muncul ketika pengguna mengklik expander.")

# ==========================================
# 7. MANAJEMEN FORM & SUBMIT BUTTON
# ==========================================
# st.form mengelompokkan input sehingga tidak memicu 'rerun' sampai tombol 'Submit' diklik.
st.subheader("Pengelompokan Form (st.form)")
with st.form(key="form_kalkulasi"):
    a = st.number_input("Nilai A:", value=5)
    b = st.number_input("Nilai B:", value=10)
    sub = st.form_submit_button("Hitung Jumlah")

if sub:
    st.write(f"Hasil Penjumlahan: **{a + b}**")

# ==========================================
# 8. MANAJEMEN SESSION STATE & LOGIN SIMULASI
# ==========================================
# st.session_state digunakan untuk menyimpan variabel agar nilainya tidak hilang saat rerun.
st.subheader("Manajemen State & Autentikasi")

# A. Counter sederhana dengan Session State
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Tambah Counter"):
    st.session_state.count += 1
    st.write(f"Total Klik: **{st.session_state.count}**")

# B. Simulasi Sistem Login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.subheader("Halaman Akses / Login")
    u = st.text_input("Username:")
    p = st.text_input("Password:", type="password")
    if st.button("Login"):
        if u == "admin" and p == "123":
            st.session_state.logged_in = True
            st.session_state.user = u
            st.success("Login Berhasil!")
            st.rerun() # Memicu rerun aplikasi untuk memperbarui tampilan
        else:
            st.error("Kredensial Salah!")
else:
    st.success(f"Selamat Datang Kembali, **{st.session_state.get('user', 'User')}**!")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

# ==========================================
# 9. FUNGSI MATEMATIKA & REKURSIF
# ==========================================
# Definisi fungsi matematika dasar menggunakan pendekatan rekursif.

# 1. Fungsi Faktorial Rekursif
def faktorial(n):
    if n <= 1: 
        return 1
    return n * faktorial(n - 1)

# 2. Fungsi Fibonacci Rekursif
def fibonacci(n):
    if n <= 0: 
        return 0
    if n == 1: 
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# 3. Fungsi FPB / GCD (Greatest Common Divisor)
def gcd(a, b):
    if b == 0: 
        return a
    return gcd(b, a % b)

# 4. Fungsi Pangkat Rekursif
def pangkat(a, b):
    if b == 0: 
        return 1
    return a * pangkat(a, b - 1)

# ==========================================
# 10. VISUALISASI REKURSIF & TRACING STACK
# ==========================================
# Fungsi untuk mendokumentasikan/menjejak setiap langkah pemanggilan fungsi rekursif pada halaman.
def trace_faktorial(n, depth=0):
    indent = "&nbsp;&nbsp;&nbsp;&nbsp;" * depth  # Indentasi spasi HTML
    st.markdown(f"{indent}➡️ **Masuk Call Stack:** `faktorial({n})`", unsafe_allow_html=True)
    
    # Base Case
    if n <= 1:
        st.markdown(f"{indent}🛑 **Base Case Reached!** Return 1", unsafe_allow_html=True)
        return 1
    
    # Recursive Call
    res = n * trace_faktorial(n - 1, depth + 1)
    st.markdown(f"{indent}⬅️ **Keluar Call Stack:** `faktorial({n})` = **{res}**", unsafe_allow_html=True)
    return res

# Antarmuka Interaktif Visualisasi Rekursif
st.markdown("---")
st.subheader("Visualisator Call Stack Rekursif (Faktorial)")
num = st.number_input("Masukkan Nilai N (Maksimal 6 agar stack tidak terlalu panjang):", min_value=1, max_value=6, value=3)

if st.button("Jalankan Tracing Rekursif"):
    with st.spinner("Memproses tracing call stack..."):
        time.sleep(0.3) # Efek simulasi pemrosesan
        st.info(f"Pohon Pemanggilan Rekursif untuk N = {num}:")
        hasil = trace_faktorial(num)
        st.success(f"Hasil AkhirPerhitungan {num}! = **{hasil}**")


# ==========================================
# 11. PENGOLAHAN DATA TABULAR (DATAFRAME & TABLE)
# ==========================================
# Streamlit menyediakan widget khusus untuk menampilkan dan mengedit data tabel/Dataframe.
import pandas as pd

st.markdown("---")
st.subheader("11. Tampilan Data Tabular & Edit Data")

# Contoh DataFrame Sederhana
data_film = pd.DataFrame({
    "Judul": ["Inception", "Interstellar", "The Dark Knight", "Oppenheimer"],
    "Genre": ["Sci-Fi", "Sci-Fi", "Action", "Biography"],
    "Tahun": [2010, 2014, 2008, 2023],
    "Rating": [8.8, 8.7, 9.0, 8.9]
})

# A. Display Dataframe Interaktif
st.write("##### A. Tabel Interaktif (`st.dataframe`)")
st.dataframe(data_film, use_container_width=True)

# B. Edit Dataframe Langsung
st.write("##### B. Editor Data Interaktif (`st.data_editor`)")
st.caption("Anda dapat mengubah angka/teks langsung di tabel berikut:")
edited_df = st.data_editor(data_film, num_rows="dynamic")


# ==========================================
# 12. UNGGAH & UNDUH FILE (FILE I/O)
# ==========================================
# Widget untuk mengunggah file dari lokal atau mengunduh data dari aplikasi.
st.subheader("12. Unggah & Unduh File")

col_up, col_down = st.columns(2)

with col_up:
    st.write("##### Unggah File CSV/JSON")
    uploaded_file = st.file_uploader("Pilih file CSV", type=["csv", "json"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv'):
            df_upload = pd.read_csv(uploaded_file)
            st.write("Isi File Upload:")
            st.dataframe(df_upload)
        else:
            st.json(uploaded_file.read().decode("utf-8"))

with col_down:
    st.write("##### Unduh Data ke CSV")
    csv_data = data_film.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Unduh Data Film (CSV)",
        data=csv_data,
        file_name="data_film.csv",
        mime="text/csv"
    )


# ==========================================
# 13. ELEMEN POP-UP: DIALOG & POPOVER
# ==========================================
# Streamlit mendukung pop-up berupa Dialog (Modal) dan Popover.
st.subheader("13. Modals & Popover")

# A. Popover Button (Menu Dropdown/Pop-up kecil saat diklik)
with st.popover("⚙️ Pengaturan Filter"):
    st.write("Pengaturan Akses Cepat")
    kat_pilihan = st.selectbox("Pilih Kategori:", ["All", "Sci-Fi", "Action"])
    st.slider("Skor Minimal:", 0.0, 10.0, 8.0)

# B. Streamlit Dialog (Modal Pop-up)
if hasattr(st, "dialog"):
    @st.dialog("Konfirmasi Tindakan")
    def konfirmasi_modal(pesan):
        st.write(pesan)
        if st.button("Ya, Lanjutkan"):
            st.session_state["modal_confirmed"] = True
            st.rerun()

    if st.button("Tampilkan Modal Konfirmasi"):
        konfirmasi_modal("Apakah Anda yakin ingin memperbarui data?")


# ==========================================
# 14. INDIKATOR STATUS, TOAST & PROGRESS BAR
# ==========================================
# Elemen untuk menunjukkan alur proses/pemuatan data secara visual.
st.subheader("14. Indikator Proses & Notifikasi Toast")

col_p1, col_p2 = st.columns(2)

with col_p1:
    if st.button("Simulasi Progress Bar"):
        bar = st.progress(0, text="Memulai pemrosesan...")
        for percent_complete in range(100):
            time.sleep(0.01)
            bar.progress(percent_complete + 1, text=f"Proses: {percent_complete + 1}%")
        st.success("Selesai!")

with col_p2:
    if st.button("Tampilkan Notifikasi Toast"):
        st.toast("Data berhasil disimpan!", icon="🎉")


# ==========================================
# 15. KINERJA & OPTIMASI (CACHING & FRAGMENT)
# ==========================================
# Modul optimasi agar aplikasi Streamlit tidak perlu memuat ulang data berat setiap kali ada interaksi.
st.subheader("15. Optimasi Kinerja (`@st.cache_data`)")

@st.cache_data
def muat_data_berat():
    # Simulasi query database atau membaca file besar
    time.sleep(2) 
    return {"status": "Data Berhasil Dimuat dari Cache", "timestamp": time.time()}

if st.button("Muat Data (Menggunakan Cache)"):
    hasil = muat_data_berat()
    st.write(hasil)
    st.info("Penjelasan: Panggilan pertama akan menunda 2 detik. Panggilan berikutnya akan instan karena diambil dari cache.")