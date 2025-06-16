
import pandas as pd

def calcular_kpis(df):
    cobre_total = df["Cobre"].sum()
    n_proyectos = df["Región"].nunique()
    conflictos = 2  # Simulación
    return {
        "cobre_total": cobre_total,
        "n_proyectos": n_proyectos,
        "conflictos": conflictos
    }
