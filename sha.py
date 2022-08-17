import streamlit as st
import hashlib

def sha():
    input_text = st.text_area("Masukkan Plain Text ")
    choice = st.selectbox("SHA :", ["SHA1","SHA224","SHA256","SHA384","SHA512"])
    col1,col2 = st.columns([14,1])
    with col2:
        if st.button("Hash"):
            if len(input_text) == 0:
                with col1:
                    st.error("Masukkan Text!")
            else:
                if choice == "SHA1":
                    result = hashlib.sha1(input_text.encode())
                    with col1:
                        st.info(result.hexdigest())
                if choice == "SHA224":
                    result = hashlib.sha224(input_text.encode())
                    with col1:
                        st.info(result.hexdigest())
                if choice == "SHA256":
                    result = hashlib.sha256(input_text.encode())
                    with col1:
                        st.info(result.hexdigest())
                if choice == "SHA384":
                    result = hashlib.sha384(input_text.encode())
                    with col1:
                        st.info(result.hexdigest())
                if choice == "SHA512":
                    result = hashlib.sha512(input_text.encode())
                    with col1:
                        st.info(result.hexdigest())

    with st.container():
        st.text("")
        st.header("Apa itu SHA?")
        st.write("""
        SHA(Secure Hash Algoritma) adalah serangkaian fungsi hash kriptografik yang dirancang oleh National Security Agency (NSA) dan diterbitkan oleh NIST sebagai US Federal Information Processing Standard. 
        Jenis-jenis SHA yaitu SHA-0, SHA-1, dan SHA-2.
        
        SHA-0 memiliki ukuran pesan intisari 160-bit (nilai hash) dan merupakan versi pertama dari algoritma ini. 
        Nilai hash SHA-0 adalah 40 digit. Itu diterbitkan dengan nama "SHA" pada tahun 1993 tetapi tidak digunakan dalam banyak aplikasi karena cepat diganti dengan SHA-1 pada tahun 1995 karena cacat keamanan.
        Setelah kelemahan kriptografi ditemukan di SHA-1, NIST membuat pernyataan pada tahun 2006 yang mendorong lembaga federal untuk mengadopsi penggunaan SHA-2 pada tahun 2010. SHA-2 lebih kuat dari SHA-1 dan serangan yang dilakukan terhadap SHA-2 tidak mungkin terjadi dengan kekuatan komputasi saat ini.

        SHA-2 diterbitkan pada tahun 2001, beberapa tahun setelah SHA-1. SHA-2 mencakup enam fungsi hash dengan berbagai ukuran ringkasan: SHA-224 , SHA-256 , SHA-384 , SHA-512 , SHA-512/224 , dan SHA-512/256.
        """)