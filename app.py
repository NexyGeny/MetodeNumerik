import streamlit as st
import views.displayhalaman as views
from streamlit_lottie import st_lottie
import json

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
# Load file Animasi
with open("assets/Animasi.json") as anim_file:
    anim_data = json.load(anim_file)
st_lottie(anim_data, speed=1, width=300, height=300)

# Load animasi
lottie_animation = load_lottie("assets/Animasi.json")

# CSS
st.markdown("""
    <style>
        .stApp {
            background-color: ffffff;
        }
        .stButton > button {
            background-color: #959890;
            color: warm-white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 20px;
        }
        .stSelectbox > div {
            border-radius: 8px;
        }
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("Main Menu")
    homepage_clicked = st.button("Homepage")
    SELECTION = st.selectbox(
        "Metode Numerik:",
        ("Pilih Metode","Bisection", "Regula Falsi", "Iterasi Sederhana", "Newton Raphson", "Secant","Credit")
    )
    st.markdown("---")
    st.markdown("Made with <3 by Kelompok 5")

# Main content
if homepage_clicked or 'first_load' not in st.session_state:
    st.session_state.first_load = False
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("Welcome!")
        st.markdown(
            """
            <div style='font-size:20px;'>
            Website ini akan membantu anda dalam mencari jawaban Metode Numerik. <br>
            Metode Numerik yang disediakan adalah beberapa metode yang digunakan dalam mencari akar! <br><br>
            Pilih salah satu metode di sidebar untuk mulai menghitung.
            </div>
            """, unsafe_allow_html=True
        )
    with col2:
        st_lottie(lottie_animation, height=300)
else:
    st.title(f"🔧 {SELECTION}")
    with st.container():
        if SELECTION == "Bisection":
            st.markdown("### 🔪 Metode Bisection")
            views.bisection()
        elif SELECTION == "Regula Falsi":
            st.markdown("### 🎃 Metode Regula Falsi")
            views.regula_falsi()
        elif SELECTION == "Iterasi Sederhana":
            st.markdown("### 🔄 Metode Iterasi Sederhana")
            views.iterasi_sederhana()
        elif SELECTION == "Newton Raphson":
            st.markdown("### ⚡ Metode Newton Raphson")
            views.newton_raphson()
        elif SELECTION == "Secant":
            st.markdown("### ➗ Metode Secant")
            views.secant()
        elif SELECTION == "Credit":
            st.markdown("### 📕 Credit Page")
            views.credit()
        elif SELECTION == "Pilih Metode":
            pass

# Footer
st.markdown("""
    <hr>
    <div style='text-align:center; font-size:14px;'>
        🌟 Dibuat dengan Streamlit oleh Kelompok 5 assisted by Kelompok 6  |  2025 
        Untuk memenuhi mata kuliah Rekayasa Komputasional🌟
    </div>
""", unsafe_allow_html=True)
