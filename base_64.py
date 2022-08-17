import streamlit as st
import base64

def base_64():
    input1 = st.text_area("Masukkan PlainText")
    col1,col2,col3 = st.columns([10,1,1])
    with col2:
        if st.button("Encode"):
            if len(input1) == 0:
                with col1:
                    st.error("Masukkan Text!")
            else:
                hasil = input1.encode("ascii")
                base64_bytes = base64.b64encode(hasil)
                base64_string = base64_bytes.decode("ascii")
                st.text("")
                with col1:
                    st.info(base64_string)
    with col3:
        try:
            if st.button("Decode"):
                if len(input1) == 0:
                    with col1:
                        st.error("Masukkan Text!")
                else:
                    hasil = input1.encode("ascii")
                    sample_string_bytes = base64.b64decode(hasil)
                    sample_string = sample_string_bytes.decode("ascii")
                    with col1:
                        st.info(sample_string)
        except:
            with col1:
                st.error("Kesalahan Input")

    with st.container():
        st.text("")
        st.header("Apa itu Base64?")
        st.write("""
                Base64 merupakan salah satu algoritma untuk encoding dan decoding suatu data ke dalam format ASCII, 
                yang didasarkan pada bilangan dasar 64 atau bisa dikatakan sebagai
                salah satu metode yang digunakan untuk
                melakukan encoding (penyandian) terhadap data
                binary. 
                
                Karakter yang dihasilkan pada
                transformasi Base64 ini terdiri dari A….Z, a….z
                dan 0….9, serta ditambah dengan dua karakter
                terakhir yang bersimbol yaitu + dan / serta satu
                buah karakter sama dengan (=) yang digunakan
                untuk penyesuaian dan menggenapkan data
                binary atau istilahnya disebut sebagai pengisi pad.
                Karakter simbol yang akan dihasilkan akan
                tergantung dari proses algoritma yang berjalan.              
                """)
    with st.container():
        st.text("")
        st.header("Bagaimana Cara Kerjanya?")
        col1,col2 = st.columns([2,1.3])
        with col1:
            st.write("""
                    Teknik encoding Base64 sebenarnya sederhana, jika ada satu senarai (string) bytes yang akan disandikan ke Base64 maka caranya adalah :

                    - Carilah kode ASCII dari masing-masing teks.
                    - Cari bilangan biner 8 bit dari kode ASCII yang ada.
                    - Gabungkan 8 bit tadi menjadi 24 bit.
                    - Kemudian, pecah 24 bit tadi menjadi 6 bit. Maka akan menghasilkan 4 pecahan.
                    - Masing-masing pecahan diubah diubah kedalam nilai decimal.
                    - Terakhir, jadikan nilai – nilai decimal tersebut menjadi indeks untuk memilih karakter penyusun dari base64 dan maksimal adalah 63 atau indeks ke 64.
                    - Jika ternyata dalam proses encoding terdapat sisa pembagi, maka tambahkan sebagai penggenap sisa tersebut karakter ‘=’. Maka terkadang pada base64 akan muncul satu atau dua karakter ‘=’.
                    """)
        with col2:
            st.image("gambar/index.png")