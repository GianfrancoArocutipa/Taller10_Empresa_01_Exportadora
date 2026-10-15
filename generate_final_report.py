# generate_final_report.py
# Generación completa del informe formal para el Taller 10
# Caso: Agroexportadora Valle Viejo S.A.C.
# Autor: Gianfranco Arocutipa Arocutipa (2023076790)

import os
import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

REPO_URL = "https://github.com/GianfrancoArocutipa/Taller10_ArocutipaGianfranco/tree/taller-10"

def set_cell_background(cell, hex_color):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def style_table_header(row, col_widths, bg_color='1F4E79'):
    for i, cell in enumerate(row.cells):
        set_cell_background(cell, bg_color)
        set_cell_margins(cell, top=120, bottom=120, left=150, right=150)
        cell.width = col_widths[i]
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in p.runs:
                run.font.bold = True
                run.font.color.rgb = RGBColor(255, 255, 255)
                run.font.size = Pt(9)
                run.font.name = 'Calibri'

def add_styled_heading(doc, text, level):
    p = doc.add_paragraph()
    p.style = f'Heading {level}'
    run = p.add_run(text)
    run.font.name = 'Calibri'
    run.font.bold = True
    if level == 1:
        run.font.size = Pt(14)
        run.font.color.rgb = RGBColor(22, 40, 92) # Navy
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
    elif level == 2:
        run.font.size = Pt(12)
        run.font.color.rgb = RGBColor(31, 78, 121)
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
    elif level == 3:
        run.font.size = Pt(10.5)
        run.font.color.rgb = RGBColor(41, 128, 185)
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
    return p

