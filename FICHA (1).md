<div align="center">
  <img src="../../../Logos/logo_universidad.png" alt="Universidad Privada de Tacna" height="62">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="../../../Logos/logo_escuela_sistemas.jpeg" alt="Escuela Profesional de Ingeniería de Sistemas" height="62">
</div>

<p align="center">
  <strong>Universidad Privada de Tacna</strong><br>
  Facultad de Ingeniería · Escuela Profesional de Ingeniería de Sistemas
</p>

<h1 align="center">CLÍNICA SAN RAMÓN S.A.C.</h1>

<p align="center">
  Banco de casos · <strong>Empresa 02</strong> · Salud privada · clínica de mediana complejidad<br>
  <em>Organización ficticia. Cualquier parecido con una empresa real es coincidencia.</em>
</p>

---

## A. Ficha de la organización

| Campo | Contenido |
|---|---|
| **Razón social** | CLÍNICA SAN RAMÓN S.A.C. |
| **Sector** | Salud privada · clínica de mediana complejidad |
| **Domicilio fiscal** | Cercado de Tacna |
| **RUC** | 20601XXXXX *(enmascarado; es una organización ficticia)* |
| **Años de operación** | 23 |
| **Personal en planilla** | 214 |
| **Personal adicional** | 46 médicos por honorarios |
| **Facturación / presupuesto anual** | S/ 38.9 millones |
| **Mercado o población atendida** | Tacna y pacientes de Arica, Chile |
| **Naturaleza** | Empresa privada. |
| **Entidades que la regulan o supervisan** | SUSALUD · DIRESA Tacna · SUNAT · ANPD (datos de salud) · DIGEMID |

**Objetivo declarado para TI en el periodo.** Eliminar la carga manual entre sistemas clínicos y cumplir la protección reforzada de datos de salud.

## B. Estructura y gobierno

| | |
|---|---|
| **Personal de TI** | 4 personas |
| **Responsable de TI** | Coordinador de TI, técnico titulado, 3 años en el puesto, reporta a Gerencia General |
| **Comité de TI o de gobierno digital** | No existe. |
| **Política de seguridad de la información** | Existe desde 2022, sin difusión ni revisión posterior. |
| **Presupuesto de TI del periodo** | S/ 686 000 · 1.76 % de la facturación |

> **Sin marco de gobierno digital obligatorio.** Al ser privada, las exigencias provienen de su regulador sectorial, de la Ley 29733 de protección de datos personales y de sus compromisos contractuales.

## C. Sistemas de información

| Sistema | Descripción | Dónde corre | Desde | ¿Tiene soporte vigente? |
|---|---|---|---|---|
| **HIS — historia clínica electrónica** | Producto peruano, módulos de admisión, consulta, hospitalización y farmacia | Servidor propio en sala de máquinas | 2018 | Sí, soporte por horas |
| **Facturación y convenios con aseguradoras** | Módulo del mismo HIS | Mismo servidor | 2018 | Sí |
| **Laboratorio (LIS)** | Software del proveedor de equipos, integrado por archivos planos | PC de laboratorio | 2020 | Parcial |
| **Imágenes (PACS)** | Servidor de imágenes del proveedor de tomógrafo | Servidor dedicado | 2022 | Sí |
| **Planillas y asistencia** | Sistema local con marcador biométrico | PC de RR. HH. | 2017 | No |

**El problema que la organización reconoce.** La integración entre laboratorio y HIS es por archivo plano copiado a mano dos veces al día. En 2025 se detectaron 34 resultados adjuntados al paciente equivocado.

## D. Procesos de negocio

| N.º | Proceso | ¿Qué sistema lo soporta? |
|---|---|---|
| 1 | Admisión y filiación del paciente | HIS — historia clínica electrónica |
| 2 | Atención ambulatoria y hospitalización | HIS — historia clínica electrónica |
| 3 | Laboratorio e imágenes | Laboratorio (LIS) |
| 4 | Farmacia y dispensación | HIS — historia clínica electrónica |
| 5 | Facturación a aseguradoras | Facturación y convenios con aseguradoras |
| 6 | Gestión de historias clínicas | HIS — historia clínica electrónica |

