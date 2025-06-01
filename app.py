import streamlit as st
from streamlit_lottie import st_lottie
import json
import views.displayhalaman as views

# Load Lottie file
def load_lottie(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Setup page
st.set_page_config(
    page_title="Metode Numerik | Computer Engineer",
    page_icon="🗿",
    layout="wide",
)

# Load animation
lottie_animation = load_lottie("assets/Animasi.json")

# Custom CSS
st.markdown("""
    <style>
        .stApp {
            background-color: #0e1117;
        }
        .stButton > button {
            background-color: #959890;
            color: #fff;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 18px;
            margin: 3px;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }
        .stButton > button:hover {
            background-color: #6c6f66;
            transform: scale(1.05);
        }
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Header & Animation
st_lottie(lottie_animation, speed=1, width=300, height=300)
st.title("Main Menu")

# Top row buttons: Home & Credit
col_home, col_credit, _ = st.columns([1, 1, 6])

with col_home:
    if st.button("🏠 Home"):
        st.session_state.page = "home"

with col_credit:
    if st.button("📕 Credit"):
        st.session_state.page = "credit"

# Numerical methods section
st.markdown("### Pilih Metode Numerik:")

col1, col2, col3 = st.columns(3, gap="small")

with col1:
    if st.button("🔪 Bisection"):
        st.session_state.page = "bisection"
    if st.button("🎃 Regula Falsi"):
        st.session_state.page = "regula_falsi"

with col2:
    if st.button("🔄 Iterasi Sederhana"):
        st.session_state.page = "iterasi_sederhana"
    if st.button("⚡ Newton Raphson"):
        st.session_state.page = "newton_raphson"

with col3:
    if st.button("➗ Secant"):
        st.session_state.page = "secant"

# Page content logic
if 'page' not in st.session_state or st.session_state.page == "home":
    col_left, col_right = st.columns([2, 1])
    with col_left:
        st.header("Welcome!")
        st.markdown(
            """
            <div style='font-size:18px; color:#fff;'>
            Website ini membantu Anda menyelesaikan soal Metode Numerik.<br>
            Tersedia beberapa metode populer untuk mencari akar persamaan!<br><br>
            Klik salah satu metode di atas untuk mulai menghitung.
            </div>
            """, unsafe_allow_html=True
        )
    with col_right:
        st_lottie(lottie_animation, height=300)

elif st.session_state.page == "bisection":
    st.header("🔪 Metode Bisection")
    views.bisection()

elif st.session_state.page == "regula_falsi":
    st.header("🎃 Metode Regula Falsi")
    views.regula_falsi()

elif st.session_state.page == "iterasi_sederhana":
    st.header("🔄 Metode Iterasi Sederhana")
    views.iterasi_sederhana()

elif st.session_state.page == "newton_raphson":
    st.header("⚡ Metode Newton Raphson")
    views.newton_raphson()

elif st.session_state.page == "secant":
    st.header("➗ Metode Secant")
    views.secant()

elif st.session_state.page == "credit":
    st.header("📕 Credit Page")
    views.credit()

# Footer
st.markdown("""
    <hr>
    <div style='text-align:center; font-size:14px; color:#fff;'>
        🌟 Dibuat dengan Streamlit oleh Kelompok 5 | 2025<br>
        Untuk memenuhi mata kuliah Rekayasa Komputasional 🌟
    </div>
""", unsafe_allow_html=True)
