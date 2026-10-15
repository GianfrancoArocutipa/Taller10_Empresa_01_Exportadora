# 05_arquitectura/AR03_brechas.py
import pandas as pd

b = pd.DataFrame([
 # capa, elemento_actual, elemento_objetivo, tipo_brecha, esfuerzo, dependencias, origen
 ("Datos","Cliente en 3 lugares sin dueño","Maestro único con dueño designado",
  "Nuevo + Migrar","Medio","—","Principio dato único · Sección 3.1.3"),
 ("Datos","Sin registro de tratamiento","Registro de actividades de tratamiento",
  "Nuevo","Bajo","—","Sección 4.1 obligación normativa"),
 ("Aplicación","Portal sin integración","Portal integrado en tiempo real",
  "Modificar","Alto","Capa de integración","Visión Sección 2.2"),
 ("Aplicación","Ruteo en hoja de cálculo","Planificación de rutas integrada",
  "Nuevo","Medio","Maestro de clientes","Estrategia E-02"),
 ("Aplicación","Integración por archivo plano","Capa de integración por servicios",
  "Nuevo","Alto","—","Principio integración por servicios"),
 ("Aplicación","Análisis en hojas de cálculo","Tablero de gestión",
  "Nuevo","Medio","Maestro de clientes; capa de integración","Estrategia E-05"),
 ("Aplicación","Atención por correo","Mesa de servicio",
  "Nuevo","Bajo","—","Sección 4.2 ITIL"),
 ("Tecnología","Servidor único","Infraestructura con respaldo verificado e inmutable",
  "Modificar","Medio","—","Sección 4.3 DSS04"),
 ("Tecnología","Plataforma en fin de soporte","Plataforma con soporte vigente",
  "Reemplazar","Alto","Capa de integración","Sección 3.3 PE-04 — plazo del fabricante"),
 ("Negocio","Sin gobierno de TI","Comité de TI con acta y periodicidad",
  "Nuevo","Bajo","—","Sección 4.3 EDM01"),
], columns=["capa","actual","objetivo","tipo_brecha","esfuerzo","dependencias","origen"])

b.to_csv("AR03_brechas.csv", index=False)
print(b.groupby(["capa","tipo_brecha"]).size().to_string())
print(f"\nBrechas totales: {len(b)}")
print(f"Esfuerzo alto: {(b.esfuerzo=='Alto').sum()} | medio: {(b.esfuerzo=='Medio').sum()} | bajo: {(b.esfuerzo=='Bajo').sum()}")

# --- Paquetes de trabajo: agrupar brechas relacionadas ---
PAQUETES = {
 "PT-01 Gobierno del dato": ["Cliente en 3 lugares sin dueño","Sin registro de tratamiento"],
 "PT-02 Capa de integración": ["Integración por archivo plano"],
 "PT-03 Canal digital": ["Portal sin integración"],
 "PT-04 Logística inteligente": ["Ruteo en hoja de cálculo"],
 "PT-05 Analítica de gestión": ["Análisis en hojas de cálculo"],
 "PT-06 Gestión de servicios de TI": ["Atención por correo"],
 "PT-07 Continuidad de infraestructura": ["Servidor único"],
 "PT-08 Renovación de plataforma": ["Plataforma en fin de soporte"],
 "PT-09 Gobierno de TI": ["Sin gobierno de TI"],
}
print("\n=== PAQUETES DE TRABAJO (insumo del portafolio Sección 7) ===")
for p, items in PAQUETES.items():
    sub = b[b.actual.isin(items)]
    dep = ", ".join(sorted({d for d in sub.dependencias if d != "—"})) or "ninguna"
    print(f"{p}\n   brechas: {len(sub)} | esfuerzo máximo: "
          f"{sub.esfuerzo.map({'Bajo':1,'Medio':2,'Alto':3}).max()} | dependencias: {dep}")

# --- Secuencia derivada de las dependencias ---
print("\n=== SECUENCIA OBLIGADA POR DEPENDENCIAS ===")
print("  1. PT-01 Gobierno del dato   (habilita PT-04 y PT-05)")
print("  2. PT-02 Capa de integración (habilita PT-03 y PT-08)")
print("  3. PT-09, PT-06, PT-07       (independientes, esfuerzo bajo/medio)")
print("  4. PT-03, PT-04, PT-05       (dependientes de 1 y 2)")
print("  5. PT-08 Renovación de plataforma (plazo límite: el anunciado por el fabricante)")
print("\n→ Esta secuencia condiciona la hoja de ruta (Sección 7.3).")
