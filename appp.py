import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import requests
import time

# -------------------------
# CONFIG
# -------------------------
st.set_page_config(page_title="Air System", layout="wide")

# -------------------------
# SPLASH SCREEN (PANTALLA INICIAL)
# -------------------------
placeholder = st.empty()

with placeholder.container():
    st.markdown("""
    <div style="
        background-color: #f5f5dc;
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        ">
        <h1 style="color:black;">🌱 Air System</h1>
        <p style="color:black;">by Joss Mireles</p>
    </div>
    """, unsafe_allow_html=True)

time.sleep(2)
placeholder.empty()

# -------------------------
# ESTILO PRO
# -------------------------
st.markdown("""
<style>
body {
    background-color: #0b1220;
    color: white;
}
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------
st.markdown("# 🌱 Sistema Inteligente de Aire")
st.markdown("Monitoreo en tiempo real + simulación ambiental basada en algas")
st.markdown("---")

# -------------------------
# AQI
# -------------------------
col1, col2, col3 = st.columns(3)

try:
    url = "https://api.waqi.info/feed/mexico/?token=demo"
    data = requests.get(url).json()
    aqi = data["data"]["aqi"]
except:
    aqi = 80

col1.metric("🌍 AQI actual", aqi)
col2.metric("CO₂ estimado", 120)
col3.metric("Oxígeno generado", 35)

# -------------------------
# LAYOUT
# -------------------------
left, right = st.columns([1,2])

with left:
    st.markdown("### ⚙️ Control")

    co2_inicial = st.slider("CO₂ inicial", 50, 200, 100)
    luz = st.slider("Luz", 0.0, 1.0, 0.8)
    eficiencia = st.slider("Eficiencia", 0.01, 0.1, 0.06)

with right:
    dias = np.linspace(0, 30, 100)
    tasa = luz * eficiencia

    co2 = co2_inicial * np.exp(-tasa * dias)
    oxigeno = co2_inicial - co2

    fig, ax = plt.subplots()
    ax.plot(dias, co2, linewidth=3)
    ax.plot(dias, oxigeno, linewidth=3)

    ax.set_title("Simulación")
    ax.grid(True)

    st.pyplot(fig)

# -------------------------
# IMPACTO
# -------------------------
st.markdown("---")
st.markdown("### 🌍 Impacto")

personas = int(oxigeno[-1] / 5)
st.write(f"Impacto estimado: {personas} personas")

# -------------------------
# FOOTER
# -------------------------
st.markdown("---")
st.markdown("<center>Desarrollado por Joss Mireles</center>", unsafe_allow_html=True)
  

