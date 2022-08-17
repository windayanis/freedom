import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import streamlit as st

def aes():
    plaintext = st.text_area("Masukkan PlainText/CipherText ")
    key = st.text_input("Masukkan Key")
    col1,col2,col3 = st.columns([10,1,1])
    BS = 16
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    unpad = lambda s : s[:-ord(s[len(s)-1:])]
    with col2:
        if st.button("Enkrip"):
            if len(plaintext) == 0:
                with col1:
                    st.error("Masukkan Text!")
            else:
                p_key = hashlib.sha256(key.encode("utf-8")).digest()
                raw = pad(plaintext)
                iv = Random.new().read(AES.block_size)
                cipher = AES.new(p_key, AES.MODE_CBC, iv)
                hasil = base64.b64encode(iv + cipher.encrypt(raw.encode()))
                with col1:
                    st.info(bytes.decode(hasil)) 
    with col3:
        try:
            if st.button("Dekrip"):          
                inputan = plaintext
                if len(inputan) == 0:
                    with col1:
                        st.error("Masukkan Text!")
                else:
                    p_key = hashlib.sha256(key.encode("utf-8")).digest()
                    plaintext = base64.b64decode(plaintext)
                    iv = plaintext[:BS]
                    cipher = AES.new(p_key, AES.MODE_CBC, iv)
                    hasil = unpad(cipher.decrypt(plaintext[BS:]))
                    with col1:
                        st.info(bytes.decode(hasil))
        except:
                with col1:
                    st.error("Kesalahan Input")

    with st.container():
        st.header("Apa itu AES?")
        st.write("""
        AES (Advanced Encryption Standard) atau Standar Enkripsi Lanjutan merupakan standar enkripsi dengan kunci simetris yang diadopsi oleh Pemerintah Amerika Serikat. 
        Karena memiliki kemampuan dan keamanannya untuk menangani informasi rahasia. Sehingga AES dinobatkan menjadi standar industri untuk enkripsi. Sifatnya yang terbuka sehingga
        dapat digunakan untuk publik dan swasta, komersial dan nonkomersial aplikasi. 
        
        AES merupakan jenis enkripsi simetris, dimana "Simetris" berarti menggunakan kunci yang sama
        untuk mengenkripsi dan mendekripsi informasi. Selain itu, pengirim dan penerima data membutuhkan salinannya untuk mendekripsi cipher. mereka jauh lebih cepat daripada asimetris
        karena algoritma kunci simetris memerlukan daya komputasi yang lebih kecil. kunci asimetris paling baik digunakan untuk transfer file eksternal, juga lebih baik untuk enkripsi internal.
        """)

    with st.container():
        st.header("Bagaimana cara kerjanya?")
        col1,col2 = st.columns([3,1.5])

    with col1 :
        st.write("""
        AES juga sering dikenal dengan 'kode block', karena jenis sandi ini membagi informasi yang akan dienkripsi (plaintext) menjadi bagian-bagian yang disebut blok. AES menggunakan ukuran blok 128-bit,
        yang berarti data dibagi menjadi larik empat kali empat berisi 16 byte. Setiap byte berisi delapan bit. Terlepas dari itu, ukuran data terenkripsi tetap sama. Dengan kata lain, 128 bit plaintext menghasilkan 128 bit ciphertext.
        AES menggunakan Jaringan Permutasi Substitusi (SPN) algoritma yang menerapkan beberapa putaran ekspansi kunci untuk mengenkripsi data. 
        """)

    with col2:
        st.image("gambar/alur_AES.png")
    with st.container():    
        st.write("""
        Kunci awal digunakan untuk membuat serangkaian kunci baru disebut "kunci bulat".
        Dapat dikatakan bahwa, beberapa putaran modifikasi menghasilkan kunci putaran baru setiap saat. Algoritma enkripsi AES melewati beberapa putaran enkripsi. Bahkan bisa melalui 9, 11, atau 13 putaran, dimana setiap putaran melibatkan langkah yang sama. Sehingga sebuah random set karakter campur aduk itu tidak masuk akal bagi siapa saja yang tidak memiliki kunci AES.
        
        Algoritma enkripsi ini menambahkan kunci awal ke blok menggunakan Sandi XOR ("eksklusif atau"). Cipher ini adalah sebuah operasi yang dibangun ke dalam perangkat keras prosesor, dimana 
        setiap byte data adalah tersubstitusi dengan yang lain. Ketika melewati putaran pertama enkripsi AES, algoritma akan menambahkan kunci awal ke kunci putaran baru. Algoritma menggantikan setiap byte dengan kode sesuai dengan Rijndael S-box kemudian 
        akan menggeser baris dari susunan 4x4. Setiap kolom akan dikalikan dengan matriks yang telah ditentukan yang akan kembali memberi blok kode baru. Proses berlanjut beberapa kali lagi, hingga memberikan ciphertext yang sangat berbeda dari plainteks.
        """)