<div align="center">
  <img src="../../../Logos/logo_universidad.png" alt="Universidad Privada de Tacna" height="62">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="../../../Logos/logo_escuela_sistemas.jpeg" alt="Escuela Profesional de Ingeniería de Sistemas" height="62">
</div>

<p align="center">
  <strong>Universidad Privada de Tacna</strong><br>
  Facultad de Ingeniería · Escuela Profesional de Ingeniería de Sistemas
</p>

<h1 align="center">AGROEXPORTADORA VALLE VIEJO S.A.C.</h1>

<p align="center">
  Banco de casos · <strong>Empresa 01</strong> · Agroexportación · aceituna y aceite de oliva<br>
  <em>Organización ficticia. Cualquier parecido con una empresa real es coincidencia.</em>
</p>

---

## A. Ficha de la organización

| Campo | Contenido |
|---|---|
| **Razón social** | AGROEXPORTADORA VALLE VIEJO S.A.C. |
| **Sector** | Agroexportación · aceituna y aceite de oliva |
| **Domicilio fiscal** | La Yarada-Los Palos, Tacna |
| **RUC** | 20454XXXXX *(enmascarado; es una organización ficticia)* |
| **Años de operación** | 18 |
| **Personal en planilla** | 142 |
| **Personal adicional** | 380 en campaña (may–ago) |
| **Facturación / presupuesto anual** | S/ 47.3 millones |
| **Mercado o población atendida** | España, Brasil, Chile y Estados Unidos |
| **Naturaleza** | Empresa privada. |
| **Entidades que la regulan o supervisan** | SENASA · SUNAT-Aduanas · ANA (licencia de agua) · MINAGRI · SUNAFIL |

**Objetivo declarado para TI en el periodo.** Sostener la trazabilidad exigida por el mercado de destino y reducir el cierre de campaña de 11 a 2 días.

## B. Estructura y gobierno

| | |
|---|---|
| **Personal de TI** | 3 personas |
| **Responsable de TI** | Jefe de Sistemas, ingeniero de sistemas, 6 años en el puesto, reporta a Administración y Finanzas |
| **Comité de TI o de gobierno digital** | No existe. |
| **Política de seguridad de la información** | En borrador desde hace dos años; nunca se aprobó. |
| **Presupuesto de TI del periodo** | S/ 412 000 · 0.87 % de la facturación |

> **Sin marco de gobierno digital obligatorio.** Al ser privada, las exigencias provienen de su regulador sectorial, de la Ley 29733 de protección de datos personales y de sus compromisos contractuales.

## C. Sistemas de información

| Sistema | Descripción | Dónde corre | Desde | ¿Tiene soporte vigente? |
|---|---|---|---|---|
| **ERP** | Sistema comercial peruano, módulos de compras, ventas, almacén y contabilidad | On-premise, servidor único | 2016 | Sí, contrato anual |
| **Trazabilidad de lotes** | Desarrollo a medida en Access, mantenido por un exempleado | PC de planta | 2014 | No |
| **Planillas** | Servicio tercerizado, se envían Excel por correo | SaaS del proveedor | 2019 | Sí |
| **Balanza y control de ingreso de materia prima** | Software del fabricante de la balanza | PC de balanza, sin red | 2012 | No |
| **Riego tecnificado** | Consola del proveedor de fertirriego, acceso web | Nube del proveedor | 2021 | Sí |

**El problema que la organización reconoce.** La trazabilidad de lote exigida por el comprador europeo se arma a mano en Excel cada embarque. Un reclamo de calidad en 2024 tomó 11 días de reconstrucción documental.

## D. Procesos de negocio

| N.º | Proceso | ¿Qué sistema lo soporta? |
|---|---|---|
| 1 | Recepción y pesaje de materia prima | Balanza y control de ingreso de materia prima |
| 2 | Proceso y envasado | Trazabilidad de lotes |
| 3 | Control de calidad y trazabilidad de lote | Trazabilidad de lotes |
| 4 | Exportación y documentación aduanera | ERP |
| 5 | Compras a productores asociados | ERP |
| 6 | Gestión de riego y campo | Riego tecnificado |

