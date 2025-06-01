import streamlit as st
import controllers.rumus as rumus
import pandas as pd
from sympy import sympify

def bisection():
    f_x_input = st.text_input("Fungsi (misal: x**3 - x - 2)", value="x**3 - x - 2")
    a = st.number_input("Batas bawah (a)", value=1.0)
    b = st.number_input("Batas atas (b)", value=2.0)
    toleransi = st.number_input("Toleransi", value=1e-5)

    if st.button("Hitung Bisection"):
        f_x = sympify(f_x_input)
        hasil, tabel = rumus.biseksi(a, b, f_x, toleransi)
        st.success(f"Akar ditemukan: {hasil}")
        st.dataframe(pd.DataFrame(tabel))

def regula_falsi():
    f_x_input = st.text_input("Fungsi (misal: x**3 - x - 2)", value="x**3 - x - 2")
    a = st.number_input("Batas bawah (a)", value=1.0)
    b = st.number_input("Batas atas (b)", value=2.0)
    toleransi = st.number_input("Toleransi", value=1e-5)

    if st.button("Hitung Regula Falsi"):
        f_x = sympify(f_x_input)
        hasil, tabel = rumus.regula_falsi(a, b, f_x, toleransi)
        st.success(f"Akar ditemukan: {hasil}")
        st.dataframe(pd.DataFrame(tabel))

def iterasi_sederhana():
    f_x_input = st.text_input("Fungsi g(x) untuk x = g(x)", value="cos(x)")
    x_awal = st.number_input("Tebakan awal (x0)", value=1.0)
    toleransi = st.number_input("Toleransi", value=1e-5)

    if st.button("Hitung Iterasi Sederhana"):
        f_x = sympify(f_x_input)
        hasil, tabel = rumus.iterasi_sederhana(x_awal, f_x, toleransi)
        st.success(f"Akar ditemukan: {hasil}")
        st.dataframe(pd.DataFrame(tabel))

def newton_raphson():
    f_x_input = st.text_input("Fungsi f(x)", value="x**3 - x - 2")
    x_awal = st.number_input("Tebakan awal (x0)", value=1.0)
    toleransi = st.number_input("Toleransi", value=1e-5)

    if st.button("Hitung Newton-Raphson"):
        f_x = sympify(f_x_input)
        hasil, tabel = rumus.newton_raphson(x_awal, f_x, toleransi)
        st.success(f"Akar ditemukan: {hasil}")
        st.dataframe(pd.DataFrame(tabel))

def secant():
    f_x_input = st.text_input("Fungsi f(x)", value="x**3 - x - 2")
    x_prev = st.number_input("x-1 (nilai sebelumnya)", value=0.0)
    x_curr = st.number_input("x0 (nilai sekarang)", value=1.0)
    toleransi = st.number_input("Toleransi", value=1e-5)

    if st.button("Hitung Secant"):
        f_x = sympify(f_x_input)
        hasil, tabel = rumus.secant(x_prev, x_curr, f_x, toleransi)
        st.success(f"Akar ditemukan: {hasil}")
        st.dataframe(pd.DataFrame(tabel))

def credit():
    st.markdown("""
    ### Dibuat oleh Kelompok 5 untuk mata kuliah Rekayasa Komputasional.
    - Abby Rizky Febrian (50422056)
    - Afwan Apriansyah (50422111)
    - Akhmal Jannuar Sachrir (50422150)
    - Ale Bayu Prakoso (50422164)
    - Ihsan Ramdani (50422694)
    - Raafi Ferdiansyah (51422308)
    """)