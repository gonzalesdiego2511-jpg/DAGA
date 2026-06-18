import streamlit as st
import pandas as pd

ARCHIVO = "Polla_Mundial_CFI.xlsx"

st.set_page_config(
    page_title="🏆 Polla Mundial CFI 2026",
    page_icon="🏆",
    layout="wide"
)

# ==========================
# TÍTULO
# ==========================

st.title("🏆 POLLA MUNDIAL CFI 2026")
st.markdown("---")

# ==========================
# TABLA DE POSICIONES
# ==========================

try:

    ranking = pd.read_excel(
        ARCHIVO,
        sheet_name="Ranking"
    )

    st.subheader("🥇 Tabla de Posiciones")

    st.dataframe(
        ranking,
        width="stretch",
        hide_index=True
    )

except Exception as e:

    st.warning(
        "No se encontró la hoja 'Ranking'"
    )

st.markdown("---")

# ==========================
# PARTIDOS
# ==========================

try:

    partidos = pd.read_excel(
        ARCHIVO,
        sheet_name="Partidos"
    )

    st.subheader("⚽ Partidos del Mundial")

    st.dataframe(
        partidos,
        width="stretch",
        hide_index=True
    )

except Exception:

    st.warning(
        "No se encontró la hoja 'Partidos'"
    )

st.markdown("---")

# ==========================
# PRONÓSTICOS
# ==========================

try:

    pronosticos = pd.read_excel(
        ARCHIVO,
        sheet_name="Pronosticos"
    )

    st.subheader("📋 Pronósticos Registrados")

    participante = st.selectbox(
        "Seleccionar participante",
        ["Todos"] + sorted(
            pronosticos["Participante"].dropna().unique().tolist()
        )
    )

    if participante != "Todos":

        pronosticos = pronosticos[
            pronosticos["Participante"] == participante
        ]

    st.dataframe(
        pronosticos,
        width="stretch",
        hide_index=True
    )

except Exception:

    st.warning(
        "No se encontró la hoja 'Pronosticos'"
    )

st.markdown("---")

# ==========================
# REGLAS
# ==========================

st.info("""
🏆 REGLAS DE LA POLLA

✅ Pronóstico acertado: 3 puntos

❌ Pronóstico incorrecto: 0 puntos

🥇 Gana quien acumule más puntos al finalizar el Mundial.
""")