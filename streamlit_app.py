import streamlit as st

st.title("Selamat datang di Website Informatika")
st.image("4f95e729-156e-4f3d-959b-a00141376126.jpeg", width=200)
st.write("\n")
st.subheader("Savaira Aurellia Fatah")
st.write(
        Mari bekerja sama dalam sekelas membuat Website melalui Github dan  

#with col1:
st.header ("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:" , value=0, step=1)

if (angka % 2) == 0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah Bilangan Ganjil")
