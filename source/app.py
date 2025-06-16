
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.alertas import generar_alertas
from utils.indicadores import calcular_kpis

st.set_page_config(page_title="Inteligencia Minera Perú", layout="wide")

st.title("🛠️ Panel de Inteligencia Minera – Perú")
st.markdown("Versión MVP con visión sectorial, benchmarking y alertas.")

produccion = pd.read_csv("data/produccion.csv")
conflictos = pd.read_csv("data/conflictos.csv")
benchmark = pd.DataFrame({
    "País": ["Perú", "Chile", "Australia"],
    "Costo Producción ($/ton)": [5200, 4800, 4600],
    "Tiempo Aprobación (meses)": [18, 12, 10],
    "Ranking Fraser": [25, 10, 8]
})

kpis = calcular_kpis(produccion)
col1, col2, col3 = st.columns(3)
col1.metric("Producción total Cu", f"{kpis['cobre_total']} Tn")
col2.metric("Proyectos activos", kpis['n_proyectos'])
col3.metric("Conflictos activos", kpis['conflictos'])

st.subheader("📊 Evolución de Producción por Mineral")
fig = px.line(produccion, x="Año", y="Cobre", color="Región", title="Cobre por región")
st.plotly_chart(fig, use_container_width=True)

st.subheader("🌎 Benchmark Internacional")
st.dataframe(benchmark)

st.subheader("🚨 Alertas de Coyuntura Global")
with open("data/alertas.txt", "r") as f:
    noticias = f.readlines()
    alertas = generar_alertas(noticias)
    for alerta in alertas:
        st.error(alerta)
