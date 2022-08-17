import streamlit as st
import hashlib

def md_5():
    input_str = st.text_area("Masukkan Plain Text")
    col1,col2 = st.columns([14,1])
    with col2:
        if st.button("Hash"): 
            if len(input_str) == 0:
                with col1:
                    st.error("Masukkan Text!")
            else:
                hasil = hashlib.md5(input_str.encode())
                with col1:
                    st.info(hasil.hexdigest())

    with st.container():
        st.text("")
        st.header("Apa itu MD5?")
        st.write("""
        MD5 merupakan singkatan dari 'Message-Digest Algorithm 5' yang didesain oleh Profesor Ronald Rivest dari MIT (Rivest, 1994). 
        Saat kerja analitik menunjukkan bahwa pendahulu MD5 yaitu MD4 mulai tidak aman, 
        MD5 kemudian didesain pada tahun 1991 sebagai pengganti dari MD4 (kelemahan MD4 ditemukan oleh Hans Dobbertin).
        
        Dalam kriptografi, MD5 ialah fungsi hash kriptografik yang digunakan secara luas dengan hash value 128-bit. 
        Pada standart Internet (RFC 1321), MD5 telah dimanfaatkan secara bermacam-macam pada aplikasi keamanan, dan MD5 juga umum digunakan untuk melakukan pengujian integritas sebuah file.
        
        Secara perhitungan matetamatis tidak dimungkinkan untuk mendapatkan dua pesan yang miliki hash yang sama. MD-5 adalah salah satu aplikasi yang digunakan untuk mengetahui bahwa pesan yang dikirim tidak ada perubahan sewaktu berada di jaringan.
        Tidak ada serangan yang lebih efisien untuk membongkar/mengetahui hash suatu pesan selain brute-force. Gagasan yang ada didalam algoritma MD5 ini sendiri adalah mengambil data acak baik tulisan atau biner sebagai input dan menghasilkan ukuran nilan hasi tetap sebagai outputnya.
        """)
    
    with st.container():
        st.header("Bagaimana cara kerjanya?")
        col1,col2 = st.columns([3,1.25])

    with col1 :
        st.write("""
        Secara garis besar MD5 bekerja dengan menambahkan bit-bit pengganjal (padding bits), sehingga panjang pesan dalam satuan bit adalah kongruen dengan 448 modulo 512. Bit-bit pengganjal terdiri dari sebuah bit 1 diikuti dengan sisanya bit 0.
        Kemudian akan menambahkan nilai panjang pesan semula. 
        
        Pesan yang telah diberi bit-bit pengganjal selanjutnya ditambah lagi dengan 64 bit yang menyatakan panjang pesan semula. Setelah ditambah dengan 64 bit, panjang pesan sekarang menjadi kelipatan 512 bit.
        setelah selesai maka akan mulai melakukan inisialisasi penyangga (buffer) MD. 
        
        Tahap terakhir melakukan pengolahan Pesan dalam Blok Berukuran 512 bit. Dengan kata lain MD5 menenkripsi tulisan menjadi digit hex. Dengan menggunakan fitur ini bisa meningkatkan keamanan 
        karena data yang dapat dibaca adalah kumpulan digit hex bukan string asli tulisan tersebut.
        """)
    
    with col2:
        st.image("gambar/alur_MD5.jpg")
