import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import aes
import base_64
import md5
import sha

st.set_page_config(page_title="FREEDOM",page_icon=":fire:",layout='wide')
selected = option_menu(
    menu_title=None,
    options = ["Home","AES","Base64","MD5","SHA"],
    icons = ["house","key","shield-lock","lock","shield-check"],
    menu_icon = "cast",
    default_index=0,
    orientation="horizontal",
    )

if selected == "Home":
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_q5pk6p1k.json")
    with st.container():
        st.title("Kriptografi")
        st.write("---")
        left_column,right_column = st.columns([1.5,1])
    with left_column:
        st.header("Apa itu Kriptografi? :shield:")
        st.write("""
        Kriptografi adalah ilmu dan seni untuk menjaga kerahasiaan pesan dengan cara menyandi ke dalam bentuk yang tidak dapat dimengerti maknanya.
        Namun kriptografi bukan hanya sekedar privacy, tetapi memiliki tujuan data integrity, authentication, dan non-repudiation.
        Perlu diingat tidak semua aspek keamanan informasi dapat diatasi dengan kriptografi. 
      
        Sehingga melalui layanan keamanan yang disediakan oleh jenis kriptografi ini, berbagai teks penting dapat dijaga kerahasiaan dan keotentikannya,
        sehingga antar pihak dapat berkorespondensi bisa saling menaruh kepercayaan. Kecuali jika teknik pembuatan kriptografi bocor ke pihak yang tidak di kehendaki. 
        Dimana dalam kriptografi terdapat dua proses dasar yang berupa enkripsi dan deskripsi.
        """)
        st.text("")
    with right_column:
        st_lottie(lottie_coding, height=360, key="cybersec")
        
    with st.container():
        st.write("---")
        st.header("Apa itu Enkripsi? :closed_lock_with_key:")
        left_column,right_column = st.columns([2.7,1])

        with left_column:
            st.write("""
            Enkripsi adalah cara mengacak data sehingga informasi tersebut hanya bisa dibaca oleh orang-orang yang memiliki aksesnya saja.
            Secara teknis, enkripsi adalah proses konversi teks biasa yang terbaca manusia (human-readable plaintext) menjadi teks yang tidak bisa dibaca dan dimengerti (incomprehensible text) yang biasa disebut ciphertext.
            
            Untuk bisa membacanya, dibutuhkan cryptographic key. Enkripsi dibentuk agar informasi tidak jatuh ke pihak yang tidak berhak seperti nomor kartu kredit,
            catatan penting dalam komputer, maupun password untuk mengakses sesuatu.
            """)
            st.text("")
        with right_column:
            st.image("gambar/encrypt.jpg")

    with st.container():
        st.header("Apa itu Dekripsi? :unlock:")
        st.write("""
        Dekripsi adalah sebuah proses pembalikan yang mengubah teks-kode atau pesan yang tidak bisa dimengerti (ciphertext) menjadi sebuah teks-asli atau pesan yang dapat dimengerti (plaintext). 
        Dekripsi juga dapat dilakukan secara otomatis atau manual dengan menggunakan kata sandi atau password. Selama proses tersebut sistem akan mengekstraknya dan mengubahnya menjadi teks ataupun gambar 
        agar tidak hanya dipahami oleh pembaca saja tetapi sistem juga dapat membacanya secara keseluruhan. Dengan kata lain dekripsi merupakan kebalikan dari enkripsi.
        """)    
        st.text("")

    with st.container():
        col1,col2,col3 = st.columns([1,1.25,1])
    with col2:
        st.header("Layanan Kriptografi :mag:")
    st.write("---")
    st.subheader(":one: Kerahasiaan Data (Confidentiality)")
    st.info("Layanan yang ditunjukkan untuk menjaga agar pesan tidak dapat dibaca oleh pihak-pihak yang tidak berhak.")

    st.subheader(":two: Integritas Data (Data Integrity)")
    st.info("Layanan yang menjamin bahwa pesan masih asli/utuh belum pernah dimanipulasi selama pengiriman.")

    st.subheader(":three: Otentikasi (Authentication)")
    st.info("""Layanan yang berhubungan dengan identifikasi, baik mengidentifikasi pihak-pihak yang berkomunikasi (user authentication) maupun mengidentifikasi kebenaran
            sumber pesan (data origin authentication).""")

    st.subheader(":four: Nirpenyangkalan (Non-Repudiation)")
    st.info("""Layanan untuk mencegah entitas yang berkomunikasi melakukan penyangkalan, dimana pengirim pesan menyangkal melakukan pengiriman atau penerima pesan 
            menyangkal telah menerima pesan.""")
    st.text("")
    st.text("")
    with st.container():
        col1,col2,col3 = st.columns([1,1.3,1])
        st.write("---")
        with col2:
            st.header("Algoritma Kriptografi:mag:")

    col1,col2 = st.columns([2.7,1])
    with col1:
        st.subheader(":one: Symmetric Key Cryptography")
        st.write("""Jenis kriptografi ini biasa disebut dengan kriptografi kunci rahasia. Dimana penerima dan pengirim informasi hanya menggunakan satu kunci untuk mengenkripsi dan 
        mendekripsi pesan. Pendekatan yang sering diterapkan melalui jenis ini dianggap lebih efisien dan lebih cepat dibanding metode lainnya.""")
    with col2:
        st.image("gambar/simetris.png")

    col1,col2 = st.columns([2.7,1])
    with col1:
        st.subheader(":two: Asymmetric Key Cryptography")
        st.write("""Lebih dikenal dengan kriptografi kunci publik, dimana memanfaatkan dua kunci 
        yang saling berkaitan, yaitu kunci publik dan kunci privat. Meskipun kunci publik dapat didistribusikan secara bebas, namun jika di pasangkan dengan kunci privat, kode enkripsi dan data 
        didalamnya tetap menjadi rahasia. Selain itu metode ini dianggap lebih aman dan terjamin bila dibandingkan denga metode Symmetric Key Cryptography.""")
    with col2:
        st.image("gambar/asimetris.png")

    col1,col2 = st.columns([2.7,1])
    with col1:
        st.subheader(":three: Hash Function")
        st.write("""Jenis kriptografi ini mengandalkan persamaan matematika, dimana algoritma yang akan mengambil nilai numerik sebagai input dan menghasilkan pesan yang akan diringkas oleh hash. 
        Metode ini tidak memerlukan kunci apapun karena fungsinya telah disesuaikan untuk skenario pengiriman data satu arah. Ada berbagai macam putaran operasi hashing, dan setiap putaran menganggap input
        sebagai larik dari blok terbaru sehingga menghasilkan aktivitas putaran terakhir sebagai output.""")
        st.text("")
    with col2:
        st.image("gambar/hashing.jpg")
        
    with st.container():
        st.header("Contoh Algoritma Kriptografi :arrow_heading_down:")
        st.text("")
        st.text("")
        col1,col2,col3,col4,col5,col6 = st.columns([3,2,2,2,2,2])
        with col2:
            st.image("gambar/aes.png")
            st.subheader("AES")
        with col3:
            st.image("gambar/encoding.png")
            st.subheader("Base64")
        with col4:
            st.image("gambar/md5.png")
            st.subheader("MD5")
        with col5:
            st.image("gambar/sha.png")
            st.subheader("SHA")
if selected == "AES":
    aes.aes()
if selected == "Base64":
    base_64.base_64()
if selected == "MD5":
    md5.md_5()
if selected == "SHA":
    sha.sha()