## E. Instrumentos de planeamiento existentes

| Instrumento | ¿Existe? | Vigencia | Estado real |
|---|---|---|---|
| Plan estratégico o plan de negocio | Sí | 2023–2027 | Aprobado, pero no se ha revisado desde su aprobación. |
| Plan operativo anual | Sí | 2025 | Se formula cada año para efectos presupuestales. |
| Plan Estratégico de Tecnologías de la Información (PETI) | **No** | — | **Nunca se ha formulado.** |
| Plan de transformación digital | No | — | No se ha formulado. |
| Política de seguridad de la información | Parcial | — | En borrador desde hace dos años; nunca se aprobó. |
| Plan de continuidad del negocio | No | — | No existe. El BIA de `datos/bia.csv` es un borrador incompleto elaborado por un practicante. |
| Catálogo de servicios de TI | No | — | Sin responsable asignado. |

## F. Situación de TI — hechos verificables para el diagnóstico

Son los hechos que la organización admite y que pueden darse por ciertos. Todo lo demás se pregunta en la entrevista.

| Aspecto | Situación verificada |
|---|---|
| **Contratos con proveedores de TI** | Dos de los cinco contratos están vencidos y el servicio continúa. |
| **Inventario de activos de TI** | Existe una hoja de cálculo actualizada por última vez hace dos años. |
| **Registro de incidentes** | Se lleva por correo electrónico, sin clasificación ni tiempos. |
| **Gestión de cambios** | Hay un formato de cambio que se llena después de aplicar el cambio. |
| **Contraseñas** | Las cuentas de administrador se comparten entre dos personas de TI. |
| **Respaldos** | Se ejecutan a disco local y nunca se ha probado una restauración completa. |
| **Segundo factor de autenticación** | No está habilitado en ningún sistema. |
| **Capacitación en seguridad** | Nunca se ha hecho. |

## G. El incidente del periodo

**Pérdida del archivo de trazabilidad de la campaña 2024**

El archivo maestro de trazabilidad se corrompió en el PC de planta. No había respaldo. Se reconstruyó parcialmente desde correos y guías físicas durante tres semanas, en plena campaña de exportación.

## H. Riesgos que la organización ya conoce y no ha tratado

| N.º | Riesgo conocido | ¿Tratado? |
|---|---|---|
| 1 | Dependencia de una sola persona para el sistema de trazabilidad | No |
| 2 | Sin respaldo verificado de los sistemas de planta | No |
| 3 | Acceso compartido al ERP entre almacén y compras | No |

## I. Datos entregados

Los siete archivos de `datos/` corresponden al periodo del 1 de enero al 31 de diciembre de 2025. Fueron generados con la semilla de esta empresa. **No coinciden con los de ningún otro equipo**.

| Archivo | Qué contiene | Registros |
|---|---|---|
| `pagos.csv` | Población de pagos del periodo — comprobante, fecha, proveedor, concepto, monto, quién registró y quién aprobó | 12 314 |
| `proveedores.csv` | Maestro de proveedores con su contacto y documento de identidad | 71 |
| `empleados.csv` | Planilla del periodo, con fechas de ingreso y cese | 142 |
| `usuarios_erp.csv` | Usuarios del ERP con su perfil, último acceso y estado | 97 |
| `bia.csv` | Análisis de impacto al negocio por proceso, con RTO, RPO y fecha de la última prueba | 6 |
| `presupuesto_ti.csv` | Presupuesto de TI del periodo por partida, planificado contra ejecutado | 7 |
| `inversiones_cerradas.csv` | Tres inversiones cerradas con su beneficio declarado y si se midió | 3 |

---

**Docente** · Dr. Oscar Juan Jimenez Flores
[oscarjimenezflores@upt.pe](mailto:oscarjimenezflores@upt.pe) · [LinkedIn](https://www.linkedin.com/in/oscar-jimenez-flores/) · [CTI Vitae — CONCYTEC](https://ctivitae.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=33398)

Escuela Profesional de Ingeniería de Sistemas · Universidad Privada de Tacna · Tacna, Perú
