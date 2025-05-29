import streamlit as st
import controllers.rumus as rumus
from sympy import sympify
import numpy as np
import time


def bisection():
    st.subheader("Metode Bisection")
    st.write("Metode biseksi atau metode bagi dua adalah algoritme pencarian akar yang membagi dua selang [a,b], lalu memilih bagian selang yang berisi akar seharusnya berada untuk diproses lebih lanjut.")
    
    st.markdown(
        """
        ###### Rumus:
        $$c = \\frac{a + b}{2}$$
        
        Dimana:
        - $a$ dan $b$ adalah batas interval, 
        - $c$ adalah titik tengah yang diperiksa. 
        - Jika $f(a) \cdot f(c) < 0$, maka akar berada di interval $[a, c]$,
        - Jika $f(a) \cdot f(c) > 0$, maka akar berada di interval $[c, b]$.
        (from)
        """
    )
    
    
    # Input fungsi
    func = st.text_input("Masukkan fungsi (dalam x):", "x**2 - 4")
    
    # Input interval
    a = st.text_input("Nilai a:", value="0.0")
    a = np.float64(a)
    b = st.text_input("Nilai b:", value="5.0")
    b = np.float64(b)
    
    # Input toleransi kesalahan
    e = st.text_input("Toleransi kesalahan (e):", value="0.01")
    e = np.float64(e)
    
    hasil = st.empty()
     
    if st.button("Hitung"):
        with st.spinner("Menghitung Bisection...", show_time=True):
            time.sleep(2)
            st.success("Finish!")
        result = rumus.biseksi(a, b, func, e)
        hasil.write(f"Hasil Akar : {result}")
        
def regula_falsi():
    st.subheader("Metode Regula Falsi")
    st.write("Metode ini memanfaatkan garis lurus yang ditarik melalui dua titik pada kurva fungsi untuk memperkirakan posisi akar di mana garis itu memotong sumbu x.")
    
    st.markdown(
        """
        ###### Rumus:
        $$x = \\frac{b \\cdot f(a) - a \\cdot f(b)}{f(a) - f(b)}$$
        
        Dimana $a$ dan $b$ adalah dua titik, dan $f(a)$ serta $f(b)$ adalah nilai fungsi pada titik tersebut.
        """
    )
    
    # Input fungsi
    f_x = st.text_input("Masukkan fungsi (dalam x):", "x**2 - 4")
    
    # Input interval
    a = st.text_input("Nilai a:", value="0.0")
    a = np.float64(a)
    b = st.text_input("Nilai b:", value="5.0")
    b = np.float64(b)
    
    # Input toleransi kesalahan
    e = st.text_input("Toleransi kesalahan (e):", value="0.01")
    e = np.float64(e)
    
    hasil = st.empty()
    
    if st.button("Hitung"):
        with st.spinner("Menghitung Regula Falsi...", show_time=True):
            time.sleep(2)
            st.success("Finish!")
        result = rumus.regula_falsi(a, b, f_x, e)
        hasil.write(f"Hasil Akar : {result}")
        
def iterasi_sederhana():
    st.subheader("Metode Iterasi Sederhana")
    st.write("Metode ini memakai rumus iteratif, yaitu menggunakan hasil dari perhitungan sebelumnya untuk mendekati nilai akar secara bertahap.")
    
    st.markdown(
        """
            ###### Permasalahan: $x^2 - 2x - 3 = 0$
        """
    )
    
    st.write("Ada 3 kemungkinan yang dapat digunakan untuk menyelesaikan permasalahan di atas, yaitu:")
    
    st.markdown(
        """
            - $x = \\sqrt{2x + 3}$
            - $x = \\frac{3}{x - 2}$
            - $x = \\frac{x^2 - 3}{2}$
        """
    )
    
    x_initial = st.text_input("Nilai x awal:", value="0.0")
    x_initial = np.float64(x_initial)
    max_iter = st.number_input("Humlah Iterasi Maksimum:", value=100)
    e = st.text_input("Toleransi kesalahan (e):", value="0.01")
    e = np.float64(e)
    
    cols = st.empty()
    
    if st.button("Hitung"):
        with st.spinner("Menghitung Iterasi Sederhana...", show_time=True):
            time.sleep(2)
            st.success("Finish!")
        col1, col2, col3 = cols.columns(3)
        
        with col1:
            result1 = rumus.iterasi_sederhana(x_initial, "sqrt(2*x + 3)", e, max_iter)
            col1.metric(f"Hasil Akar (x = sqrt(2x + 3))", result1, border=True)
        with col2:
            result2 = rumus.iterasi_sederhana(x_initial, "3 / (x - 2)", e, max_iter)
            col2.metric(f"Hasil Akar (x = 3 / (x - 2))", result2, border=True)
        with col3:
            result3 = rumus.iterasi_sederhana(x_initial, "(x**2 - 3) / 2", e, max_iter)
            col3.metric(f"Hasil Akar (x = (x^2 - 3) / 2)", result3, border=True)



