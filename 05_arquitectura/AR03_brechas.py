import sys
import pandas as pd
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

b = pd.DataFrame([
    # capa, actual, objetivo, tipo_brecha, esfuerzo, dependencias, origen
    ("Datos", "Lote disperso en 4 sistemas sin dueño", "Maestro único de lotes con trazabilidad integral",
     "Nuevo + Migrar", "Alto", "—", "Principio 1 · Dato único y Sección 3.1.3"),
    ("Datos", "32 productores asociados fuera del ERP", "Padrón único de productores integrado al ERP",
     "Consolidar", "Medio", "—", "Principio 1 · Sección 3.1.2"),
    ("Datos", "520 trabajadores eventuales sin registro formal", "Registro automatizado y cumplimiento Ley 29733",
     "Nuevo", "Bajo", "—", "Principio 5 · Obligación normativa"),
    ("Aplicación", "Access de trazabilidad sin soporte (2014)", "Módulo corporativo de trazabilidad en ERP/MES",
     "Reemplazar", "Alto", "Maestro único de lotes", "Principio 6 · Incidente campaña 2024"),
    ("Aplicación", "Balanza en PC aislada con transcripción manual", "Integración automática balanza-ERP por servicio",
     "Nuevo", "Medio", "Capa de red y servicios", "Principio 3 · Cero digitación duplicada"),
    ("Aplicación", "Trazabilidad por lote en Excel por campaña", "Control de calidad y lotes en línea",
     "Reemplazar", "Medio", "Módulo corporativo de trazabilidad", "Estrategia E-01 · Trazabilidad SENASA"),
    ("Aplicación", "Cálculo de costo/tonelada en Excel de Finanzas", "Costeo estándar automático en ERP contable",
     "Modificar", "Medio", "Maestro único de lotes", "Estrategia E-03 · Control de costos"),
    ("Aplicación", "Consola de riego aislada sin exportación", "Conector de telemetría de campo al ERP",
     "Nuevo", "Bajo", "Capa de red y servicios", "Principio 3 · Eficiencia hídrica"),
    ("Aplicación", "Integración por libros Excel a planillas", "Servicio web seguro con proveedor de nóminas",
     "Modificar", "Bajo", "—", "Principio 5 · Seguridad de datos"),
    ("Tecnología", "Servidor único en oficina con UPS de 10 min", "Infraestructura híbrida con alta disponibilidad",
     "Modificar", "Alto", "—", "Principio 4 · COBIT DSS04"),
    ("Tecnología", "PC de planta con Access en riesgo físico", "Terminales industriales ligeros centralizados",
     "Reemplazar", "Medio", "Módulo corporativo de trazabilidad", "Principio 4 · Incidente campaña 2024"),
    ("Tecnología", "Red plana y enlace monoproveedor", "VLANs segmentadas y enlace redundante",
     "Nuevo", "Medio", "—", "Sección 4.2 · Seguridad de redes"),
    ("Negocio", "Sin Comité de TI ni políticas aprobadas", "Comité de TI formal con sesiones y políticas",
     "Nuevo", "Bajo", "—", "COBIT 2019 EDM01 · Gobierno de TI"),
], columns=["capa", "actual", "objetivo", "tipo_brecha", "esfuerzo", "dependencias", "origen"])

# Exportar a CSV
b.to_csv("05_arquitectura/AR03_brechas.csv", index=False)
print("=== CONTEO DE BRECHAS POR CAPA Y TIPO ===")
print(b.groupby(["capa", "tipo_brecha"]).size().to_string())
print(f"\nBrechas totales identificadas: {len(b)}")
print(f"Esfuerzo alto: {(b.esfuerzo=='Alto').sum()} | medio: {(b.esfuerzo=='Medio').sum()} | bajo: {(b.esfuerzo=='Bajo').sum()}")

# --- Paquetes de trabajo: agrupar brechas relacionadas ---
PAQUETES = {
    "PT-01 Gobierno y Calidad del Dato Maestro": [
        "Lote disperso en 4 sistemas sin dueño",
        "32 productores asociados fuera del ERP",
        "520 trabajadores eventuales sin registro formal"
    ],
    "PT-02 Sistema Integrado de Trazabilidad y Producción": [
        "Access de trazabilidad sin soporte (2014)",
        "Trazabilidad por lote en Excel por campaña",
        "PC de planta con Access en riesgo físico"
    ],
    "PT-03 Automatización de Pesaje y Telemetría Industrial": [
        "Balanza en PC aislada con transcripción manual",
        "Consola de riego aislada sin exportación"
    ],
    "PT-04 Infraestructura, Respaldo y Continuidad": [
        "Servidor único en oficina con UPS de 10 min",
        "Red plana y enlace monoproveedor"
    ],
    "PT-05 Integración Financiera, Costos y Nómina": [
        "Cálculo de costo/tonelada en Excel de Finanzas",
        "Integración por libros Excel a planillas"
    ],
    "PT-06 Gobierno de TI, Políticas y Protección de Datos": [
        "Sin Comité de TI ni políticas aprobadas"
    ],
}

print("\n=== PAQUETES DE TRABAJO (insumo del portafolio Sección 7) ===")
for p, items in PAQUETES.items():
    sub = b[b.actual.isin(items)]
    dep = ", ".join(sorted({d for d in sub.dependencias if d != "—"})) or "ninguna"
    max_esf = sub.esfuerzo.map({"Bajo": 1, "Medio": 2, "Alto": 3}).max()
    esf_str = {1: "Bajo", 2: "Medio", 3: "Alto"}.get(max_esf, "Medio")
    print(f"\n{p}")
    print(f"   Brechas asignadas: {len(sub)} | Esfuerzo máximo: {esf_str} | Dependencias: {dep}")

# --- Secuencia derivada de las dependencias ---
print("\n=== SECUENCIA OBLIGADA POR DEPENDENCIAS ===")
print("  Fase 1 (Habilitadores Críticos):")
print("    • PT-01 Gobierno y Calidad del Dato Maestro (habilita trazabilidad y costeo)")
print("    • PT-04 Infraestructura, Respaldo y Continuidad (habilita estabilidad y conectividad de planta)")
print("    • PT-06 Gobierno de TI, Políticas y Protección de Datos (independiente, esfuerzo bajo)")
print("  Fase 2 (Soluciones Core y Automatización):")
print("    • PT-02 Sistema Integrado de Trazabilidad y Producción (depende de PT-01 y PT-04)")
print("    • PT-03 Automatización de Pesaje y Telemetría Industrial (depende de conectividad de PT-04)")
print("  Fase 3 (Optimización y Consolidación Financiera):")
print("    • PT-05 Integración Financiera, Costos y Nómina (depende de lotes de PT-01 y producción de PT-02)")
print("\n→ Esta secuencia condiciona estrictamente la hoja de ruta de la Sección 7.3 del PETI.")
