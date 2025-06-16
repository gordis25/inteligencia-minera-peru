
def generar_alertas(noticias):
    claves = ["bloqueo", "huelga", "protesta", "retraso", "impacto"]
    alertas = []
    for n in noticias:
        if any(c in n.lower() for c in claves):
            alertas.append(f"⚠️ {n.strip()}")
    return alertas