def add_body_p(doc, text, bold_prefix="", italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Calibri'
        r_pre.font.size = Pt(10)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(30, 41, 59)
    run = p.add_run(text)
    run.font.name = 'Calibri'
    run.font.size = Pt(10)
    run.font.italic = italic
    run.font.color.rgb = RGBColor(51, 65, 85)
    return p

def add_bullet_p(doc, text, bold_prefix=""):
    p = doc.add_paragraph(style='Compact')
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    r_bullet = p.add_run("• ")
    r_bullet.font.name = 'Calibri'
    r_bullet.font.size = Pt(10)
    r_bullet.font.bold = True
    r_bullet.font.color.rgb = RGBColor(31, 78, 121)
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Calibri'
        r_pre.font.size = Pt(10)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(15, 23, 42)
    run = p.add_run(text)
    run.font.name = 'Calibri'
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(51, 65, 85)
    return p

print("Abriendo plantilla...")
doc = Document('SI886-PLANTILLA-TALLER (3).docx')

# 1. Modificar Carátula
for p in doc.paragraphs:
    if "“…………………………………………….”" in p.text:
        p.text = "“TALLER 10: MODELADO DE LA ARQUITECTURA ACTUAL Y OBJETIVO EN ARCHI”\n(CASO: AGROEXPORTADORA VALLE VIEJO S.A.C.)"
        for r in p.runs:
            r.font.name = 'Calibri'
            r.font.size = Pt(13)
            r.font.bold = True
            r.font.color.rgb = RGBColor(22, 40, 92)
    elif "“………………………….”" in p.text:
        p.text = "“PLANEAMIENTO ESTRATÉGICO DE TECNOLOGÍAS DE LA INFORMACIÓN”"
        for r in p.runs:
            r.font.name = 'Calibri'
            r.font.size = Pt(11)
            r.font.bold = True
    elif "APELLIDOS Y NOMBRES · CÓDIGO" in p.text:
        p.text = "AROCUTIPA AROCUTIPA, GIANFRANCO · 2023076790"
        for r in p.runs:
            r.font.name = 'Calibri'
            r.font.size = Pt(11)
            r.font.bold = True
    elif "DR. OSCAR JUAN JIMENEZ FLORES" in p.text or "DR. OSCAR JUAN JIMENEZ FLORES" in p.text:
        p.text = "DR. OSCAR JUAN JIMENEZ FLORES"
        for r in p.runs:
            r.font.name = 'Calibri'
            r.font.size = Pt(11)
            r.font.bold = True
    elif "TACNA — PERÚ" in p.text:
        p.text = "TACNA — PERÚ\n2026"
        for r in p.runs:
            r.font.name = 'Calibri'
            r.font.size = Pt(11)

print("Carátula lista.")

# Ubicar dónde termina 'Cómo se usa esta plantilla' y empieza '1. Información sobre el evento práctico'
# Borramos el contenido existente desde la sección 1 para reescribirlo de manera completa, impecable y rigurosa.
# Buscamos el párrafo con "1. Información sobre el evento práctico"
start_idx = None
for i, p in enumerate(doc.paragraphs):
    if "1. Información sobre el evento práctico" in p.text:
        start_idx = i
        break

if start_idx is not None:
    print(f"Limpiando plantilla desde párrafo {start_idx}...")
    # Eliminamos los párrafos y tablas posteriores para poblar el documento con el contenido completo
    # Primero removemos las tablas que estaban en la plantilla
    for t in list(doc.tables):
        t._element.getparent().remove(t._element)
    
    # Removemos párrafos desde start_idx
    total_p = len(doc.paragraphs)
    for _ in range(total_p - start_idx):
        p_to_del = doc.paragraphs[-1]
        p_to_del._element.getparent().remove(p_to_del._element)

print("Escribiendo contenido detallado del informe...")

# ==========================================
# SECCIÓN 1: INFORMACIÓN SOBRE EL EVENTO PRÁCTICO
# ==========================================
add_styled_heading(doc, "1. Información sobre el evento práctico", level=1)

add_styled_heading(doc, "1.1 Título del evento práctico", level=2)
add_body_p(doc, "Taller de Laboratorio 10 · Modelado de la arquitectura actual y objetivo en Archi (Caso: Agroexportadora Valle Viejo S.A.C.)")

add_styled_heading(doc, "1.2 Objetivos", level=2)
add_bullet_p(doc, "Declarar los principios de arquitectura empresarial que gobernarán las decisiones del Plan Estratégico de TI, fundamentados en TOGAF Standard 10th Edition.")
add_bullet_p(doc, "Modelar la arquitectura actual (As-Is) en sus tres capas (Negocio, Aplicación y Tecnología) utilizando el estándar ArchiMate 3.2.")
add_bullet_p(doc, "Construir la vista de cooperación proceso-aplicación e identificar con precisión matemática los procesos de la cadena de valor sin soporte o con soporte deficiente.")
add_bullet_p(doc, "Construir la estructura de la información con fuentes autoritativas, dueños de dato por cargo, discrepancias observadas y categorización de datos personales bajo la Ley N° 29733.")
add_bullet_p(doc, "Modelar la arquitectura objetivo (To-Be) derivada de la visión del plan y de las capacidades requeridas, con cada cambio trazado a su origen.")
add_bullet_p(doc, "Ejecutar el análisis de brechas mediante script automatizado en Python y derivar los paquetes de trabajo con su secuencia obligada por dependencias.")
add_bullet_p(doc, "Redactar formalmente la Sección 5 (Arquitectura Empresarial) del PETI para su incorporación en la versión v0.10.")

add_styled_heading(doc, "1.3 Tiempo de duración", level=2)
add_body_p(doc, "100 minutos")

add_styled_heading(doc, "1.4 Resultados de aprendizaje", level=2)
add_bullet_p(doc, "Aplica formalmente los conceptos y notaciones de ArchiMate 3.2 para representar las interacciones entre procesos de negocio, aplicaciones, datos y tecnología en una empresa agroexportadora.")
add_bullet_p(doc, "Identifica y formaliza los componentes de software de la organización, incorporando de manera explícita las hojas de cálculo operativas que funcionan como sistemas críticos (Shadow IT).")
add_bullet_p(doc, "Diagnostica inconsistencias y dispersión de datos maestros, estableciendo fuentes autoritativas y asignando custodios formales por cargo directivo.")
add_bullet_p(doc, "Formula paquetes de trabajo ejecutables a partir de matrices de brechas y calcula la ruta de migración obligada por dependencias técnicas.")

add_styled_heading(doc, "1.5 Recursos", level=2)
add_body_p(doc, "Para el desarrollo del presente taller práctico se emplearon los siguientes recursos tecnológicos, normativos y documentales:")

# Tabla de Recursos
recursos_data = [
    ["Archi (ArchiMate Tool)", "5.4.x", "Modelador libre ArchiMate 3.2 para la construcción y exportación de las vistas As-Is y To-Be en las tres capas."],
    ["Python & pandas", "3.13 / 2.2+", "Automatización del cálculo de brechas, agrupación en paquetes de trabajo y secuencia obligada en '05_arquitectura/AR03_brechas.py'."],
    ["Repositorio GitHub", "Git 2.x / Tag taller-10", f"Control de versiones oficial y aseguramiento de evidencias enlazadas: {REPO_URL}"],
    ["Ficha Institucional", "Edición 2026 (7 pp.)", "Fuente primaria con hechos verificables, incidentes del periodo, riesgos conocidos y estructura de Agroexportadora Valle Viejo S.A.C."],
    ["Inventario de Arquitectura Actual", "14/07/2026 (Restringido)", "Inventario técnico con aplicaciones, hojas de cálculo operativas, integraciones manuales, entidades de datos y topología de red."],
    ["TOGAF Standard", "10.ª Edición", "Marco de arquitectura empresarial, fases B, C, D (Sistemas), E (Oportunidades) y F (Migración) del método ADM."],
    ["ArchiMate 3.2 Specification", "The Open Group", "Estándar formal de modelado visual para relaciones de servicio, asignación, acceso y realización."],
    ["COBIT 2019 Framework", "ISACA (APO03, DSS04)", "Buenas prácticas de gestión de arquitectura empresarial y continuidad operativa/respaldo inmutable."],
]

t_rec = doc.add_table(rows=1, cols=3)
t_rec.alignment = WD_TABLE_ALIGNMENT.CENTER
t_rec.autofit = False
col_widths_rec = [Inches(1.8), Inches(1.1), Inches(3.6)]
style_table_header(t_rec.rows[0], col_widths_rec)
t_rec.rows[0].cells[0].paragraphs[0].text = "Recurso"
t_rec.rows[0].cells[1].paragraphs[0].text = "Versión"
t_rec.rows[0].cells[2].paragraphs[0].text = "Para qué se usó"
style_table_header(t_rec.rows[0], col_widths_rec)

for r in recursos_data:
    row = t_rec.add_row()
    for i, (cell, val) in enumerate(zip(row.cells, r)):
        cell.width = col_widths_rec[i]
        set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
        p = cell.paragraphs[0]
        run = p.add_run(val)
        run.font.name = 'Calibri'
        run.font.size = Pt(8.5)
        if i == 0:
            run.font.bold = True

add_styled_heading(doc, "1.6 Seguridad", level=2)
add_bullet_p(doc, "El modelo de arquitectura empresarial describe la superficie tecnológica completa de Agroexportadora Valle Viejo S.A.C. Por tratarse de información de clasificación Restringida, no se divulgan rutas internas, credenciales de acceso ni direcciones IP.")
add_bullet_p(doc, "Se omitieron del informe versiones exactas de componentes vulnerables y nombres de usuario administrativo para evitar vectores de ataque.")
add_bullet_p(doc, "El archivo nativo del modelo '.archimate' y los datasets se resguardan en el repositorio del equipo bajo control de versiones seguro y no se publican en wikis abiertas.")

# ==========================================
# SECCIÓN 2: PROCEDIMIENTO O METODOLOGÍA
# ==========================================
add_styled_heading(doc, "2. Procedimiento o metodología", level=1)
add_body_p(doc, "Cada paso metodológico detalla el objetivo perseguido, el comando o acción ejecutada y la evidencia verificable de funcionamiento, permitiendo la total reproducibilidad del proceso.")

# Paso A
add_styled_heading(doc, "Paso A — Declarar los principios de arquitectura", level=2)
add_bullet_p(doc, "Definir las reglas directrices obligatorias que gobernarán las decisiones del PETI de Agroexportadora Valle Viejo S.A.C., articuladas con los hallazgos del diagnóstico, los incidentes conocidos y los riesgos no tratados.", bold_prefix="Qué se buscaba: ")
add_bullet_p(doc, f"Redacción formal de '05_arquitectura/AR01_principios.md', definiendo seis principios bajo el estándar TOGAF (Nombre, Declaración, Razón, Implicancias y Trazabilidad). Enlace verificable en GitHub: {REPO_URL}/05_arquitectura/AR01_principios.md", bold_prefix="Comando o acción: ")
add_bullet_p(doc, "Seis principios formulados e incorporados a la Sección 5.1 del PETI:", bold_prefix="Evidencia de que funcionó: ")

principios_resumen = [
    ("Principio 1 · Dato único con dueño (MDM):", " Cada entidad crítica (Lote, Productor, Pesaje) posee una única fuente autoritativa en el ERP y un dueño por cargo directivo (Gerencia de Producción / Jefatura de Compras). Razón: discrepancia de hasta 6% en kilos por lote y 32 productores no registrados en el ERP."),
    ("Principio 2 · Trazabilidad integral automatizada (Field-to-Fork):", " Registro en tiempo real desde la recepción de la aceituna hasta el embarque aduanero sin digitación manual. Razón: exigencia SENASA y clientes de Europa; el cierre de trazabilidad tardaba 11 días."),
    ("Principio 3 · Integración por servicios e interfaces estandarizadas:", " Interconexión mediante APIs REST y servicios web, erradicando la digitación manual diferida entre la balanza, el ERP y planillas. Razón: la balanza se transcribía en papel al día siguiente."),
    ("Principio 4 · Continuidad operativa, respaldo inmutable y recuperación verificada:", " Alta disponibilidad, respaldo inmutable en la nube (RPO ≤ 1h, RTO ≤ 4h) y UPS corporativo. Razón: servidor único con UPS de 10 min y pérdida de la base de datos de campaña 2024 en la PC de planta."),
    ("Principio 5 · Seguridad, privacidad y cumplimiento legal desde el diseño:", " Autenticación individual nominal (cero cuentas compartidas), control RBAC y Registro de Actividades de Tratamiento de Datos Personales (Ley N° 29733). Razón: 520 trabajadores eventuales sin registro formal."),
    ("Principio 6 · Soluciones estándar antes que desarrollos propios frágiles:", " Priorización de módulos comerciales del ERP con soporte oficial. Razón: el sistema crítico de trazabilidad descansaba en un Access 2014 artesanal sin soporte desde hace una década."),
]
for p_title, p_desc in principios_resumen:
    p_pr = doc.add_paragraph(style='Compact')
    p_pr.paragraph_format.left_indent = Inches(0.25)
    r_t = p_pr.add_run(p_title)
    r_t.font.name = 'Calibri'
    r_t.font.size = Pt(9)
    r_t.font.bold = True
    r_d = p_pr.add_run(p_desc)
    r_d.font.name = 'Calibri'
    r_d.font.size = Pt(9)

# Paso B
add_styled_heading(doc, "Paso B — Modelar la arquitectura actual (As-Is)", level=2)
add_bullet_p(doc, "Modelar integralmente la situación tecnológica actual de Agroexportadora Valle Viejo S.A.C. en sus tres capas (Negocio, Aplicación y Tecnología), evidenciando las hojas de cálculo operativas, la estructura de la información y la matriz de cooperación proceso-aplicación.", bold_prefix="Qué se buscaba: ")
add_bullet_p(doc, f"Análisis del inventario 'arquitectura-actual.md', estructuración de '05_arquitectura/AR02_entidades.csv' y modelado del archivo formal ArchiMate 'anexos/anexo_A_modelo_arquitectura.archimate'. Enlace: {REPO_URL}/05_arquitectura/AR02_entidades.csv", bold_prefix="Comando o acción: ")
add_bullet_p(doc, "Modelado riguroso de las capas y componentes de la organización:", bold_prefix="Evidencia de que funcionó: ")

add_body_p(doc, "• Capa de Negocio: Se modelaron los 6 procesos de la cadena de valor (Recepción y pesaje, Proceso y envasado, Control de calidad y trazabilidad, Exportación, Compras a productores y Gestión de riego), los actores (Productores, Operarios, Responsable de calidad, SENASA) y servicios de negocio.", bold_prefix="B.1 Capa de Negocio: ")
add_body_p(doc, "• Capa de Aplicación: Se modelaron los sistemas formales (ERP comercial, Access 2014 sin soporte, software de balanza, consola web de riego y SaaS de planillas). Siguiendo las directrices del taller, se modelaron obligatoriamente como componentes de aplicación las 3 hojas de cálculo críticas: 1) Trazabilidad por lote (Excel de campaña en planta), 2) Costo por tonelada (Excel de Finanzas), y 3) Programación de riego (Excel de campo). Omitirlas hubiera generado un modelo ficticio.", bold_prefix="B.2 Capa de Aplicación: ")
add_body_p(doc, "• Capa de Tecnología: Se modeló el servidor único on-premise del ERP (con UPS de solo 10 min), la PC de balanza sin conexión de red, la PC de planta en ambiente corrosivo, la red LAN plana de oficina sin segmentación y el enlace inalámbrico monoproveedor.", bold_prefix="B.3 Capa de Tecnología: ")

add_body_p(doc, "B.4 Vista de Cooperación Proceso-Aplicación:", bold_prefix="")
add_body_p(doc, "La siguiente matriz resume la cobertura real de los sistemas frente a los procesos de negocio, evidenciando un estado crítico en la organización:")

# Tabla Cooperación
coop_data = [
    ["Recepción y pesaje de materia prima", "Software Balanza (PC aislada sin red) + Digitación manual en ERP", "✗ Deficiente", "Cálculo diferido; transcripción al día siguiente en papel."],
    ["Proceso y envasado de aceituna", "Access 2014 (Desarrollo artesanal) + Hojas de cálculo locales", "✗ Deficiente", "Sin soporte ni mantenimiento; riesgo severo de corrupción."],
    ["Control de calidad y trazabilidad", "Access 2014 + Hoja de cálculo de campaña en planta", "✗ Deficiente", "Reconstrucción manual de 11 días; incumplimiento SENASA."],
    ["Exportación y trámites aduaneros", "ERP Comercial (Ventas/Almacén) + Documentos aduana", "~ Parcial", "No valida lotes en tiempo real; acuerdos en correos."],
    ["Compras a productores asociados", "ERP Comercial (Compras) + Contratos papel + Excel campo", "~ Parcial", "32 productores agrícolas operan al margen del ERP."],
    ["Gestión de riego y campo", "Consola Web Proveedor (Nube cerrada) + Excel campo", "~ Parcial", "Telemetría aislada sin exportación ni integración con ERP."],
]
t_coop = doc.add_table(rows=1, cols=4)
t_coop.alignment = WD_TABLE_ALIGNMENT.CENTER
t_coop.autofit = False
col_widths_coop = [Inches(1.8), Inches(2.2), Inches(0.9), Inches(1.6)]
style_table_header(t_coop.rows[0], col_widths_coop)
t_coop.rows[0].cells[0].paragraphs[0].text = "Proceso de Negocio"
t_coop.rows[0].cells[1].paragraphs[0].text = "Sistema de Soporte Actual"
t_coop.rows[0].cells[2].paragraphs[0].text = "Nivel"
t_coop.rows[0].cells[3].paragraphs[0].text = "Diagnóstico"
style_table_header(t_coop.rows[0], col_widths_coop)

for r in coop_data:
    row = t_coop.add_row()
    for i, (cell, val) in enumerate(zip(row.cells, r)):
        cell.width = col_widths_coop[i]
        set_cell_margins(cell, top=70, bottom=70, left=100, right=100)
        p = cell.paragraphs[0]
        run = p.add_run(val)
        run.font.name = 'Calibri'
        run.font.size = Pt(8)
        if i == 0:
            run.font.bold = True
        elif i == 2:
            run.font.bold = True
            if "✗" in val:
                run.font.color.rgb = RGBColor(192, 57, 43)
            else:
                run.font.color.rgb = RGBColor(180, 130, 20)

add_body_p(doc, "Resultado cuantitativo: 3 de 6 procesos (50%) en nivel Deficiente y 3 de 6 procesos (50%) en nivel Parcial. 0% de procesos con soporte Bueno.", italic=True)

# Insertar imagen vista cooperación si existe
if os.path.exists("docs/evidencias/S10/graficos/vista_cooperacion.png"):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_picture("docs/evidencias/S10/graficos/vista_cooperacion.png", width=Inches(6.2))
    p_cap = doc.add_paragraph(style='Image Caption')
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.add_run("Figura 1. Vista de cooperación proceso-aplicación de la arquitectura actual (As-Is).")

add_body_p(doc, "B.5 Estructura de la Información (Catálogo de Entidades de Datos):", bold_prefix="")
add_body_p(doc, "Se construyó la matriz de información en '05_arquitectura/AR02_entidades.csv'. A continuación se presenta el diagnóstico consolidado:")

# Tabla Entidades
ent_table_data = [
    ["Lote", "Access, ERP Almacén, Balanza, Excel", "2 300 / 410 / 9 800 / 22", "Ninguna", "Ninguno", "Kilos por lote difieren hasta 6% entre sistemas.", "Interna", "No"],
    ["Productor", "ERP Proveedores, Excel campo, Papel", "71 / 210 / 180", "ERP (incompleta)", "Jefe Compras", "32 productores del campo no existen en ERP.", "Confidencial", "Sí"],
    ["Trabajador", "SaaS Planillas, ERP, Asistencia papel", "142 / 97 / 520 campaña", "SaaS Planillas", "Administración", "520 trabajadores de campaña sin registro.", "Restringida", "Sí (sensibles)"],
    ["Cliente ext.", "ERP Ventas, Correo, Documentos aduana", "14 / — / 22", "ERP Ventas", "Gerencia Gral.", "Condiciones comerciales residen en correos.", "Confidencial", "Sí (contacto)"],
    ["Pesaje", "Balanza PC, Hojas papel, ERP Compras", "9 800 / 9 800 / 9 150", "Ninguna", "Ninguno", "650 pesajes de balanza sin transcripción a ERP.", "Interna", "No"],
    ["Costo/Tn", "Excel Finanzas, ERP Contab., Planta", "1 libro / Cuentas / Notas", "Ninguna", "Ninguno", "Mermas en Excel no concilian con contabilidad.", "Confidencial", "No"],
    ["Riego", "Consola web fertirriego, Excel campo", "48 sectores / 1 libro", "Ninguna", "Ninguno", "Volumen de agua/fertilizante difiere del sistema web.", "Interna", "No"],
]

t_ent = doc.add_table(rows=1, cols=8)
t_ent.alignment = WD_TABLE_ALIGNMENT.CENTER
t_ent.autofit = False
col_widths_ent = [Inches(0.8), Inches(1.0), Inches(0.9), Inches(0.7), Inches(0.8), Inches(1.3), Inches(0.6), Inches(0.6)]
style_table_header(t_ent.rows[0], col_widths_ent)
for i, h in enumerate(["Entidad", "Sistemas", "Registros", "Fuente Aut.", "Dueño", "Discrepancia", "Clasif.", "Datos Pers."]):
    t_ent.rows[0].cells[i].paragraphs[0].text = h
style_table_header(t_ent.rows[0], col_widths_ent)

for r in ent_table_data:
    row = t_ent.add_row()
    for i, (cell, val) in enumerate(zip(row.cells, r)):
        cell.width = col_widths_ent[i]
        set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
        p = cell.paragraphs[0]
        run = p.add_run(val)
        run.font.name = 'Calibri'
        run.font.size = Pt(7.5)
        if i == 0:
            run.font.bold = True

add_body_p(doc, "Métricas clave de la capa de datos: 5 de 7 entidades (71.4%) carecen de fuente autoritativa única y 5 de 7 entidades (71.4%) no tienen un dueño asignado formalmente por cargo. Asimismo, el 100% de los datos personales de trabajadores de campaña se manejan de manera informal sin medidas de la Ley N° 29733.", italic=True)

# Insertar imagen 3 capas actual si existe
if os.path.exists("docs/evidencias/S10/graficos/vista_actual_3capas.png"):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_picture("docs/evidencias/S10/graficos/vista_actual_3capas.png", width=Inches(6.2))
    p_cap = doc.add_paragraph(style='Image Caption')
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.add_run("Figura 2. Modelo de la arquitectura actual (As-Is) en tres capas con hojas de cálculo operativas.")

# Paso C
add_styled_heading(doc, "Paso C — Modelar la arquitectura objetivo (To-Be)", level=2)
add_bullet_p(doc, "Diseñar la arquitectura futura (To-Be) derivándola estrictamente de la visión institucional, los objetivos de TI, las capacidades requeridas y las estrategias del FODA cruzado.", bold_prefix="Qué se buscaba: ")
add_bullet_p(doc, "Construcción de la matriz de cambios por capa y modelado del estado objetivo en ArchiMate 3.2, documentado en '05_seccion_arquitectura.md'.", bold_prefix="Comando o acción: ")
add_bullet_p(doc, "Derivación trazada y especificación de cambios estructurales:", bold_prefix="Evidencia de que funcionó: ")

add_body_p(doc, "• Derivación Estratégica: El objetivo declarado de 'reducir el cierre de trazabilidad de 11 días a menos de 2 horas' exige reemplazar el Access 2014 y las hojas de cálculo por un Módulo de Trazabilidad y Producción (MES) integrado nativamente al ERP. La exigencia de inocuidad SENASA y la Ley 29733 imponen la digitalización del padrón de productores y el registro de trabajadores.", bold_prefix="C.1 Derivación: ")

# Tabla cambios To-Be
cambios_to_be = [
    ["Negocio", "Toma de pesaje en papel y diferido", "Recepción y pesaje automatizado con sensores IoT y escáner", "Visión del PETI (Sección 2.2)"],
    ["Negocio", "Trazabilidad manual armada en 11 días", "Trazabilidad digital inmediata 'Field-to-Fork' (< 2 horas)", "Exigencia SENASA y clientes UE"],
    ["Datos", "Lote en 4 sistemas disjuntos (6% desvío)", "Maestro Único de Lotes en ERP como fuente autoritativa", "Principio 1 (Dato único con dueño)"],
    ["Datos", "32 productores asociados fuera del ERP", "Padrón unificado de productores integrado al módulo de compras", "Control fiscal y Principio 1"],
    ["Datos", "520 trabajadores de campaña sin registro", "Registro automatizado de personal y cumplimiento Ley 29733", "Sección 4.1 (Obligación ANPD)"],
    ["Aplicación", "Access 2014 sin soporte y Excel en planta", "Módulo Integrado de Trazabilidad y Producción (MES) en ERP", "Principio 6 e Incidente 2024"],
    ["Aplicación", "Balanza en PC aislada con transcripción", "Integración automática de balanza con ERP vía API REST", "Principio 3 (Cero digitación diferida)"],
    ["Aplicación", "Costeo por tonelada en Excel de Finanzas", "Módulo de costeo estándar automático en ERP contable", "Estrategia E-03 (Control de rentabilidad)"],
    ["Aplicación", "Consola de fertirriego sin integración", "Conector de telemetría de campo al ERP", "Principio 3 y Eficiencia hídrica"],
    ["Tecnología", "Servidor único con UPS de 10 minutos", "Infraestructura híbrida con RAID y réplica inmutable en nube", "Principio 4 y COBIT DSS04"],
    ["Tecnología", "PC de planta en ambiente corrosivo", "Terminales industriales rugerizados IP65 centralizados", "Mitigación del incidente 2024"],
    ["Tecnología", "Red plana y enlace monoproveedor", "VLANs segmentadas (Planta/Oficina/DMZ) y enlace redundante", "COBIT DSS05 (Seguridad perimetral)"],
]

t_tob = doc.add_table(rows=1, cols=4)
t_tob.alignment = WD_TABLE_ALIGNMENT.CENTER
t_tob.autofit = False
col_widths_tob = [Inches(1.0), Inches(2.2), Inches(2.2), Inches(1.3)]
style_table_header(t_tob.rows[0], col_widths_tob)
t_tob.rows[0].cells[0].paragraphs[0].text = "Capa"
t_tob.rows[0].cells[1].paragraphs[0].text = "Elemento Actual (As-Is)"
t_tob.rows[0].cells[2].paragraphs[0].text = "Elemento Objetivo (To-Be)"
t_tob.rows[0].cells[3].paragraphs[0].text = "Origen del Cambio"
style_table_header(t_tob.rows[0], col_widths_tob)

for r in cambios_to_be:
    row = t_tob.add_row()
    for i, (cell, val) in enumerate(zip(row.cells, r)):
        cell.width = col_widths_tob[i]
        set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
        p = cell.paragraphs[0]
        run = p.add_run(val)
        run.font.name = 'Calibri'
        run.font.size = Pt(8)
        if i == 0:
            run.font.bold = True

if os.path.exists("docs/evidencias/S10/graficos/vista_objetivo.png"):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_picture("docs/evidencias/S10/graficos/vista_objetivo.png", width=Inches(6.2))
    p_cap = doc.add_paragraph(style='Image Caption')
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.add_run("Figura 3. Modelo de la arquitectura objetivo (To-Be) en tres capas con integración de servicios y nube híbrida.")

# Paso D
add_styled_heading(doc, "Paso D — Análisis de brechas y paquetes de trabajo", level=2)
add_bullet_p(doc, "Identificar la totalidad de brechas entre el estado actual y el objetivo, clasificarlas por capa y tipo, calcular el esfuerzo técnico y derivar los paquetes de trabajo respetando su secuencia lógica obligada.", bold_prefix="Qué se buscaba: ")
add_bullet_p(doc, f"Ejecución automatizada del script en Python '05_arquitectura/AR03_brechas.py', generando el dataset '05_arquitectura/AR03_brechas.csv' y el registro en 'docs/evidencias/S10/salidas/salida_brechas.txt'. Enlace: {REPO_URL}/05_arquitectura/AR03_brechas.py", bold_prefix="Comando o acción: ")
add_bullet_p(doc, "Se detectaron 13 brechas arquitectónicas consolidadas en seis paquetes de trabajo prioritarios:", bold_prefix="Evidencia de que funcionó: ")

# Tabla de Paquetes de Trabajo
pt_resumen = [
    ["PT-01", "Gobierno y Calidad del Dato Maestro (MDM)", "Lote disperso en 4 sistemas; 32 productores fuera de ERP; 520 trabajadores sin registro.", "Alto", "Ninguna (Habilitador)", "Fase 1"],
    ["PT-02", "Sistema Integrado de Trazabilidad (MES)", "Access 2014 sin soporte; Excel de campaña en planta; PC de planta en riesgo físico.", "Alto", "PT-01, PT-04", "Fase 2"],
    ["PT-03", "Automatización de Pesaje y Telemetría Industrial", "Balanza aislada con transcripción manual; Consola de riego aislada.", "Medio", "PT-04 (Redes)", "Fase 2"],
    ["PT-04", "Infraestructura, Respaldo Inmutable y Continuidad", "Servidor único con UPS 10 min; Red plana y enlace monoproveedor.", "Alto", "Ninguna (Habilitador)", "Fase 1"],
    ["PT-05", "Integración Financiera, Costeo y Nómina", "Cálculo de costo/Tn en Excel de Finanzas; Integración por correo a planillas.", "Medio", "PT-01, PT-02", "Fase 3"],
    ["PT-06", "Gobierno de TI, Políticas y Protección de Datos", "Sin Comité de TI ni políticas formalizadas; Cuentas de admin compartidas.", "Bajo", "Ninguna (Habilitador)", "Fase 1"],
]

t_pt = doc.add_table(rows=1, cols=6)
t_pt.alignment = WD_TABLE_ALIGNMENT.CENTER
t_pt.autofit = False
col_widths_pt = [Inches(0.8), Inches(2.0), Inches(2.1), Inches(0.8), Inches(1.1), Inches(0.7)]
style_table_header(t_pt.rows[0], col_widths_pt)
for i, h in enumerate(["Paquete", "Nombre del Proyecto", "Brechas Relacionadas", "Esfuerzo", "Dependencias", "Fase"]):
    t_pt.rows[0].cells[i].paragraphs[0].text = h
style_table_header(t_pt.rows[0], col_widths_pt)

for r in pt_resumen:
    row = t_pt.add_row()
    for i, (cell, val) in enumerate(zip(row.cells, r)):
        cell.width = col_widths_pt[i]
        set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
        p = cell.paragraphs[0]
        run = p.add_run(val)
        run.font.name = 'Calibri'
        run.font.size = Pt(8)
        if i == 0:
            run.font.bold = True

add_body_p(doc, "Secuencia obligada determinada: La Fase 1 (PT-01, PT-04 y PT-06) constituye la base habilitadora obligatoria. La Fase 2 (PT-02 y PT-03) no puede iniciar sin datos maestros saneados ni redes industriales operativas. Finalmente, la Fase 3 (PT-05) optimiza los costos una vez que la trazabilidad en planta está estabilizada.", bold_prefix="Justificación de la Secuencia: ")

# Paso E
add_styled_heading(doc, "Paso E — Vistas y redacción de la Sección 5 del PETI", level=2)
add_bullet_p(doc, "Exportar las vistas formales en alta resolución y redactar formalmente la Sección 5 (Arquitectura Empresarial) del PETI para su incorporación en la versión v0.10 del plan institucional.", bold_prefix="Qué se buscaba: ")
add_bullet_p(doc, f"Redacción completa de 'docs/05_seccion_arquitectura.md' estructurada en cuatro subsecciones: 5.1 Principios, 5.2 Arquitectura actual, 5.3 Arquitectura objetivo y 5.4 Análisis de brechas. Enlace: {REPO_URL}/docs/05_seccion_arquitectura.md", bold_prefix="Comando o acción: ")
add_bullet_p(doc, "Sección 5 redactada íntegramente cumpliendo la numeración estándar y consolidando el diagnóstico, los modelos y la hoja de ruta preliminar.", bold_prefix="Evidencia de que funcionó: ")

# Paso F
add_styled_heading(doc, "Paso F — Validar y corregir", level=2)
add_bullet_p(doc, "Someter los artefactos producidos a las tres comprobaciones obligatorias de calidad antes de cerrar la sesión de laboratorio, registrando el resultado en 'docs/evidencias/S10/salidas/validaciones.txt'.", bold_prefix="Qué se buscaba: ")
add_bullet_p(doc, "Auditoría cruzada del modelo ArchiMate frente al inventario real y verificación de relaciones bidireccionales en las brechas.", bold_prefix="Comando o acción: ")
add_bullet_p(doc, "Las tres comprobaciones resultaron plenamente satisfactorias:", bold_prefix="Evidencia de que funcionó: ")
add_bullet_p(doc, "Comprobación 1 (Pertenencia de Capas en ArchiMate 3.2): Cumplida. Se verificó que los procesos y actores residan en Negocio, los sistemas y hojas de cálculo en Aplicación, y los nodos, redes y DBMS en Tecnología.", bold_prefix="1. ")
add_bullet_p(doc, "Comprobación 2 (Existencia Real de Aplicaciones): Cumplida. Se contrastó el modelo con el inventario oficial. No se incluyeron aplicaciones teóricas; las 8 aplicaciones modeladas existen y operan en La Yarada.", bold_prefix="2. ")
add_bullet_p(doc, "Comprobación 3 (Trazabilidad Bipolar de Brechas): Cumplida. Las 13 brechas tienen origen claro en el modelo As-Is y solución concreta en el modelo To-Be, sin elementos huérfanos.", bold_prefix="3. ")

# Paso G
add_styled_heading(doc, "Paso G — Registrar la evidencia y cerrar", level=2)
add_bullet_p(doc, "Versionar en Git todos los artefactos creados, generar las etiquetas requeridas y responder la pregunta de transferencia metodológica.", bold_prefix="Qué se buscaba: ")
add_bullet_p(doc, "Ejecución de los comandos oficiales de control de versiones y etiquetado:", bold_prefix="Comando o acción: ")
p_cmd = doc.add_paragraph(style='Source Code')
p_cmd.paragraph_format.left_indent = Inches(0.3)
p_cmd.add_run('git add .\n'
              'git commit -m "S10: arquitectura empresarial actual, objetivo y analisis de brechas — seccion 5"\n'
              'git tag -a v0.10 -m "PETI v0.10 — arquitectura empresarial"\n'
              'git tag -a taller-10 -m "Taller 10 · SI886"\n'
              'git push origin main --tags')

add_bullet_p(doc, "Versionamiento exitoso bajo los tags 'v0.10' y 'taller-10'. Asimismo, se respondió exhaustivamente a la pregunta de transferencia en la Sección 5 del cuestionario.", bold_prefix="Evidencia de que funcionó: ")

# ==========================================
# SECCIÓN 3: RESULTADOS
# ==========================================
add_styled_heading(doc, "3. Resultados", level=1)
add_body_p(doc, "A continuación se presenta la matriz de comprobación oficial del Taller 10, evaluada frente a los resultados esperados de la guía y respaldada por las evidencias verificables en el repositorio:")

# Tabla 3.2 de Resultados
resultados_checklist = [
    ["1", "Seis principios de arquitectura con los cinco campos y su trazabilidad al diagnóstico", "Logrado", f"{REPO_URL}/05_arquitectura/AR01_principios.md"],
    ["2", "Modelo en Archi con las tres capas de la arquitectura actual", "Logrado", f"{REPO_URL}/anexos/anexo_A_modelo_arquitectura.archimate"],
    ["3", "Las hojas de cálculo modeladas como componentes de aplicación", "Logrado", f"{REPO_URL}/docs/evidencias/S10/graficos/vista_actual_3capas.png"],
    ["4", "Vista de cooperación proceso-aplicación, con los procesos sin soporte identificados", "Logrado", f"{REPO_URL}/docs/evidencias/S10/graficos/vista_cooperacion.png"],
    ["5", "Estructura de la información con ≥ 6 entidades, sus sistemas y su número de registros", "Logrado", f"{REPO_URL}/05_arquitectura/AR02_entidades.csv"],
    ["6", "Entidades sin fuente autoritativa y sin dueño identificadas y contadas", "Logrado", f"5 de 7 entidades (71.4%) en {REPO_URL}/05_arquitectura/AR02_entidades.csv"],
    ["7", "Entidades que contienen datos personales marcadas, con su clasificación", "Logrado", f"3 entidades clasificadas en {REPO_URL}/05_arquitectura/AR02_entidades.csv"],
    ["8", "Arquitectura objetivo modelada, con cada cambio trazado a su origen", "Logrado", f"{REPO_URL}/docs/evidencias/S10/graficos/vista_objetivo.png"],
    ["9", "Análisis de brechas con ≥ 10 brechas, su tipo, esfuerzo y dependencias", "Logrado", f"13 brechas en {REPO_URL}/05_arquitectura/AR03_brechas.csv"],
    ["10", "Paquetes de trabajo derivados de las brechas", "Logrado", f"6 paquetes (PT-01 a PT-06) en {REPO_URL}/docs/evidencias/S10/salidas/salida_brechas.txt"],
    ["11", "Secuencia obligada por dependencias determinada", "Logrado", f"Secuencia en 3 fases en {REPO_URL}/docs/evidencias/S10/salidas/salida_brechas.txt"],
    ["12", "Tres vistas exportadas en PNG, sin detalle técnico sensible", "Logrado", f"{REPO_URL}/docs/evidencias/S10/graficos/"],
    ["13", "Sección 5 redactada · etiquetas v0.10 y taller-10", "Logrado", f"Tags v0.10 y taller-10 en {REPO_URL}"],
]

t_res = doc.add_table(rows=1, cols=4)
t_res.alignment = WD_TABLE_ALIGNMENT.CENTER
t_res.autofit = False
col_widths_res = [Inches(0.4), Inches(2.8), Inches(0.8), Inches(2.6)]
style_table_header(t_res.rows[0], col_widths_res)
t_res.rows[0].cells[0].paragraphs[0].text = "#"
t_res.rows[0].cells[1].paragraphs[0].text = "Resultado esperado"
t_res.rows[0].cells[2].paragraphs[0].text = "¿Se logró?"
t_res.rows[0].cells[3].paragraphs[0].text = "Evidencia verificable"
style_table_header(t_res.rows[0], col_widths_res)

for r in resultados_checklist:
    row = t_res.add_row()
    for i, (cell, val) in enumerate(zip(row.cells, r)):
        cell.width = col_widths_res[i]
        set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
        p = cell.paragraphs[0]
        run = p.add_run(val)
        run.font.name = 'Calibri'
        run.font.size = Pt(8)
        if i == 0 or i == 2:
            run.font.bold = True
            if i == 2:
                run.font.color.rgb = RGBColor(39, 174, 96)

add_body_p(doc, "Evaluación global de resultados: Los trece resultados exigidos por la lista de comprobación de la Semana 10 fueron alcanzados satisfactoriamente (100% de cumplimiento). Toda la evidencia cuantitativa, datasets, diagramas a 300 DPI y scripts de cálculo se encuentran debidamente versionados y accesibles en el repositorio oficial de GitHub bajo la etiqueta 'taller-10'.", bold_prefix="Evaluación Global: ")

# ==========================================
# SECCIÓN 4: CONCLUSIONES
# ==========================================
add_styled_heading(doc, "4. Conclusiones", level=1)

conclusiones = [
    ("1. La capa de datos revela la verdadera deuda técnica y el riesgo operacional de la empresa:",
     " El diagnóstico demostró que la dispersión del dato maestro de 'Lote' en cuatro sistemas y la falta de dueño formal (5 de 7 entidades sin dueño) explican por qué la empresa tardó 11 días en atender un reclamo de calidad en 2024. Los problemas de trazabilidad no eran atribuibles al software de balanza, sino a la inexistencia de una fuente autoritativa de verdad. Preguntar quién responde por el lote reveló que múltiples áreas lo alimentan y ninguna responde por su consistencia."),
    
    ("2. La arquitectura objetivo no se diseña por moda tecnológica, sino por estricta derivación estratégica:",
     " Cada componente propuesto en el modelo To-Be (el Módulo MES, las APIs de integración y la nube híbrida) responde a una métrica concreta del plan: reducir el tiempo de trazabilidad de 11 días a menos de 2 horas para cumplir las auditorías de SENASA y la Unión Europea. La trazabilidad bipolar entre el estado actual y el objetivo es lo que permite defender técnicamente el presupuesto de TI ante la Alta Dirección."),
    
    ("3. Las dependencias entre paquetes de trabajo imponen una secuencia obligada que la hoja de ruta debe respetar:",
     " La ejecución del análisis de brechas demostró que proyectos como la analítica avanzada de costos o el portal de trazabilidad no pueden implementarse sobre datos inconsistentes o infraestructura inestable. El Gobierno del Dato Maestro (PT-01) y la Infraestructura con Respaldo Inmutable (PT-04) constituyen prerrequisitos habilitadores ineludibles. Ignorar esta secuencia provocaría la parálisis de los sistemas y el rechazo de los usuarios."),
]
for c_title, c_desc in conclusiones:
    p_c = doc.add_paragraph()
    p_c.paragraph_format.space_after = Pt(6)
    p_c.paragraph_format.line_spacing = 1.15
    r_t = p_c.add_run(c_title)
    r_t.font.name = 'Calibri'
    r_t.font.size = Pt(10)
    r_t.font.bold = True
    r_t.font.color.rgb = RGBColor(22, 40, 92)
    r_d = p_c.add_run(c_desc)
    r_d.font.name = 'Calibri'
    r_d.font.size = Pt(10)
    r_d.font.color.rgb = RGBColor(51, 65, 85)

# ==========================================
# SECCIÓN 5: CUESTIONARIO
# ==========================================
add_styled_heading(doc, "5. Cuestionario", level=1)

cuestionario = [
    ("Pregunta 1 (Pregunta de transferencia de la guía · Paso G): ¿Qué riesgo correría una organización real si este modelado de arquitectura empresarial se hiciera mal o se omitiera?",
     "Respuesta: Correría el riesgo inminente de parálisis operativa, pérdidas económicas millonarias por rechazo de exportaciones y sanciones regulatorias severas. En una agroexportadora como Valle Viejo, omitir la arquitectura empresarial implicaría seguir confiando el núcleo de la trazabilidad a un aplicativo artesanal en Access y libros de Excel manipulables. Si SENASA o la FDA auditan un embarque y la empresa tarda 11 días en reconstruir el lote (en lugar de 2 horas), los contenedores son retenidos en puerto perdiéndose perecibles de alto valor y cancelándose certificaciones internacionales. Asimismo, comprar un nuevo software sin sanear las entidades de datos duplicaría los costos de implantación sin resolver el desvío de kilos entre sistemas."),
    
    ("Pregunta 2: ¿Por qué es obligatorio modelar las hojas de cálculo operativas dentro de la capa de aplicaciones de ArchiMate y qué impacto tiene omitirlas?",
     "Respuesta: Porque en organizaciones medianas, las hojas de cálculo operan en la práctica como sistemas de información críticos (Shadow IT). Si se omitieran del modelo para reflejar solo los sistemas formalmente adquiridos, se construiría una arquitectura ficticia. Omitir el libro de Excel de trazabilidad o el de costos de Finanzas impediría detectar las brechas de integración reales, llevando a formular proyectos de TI que no resuelven el trabajo manual subyacente y perpetúan la duplicidad de digitación."),
    
    ("Pregunta 3: ¿Por qué se afirma en el marco TOGAF que la capa de datos es la que mayor valor aporta al PETI y la que menos suele estar documentada?",
     "Respuesta: Porque los datos representan los activos informacionales perdurables del negocio, independientes de la tecnología de turno. La tecnología cambia de servidor a nube y las aplicaciones se reemplazan, pero el histórico de lotes, clientes y compras permanece. Documentar la capa de datos revela las inconsistencias estructurales que ninguna herramienta automática detecta: duplicidades de registros, ausencia de fuentes autoritativas y vacío de responsabilidades legales."),
    
    ("Pregunta 4: ¿Cómo justifica la regla de dependencias que el paquete de trabajo PT-01 (Gobierno del Dato) deba preceder a PT-02 (Trazabilidad MES) y PT-05 (Costeo Estándar)?",
     "Respuesta: Porque un sistema transaccional o de costeo solo es tan confiable como los datos maestros que consume. Si se implementa un software de trazabilidad industrial o de costeo automático antes de definir la estructura única del lote y sanear el padrón de productores agrícolas, el nuevo sistema procesará registros inconsistentes, arrojando mermas ficticias y liquidaciones erróneas. El principio 'basura entra, basura sale' impone que el gobierno del dato sea siempre el primer hito habilitador."),
]

for q_text, a_text in cuestionario:
    p_q = doc.add_paragraph()
    p_q.paragraph_format.space_before = Pt(8)
    p_q.paragraph_format.space_after = Pt(2)
    r_q = p_q.add_run(q_text)
    r_q.font.name = 'Calibri'
    r_q.font.size = Pt(10)
    r_q.font.bold = True
    r_q.font.color.rgb = RGBColor(31, 78, 121)
    
    p_a = doc.add_paragraph()
    p_a.paragraph_format.space_after = Pt(6)
    p_a.paragraph_format.line_spacing = 1.15
    r_a = p_a.add_run(a_text)
    r_a.font.name = 'Calibri'
    r_a.font.size = Pt(9.5)
    r_a.font.color.rgb = RGBColor(51, 65, 85)

# ==========================================
# SECCIÓN 6: REFERENCIAS BIBLIOGRÁFICAS
# ==========================================
add_styled_heading(doc, "6. Referencias bibliográficas", level=1)

referencias = [
    "Archi. (2024). Archi — Open Source ArchiMate Modelling (Versión 5.4). https://www.archimatetool.com/",
    "Congreso de la República del Perú. (2011). Ley N° 29733: Ley de Protección de Datos Personales y su Reglamento aprobado por D. S. N° 003-2013-JUS.",
    "ISACA. (2018). COBIT 2019 Framework: Governance and Management Objectives (Objetivos APO03 Managed Enterprise Architecture y DSS04 Managed Continuity). Information Systems Audit and Control Association.",
    "ISO/IEC/IEEE. (2011). Systems and software engineering — Architecture description (ISO/IEC/IEEE Standard 42010:2011). IEEE.",
    "Lankhorst, M. (2017). Enterprise Architecture at Work: Modelling, Communication and Analysis (4.ª ed.). Springer.",
    "MINTIC Colombia. (2020). Marco de Referencia de Arquitectura Empresarial para la gestión de TI en el Estado. Ministerio de Tecnologías de la Información y las Comunicaciones.",
    "Presidencia del Consejo de Ministros. (2021). Decreto Supremo N° 029-2021-PCM: Reglamento del Decreto de Urgencia N° 006-2020 que crea el Sistema Nacional de Transformación Digital.",
    "Rodríguez Bermúdez, J. R. (2015). Planificación y dirección estratégica de sistemas de información. Editorial UOC.",
    "Ross, J. W., Weill, P. y Robertson, D. C. (2006). Enterprise Architecture as Strategy: Creating a Foundation for Business Execution. Harvard Business School Press.",
    "SENASA. (2023). Manual de Procedimientos para la Certificación Fitosanitaria de Exportación de Productos Agrícolas. Servicio Nacional de Sanidad Agraria del Perú.",
    "The Open Group. (2022). The TOGAF® Standard, 10th Edition. The Open Group. https://www.opengroup.org/togaf",
    "The Open Group. (2022). ArchiMate® 3.2 Specification. The Open Group. https://pubs.opengroup.org/architecture/archimate3-doc/",
]

for ref in referencias:
    p_ref = doc.add_paragraph(style='Bibliography')
    p_ref.paragraph_format.space_after = Pt(4)
    p_ref.paragraph_format.line_spacing = 1.15
    p_ref.paragraph_format.left_indent = Inches(0.4)
    p_ref.paragraph_format.first_line_indent = Inches(-0.4)
    r = p_ref.add_run(ref)
    r.font.name = 'Calibri'
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(51, 65, 85)

# ==========================================
# SECCIÓN 7: ANEXOS
# ==========================================
add_styled_heading(doc, "7. Anexos", level=1)

anexos_desc = [
    ("Anexo A: Modelo de Arquitectura Empresarial en ArchiMate",
     "anexos/anexo_A_modelo_arquitectura.archimate",
     f"{REPO_URL}/anexos/anexo_A_modelo_arquitectura.archimate",
     "Archivo oficial en formato XML nativo de Archi con la especificación completa de elementos de Negocio, Aplicación, Tecnología y Motivación."),
    
    ("Anexo B: Vista de Cooperación Proceso-Aplicación (Alta Resolución)",
     "anexos/anexo_B_vista_proceso_aplicacion.png",
     f"{REPO_URL}/anexos/anexo_B_vista_proceso_aplicacion.png",
     "Gráfico renderizado a 300 DPI que ilustra la matriz de soporte actual e identifica los tres procesos en estado deficiente."),
    
    ("Anexo C: Matriz de Estructura de la Información y Gobierno del Dato",
     "anexos/anexo_C_estructura_informacion.xlsx",
     f"{REPO_URL}/anexos/anexo_C_estructura_informacion.xlsx",
     "Libro de cálculo en Excel con el inventario de entidades de datos, sistemas de residencia, discrepancias observadas, conteos y asignación de dueños por cargo."),
    
    ("Anexo D: Vista de Arquitectura Objetivo To-Be (Alta Resolución)",
     "anexos/anexo_D_arquitectura_objetivo.png",
     f"{REPO_URL}/anexos/anexo_D_arquitectura_objetivo.png",
     "Diagrama en alta resolución que muestra la modernización de las tres capas con el módulo MES, APIs de integración y nube híbrida."),
    
    ("Anexo E: Matriz de Análisis de Brechas y Paquetes de Trabajo",
     "anexos/anexo_E_analisis_brechas.xlsx",
     f"{REPO_URL}/anexos/anexo_E_analisis_brechas.xlsx",
     "Libro de cálculo estructurado con las 13 brechas categorizadas y la formulación de los 6 paquetes de trabajo con su secuencia obligada."),
    
    ("Anexo F: Sección 5 del PETI (Arquitectura Empresarial)",
     "docs/05_seccion_arquitectura.md",
     f"{REPO_URL}/docs/05_seccion_arquitectura.md",
     "Documento normativo final redactado formalmente e incorporado al Plan Estratégico de TI bajo la versión v0.10."),
]

for title, fpath, url, desc in anexos_desc:
    p_an = doc.add_paragraph()
    p_an.paragraph_format.space_before = Pt(6)
    p_an.paragraph_format.space_after = Pt(2)
    r_t = p_an.add_run(f"• {title}")
    r_t.font.name = 'Calibri'
    r_t.font.size = Pt(9.5)
    r_t.font.bold = True
    r_t.font.color.rgb = RGBColor(31, 78, 121)
    
    p_det = doc.add_paragraph()
    p_det.paragraph_format.left_indent = Inches(0.25)
    p_det.paragraph_format.space_after = Pt(4)
    r_f = p_det.add_run(f"Archivo: {fpath} | Enlace oficial: {url}\n")
    r_f.font.name = 'Calibri'
    r_f.font.size = Pt(8.5)
    r_f.font.italic = True
    r_f.font.color.rgb = RGBColor(100, 116, 139)
    r_d = p_det.add_run(f"Descripción: {desc}")
    r_d.font.name = 'Calibri'
    r_d.font.size = Pt(9)
    r_d.font.color.rgb = RGBColor(51, 65, 85)

# Guardar documento Word final
output_docx = "SI886-S10-TALLER-GianFrancoArocutipa.docx"
doc.save(output_docx)
print(f"Documento Word guardado exitosamente como: {output_docx}")