def newton_raphson():
    st.subheader("Metode Newton Raphson")
    st.write("Metode Newton Raphson Ini adalah metode numerik yang menemukan akar fungsi dengan memanfaatkan turunan dari fungsi tersebut dalam proses perhitungannya.")
    
    st.markdown(
        """
        ###### Rumus:
        $$x_{n+1} = x_n - \\frac{f(x_n)}{f'(x_n)}$$
        
        Dimana $f(x_n)$ adalah nilai fungsi pada $x_n$, dan $f'(x_n)$ adalah turunan pertama dari fungsi tersebut.
        """
    )
    
    # Input fungsi
    f_x = st.text_input("Masukkan fungsi (dalam x):", "x - exp(-x)")
    f_x = sympify(f_x)
    
    # Input nilai awal
    x0 = st.text_input("Nilai x awal:", value="0.0")
    x0 = np.float64(x0)
    
    # Input toleransi kesalahan
    e = st.text_input("Toleransi kesalahan (e):", value="0.00001")
    e = np.float64(e)
    
    hasil = st.empty()
    
    if st.button("Hitung"):
        with st.spinner("Menghitung Newton Raphson...", show_time=True):
            time.sleep(2)
            st.success("Finish!")
        result = rumus.newton_raphson(x0, f_x, e)
        hasil.write(f"Hasil Akar : {result}")

def secant():
    st.subheader("Metode Secant")
    st.write("Metode Secant menggunakan dua titik berbeda pada grafik fungsi untuk memperkirakan letak akar melalui pendekatan garis secant.")
    
    st.markdown(
        """
        ###### Rumus:
        $$x_{n+1} = x_n - \\frac{f(x_n) \\cdot (x_n - x_{n-1})}{f(x_n) - f(x_{n-1})}$$
        
        Dimana $x_n$ dan $x_{n-1}$ adalah dua titik yang digunakan dalam perhitungan akar.
        """
    )
        
    # Input fungsi
    f_x = st.text_input("Masukkan fungsi (dalam x):", "x**2 - 4")
    
    # Input nilai x0 & x1
    x0 = st.text_input("Nilai x0:", value="0.0")
    x0 = np.float64(x0)
    x1 = st.text_input("Nilai x1:", value="5.0")
    x1 = np.float64(x1)
    
    # Input toleransi kesalahan
    e = st.text_input("Toleransi kesalahan (e):", value="0.01")
    e = np.float64(e)
    
    hasil = st.empty()
    
    if st.button("Hitung"):
        with st.spinner("Menghitung Metode Secant...", show_time=True):
            time.sleep(2)
            st.success("Finish!")
        result = rumus.secant(x0, x1, f_x, e)
        hasil.write(f"Hasil Akar : {result}")

def credit():
    st.subheader("Penyusun dan Anggota Kelompok")
    st.write("""Terimakasih telah meluangkan waktunya untuk mengunjungi website kami! <br><br>
    - Abby Rizky Febrian (50422056) <br>
    - Afwan Apriansyah (50422111) <br>
    - Akhmal Januar Sachrir (50422150) <br>
    - Ale Bayu Prakoso (50422164) <br>
    - Ihsan Ramdani (50422694) <br><br>
        <i>Assisted by Kelompok 6</i>
    """, unsafe_allow_html=True)
    