## E. Instrumentos de planeamiento existentes

| Instrumento | ¿Existe? | Vigencia | Estado real |
|---|---|---|---|
| Plan estratégico o plan de negocio | Sí | 2023–2027 | Aprobado por resolución, se cumple parcialmente. |
| Plan operativo anual | Sí | 2025 | Se formula cada año para efectos presupuestales. |
| Plan Estratégico de Tecnologías de la Información (PETI) | **No** | — | **Nunca se ha formulado.** |
| Plan de transformación digital | No | — | No se ha formulado. |
| Política de seguridad de la información | Parcial | — | Existe desde 2022, sin difusión ni revisión posterior. |
| Plan de continuidad del negocio | No | — | No existe. El BIA de `datos/bia.csv` es un borrador incompleto elaborado por un practicante. |
| Catálogo de servicios de TI | No | — | Sin responsable asignado. |

## F. Situación de TI — hechos verificables para el diagnóstico

Son los hechos que la organización admite y que pueden darse por ciertos. Todo lo demás se pregunta en la entrevista.

| Aspecto | Situación verificada |
|---|---|
| **Capacitación en seguridad** | Nunca se ha hecho. |
| **Gestión de cambios** | Hay un formato de cambio que se llena después de aplicar el cambio. |
| **Contraseñas** | Las cuentas de administrador se comparten entre dos personas de TI. |
| **Registro de incidentes** | Existe un cuaderno físico en TI. |
| **Respaldos** | Existen respaldos programados, pero tres de los sistemas quedaron fuera del alcance sin que nadie lo advirtiera. |
| **Contratos con proveedores de TI** | Los contratos existen pero ninguno define niveles de servicio medibles. |
| **Segundo factor de autenticación** | Solo en el correo corporativo. |
| **Inventario de activos de TI** | Existe una hoja de cálculo actualizada por última vez hace dos años. |

## G. El incidente del periodo

**Resultados de laboratorio asignados a pacientes equivocados**

El proceso manual de carga del LIS al HIS asignó 34 resultados a historias clínicas incorrectas durante seis semanas. Se detectó por reclamo de un paciente. No existe registro de quién ejecutó cada carga.

## H. Riesgos que la organización ya conoce y no ha tratado

| N.º | Riesgo conocido | ¿Tratado? |
|---|---|---|
| 1 | Datos sensibles de salud sin cifrado en reposo | No |
| 2 | Integración manual entre sistemas clínicos | No |
| 3 | Cuentas de médicos compartidas en consultorios | No |

## I. Datos entregados

Los siete archivos de `datos/` corresponden al periodo del 1 de enero al 31 de diciembre de 2025. Fueron generados con la semilla de esta empresa. **No coinciden con los de ningún otro equipo**.

| Archivo | Qué contiene | Registros |
|---|---|---|
| `pagos.csv` | Población de pagos del periodo — comprobante, fecha, proveedor, concepto, monto, quién registró y quién aprobó | 10 129 |
| `proveedores.csv` | Maestro de proveedores con su contacto y documento de identidad | 107 |
| `empleados.csv` | Planilla del periodo, con fechas de ingreso y cese | 214 |
| `usuarios_erp.csv` | Usuarios del ERP con su perfil, último acceso y estado | 140 |
| `bia.csv` | Análisis de impacto al negocio por proceso, con RTO, RPO y fecha de la última prueba | 6 |
| `presupuesto_ti.csv` | Presupuesto de TI del periodo por partida, planificado contra ejecutado | 7 |
| `inversiones_cerradas.csv` | Tres inversiones cerradas con su beneficio declarado y si se midió | 3 |

---

**Docente** · Dr. Oscar Juan Jimenez Flores
[oscarjimenezflores@upt.pe](mailto:oscarjimenezflores@upt.pe) · [LinkedIn](https://www.linkedin.com/in/oscar-jimenez-flores/) · [CTI Vitae — CONCYTEC](https://ctivitae.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=33398)

Escuela Profesional de Ingeniería de Sistemas · Universidad Privada de Tacna · Tacna, Perú
