<div align="center">
  <strong>CLÍNICA SAN RAMÓN S.A.C.</strong><br>
  <em>Documento del caso</em>
</div>

---

# Inventario de la arquitectura actual

| | |
|---|---|
| **Organización** | CLÍNICA SAN RAMÓN S.A.C. |
| **Documento** | Inventario de la arquitectura actual |
| **Entregado por** | Tecnologías de la Información, a pedido del equipo |
| **Fecha de entrega** | 25 de abril de 2026 |
| **Clasificación** | Restringido |

> Documento de una organización ficticia, elaborado para el curso. Cualquier parecido con una empresa real es coincidencia.

---

## 1. Qué es este documento

Es lo que el área de tecnologías de la información entrega cuando se le pide **cómo están armados sus sistemas**. No existía. Se armó a pedido del equipo con lo que el área sabe, y el propio jefe advierte que «faltan cosas que solo están en la cabeza de alguien».

## 2. Aplicaciones que operan

Los sistemas de la ficha, más **las hojas de cálculo que operan como sistema**. El área reconoce que sin ellas la organización no funciona.

| Aplicación | Qué es | Dónde corre | ¿Tiene soporte vigente? |
|---|---|---|---|
| **HIS — historia clínica electrónica** | Producto peruano, módulos de admisión, consulta, hospitalización y farmacia | Servidor propio en sala de máquinas | Sí, soporte por horas |
| **Facturación y convenios con aseguradoras** | Módulo del mismo HIS | Mismo servidor | Sí |
| **Laboratorio (LIS)** | Software del proveedor de equipos, integrado por archivos planos | PC de laboratorio | Parcial |
| **Imágenes (PACS)** | Servidor de imágenes del proveedor de tomógrafo | Servidor dedicado | Sí |
| **Planillas y asistencia** | Sistema local con marcador biométrico | PC de RR. HH. | No |
| **Hoja de cálculo · Programación de salas y camas** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |
| **Hoja de cálculo · Conciliación con aseguradoras** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |
| **Hoja de cálculo · Honorarios médicos** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |

## 3. Qué sistema soporta cada proceso

| Proceso de negocio | Sistema que lo soporta |
|---|---|
| Admisión y filiación del paciente | HIS — historia clínica electrónica |
| Atención ambulatoria y hospitalización | HIS — historia clínica electrónica |
| Laboratorio e imágenes | Laboratorio (LIS) |
| Farmacia y dispensación | HIS — historia clínica electrónica |
| Facturación a aseguradoras | Facturación y convenios con aseguradoras |
| Gestión de historias clínicas | HIS — historia clínica electrónica |

## 4. Integraciones entre sistemas

| De | A | Cómo se integra hoy |
|---|---|---|
| Laboratorio (LIS) | HIS | Archivo plano copiado a mano dos veces al día |
| Imágenes (PACS) | HIS | Enlace por número de historia, sin validación |
| HIS | Facturación | Módulo del mismo producto, en línea |
| Planillas y asistencia | Nadie | Ninguna. El marcador biométrico exporta a un libro de cálculo |

## 5. Entidades de datos y dónde viven

Lo que el área pudo reconstruir. Los conteos son los que cada sistema devuelve hoy; cuando no coinciden, el área no sabe cuál es el bueno.

| Entidad | Sistemas donde reside | Registros por sistema | ¿Fuente autoritativa declarada? | Dueño del dato, por cargo | Discrepancia que el área conoce | Clasificación | ¿Datos personales? |
|---|---|---|---|---|---|---|---|
| Paciente | HIS admisión · HIS facturación · LIS · PACS · Portal de citas | 48 000 · 48 000 · 31 000 · 12 000 · 9 600 | HIS, declarada | Ninguno. Admisión lo crea y nadie lo corrige | 1 100 pacientes con dos historias | Restringida | Sí, sensibles |
| Resultado de laboratorio | LIS · HIS · Papel | 46 800 al año · 46 800 · 46 800 | LIS | Jefe de laboratorio | 34 resultados asignados al paciente equivocado | Restringida | Sí, sensibles |
| Médico | HIS · Planillas · Libro de honorarios | 92 · 214 en planilla · 46 | Ninguna | Ninguno | Médicos por honorarios con cuentas compartidas en consultorio | Confidencial | Sí |
| Cita | Portal de citas · Agenda del HIS · Cuaderno de recepción | 9 600 · 31 000 · — | HIS | Jefe de admisión | Las citas del portal se vuelven a registrar a mano | Interna | Sí, de contacto |

## 6. Nodos, dispositivos y redes

**Nodos.** Servidor del HIS y de facturación en una sala de máquinas propia con aire acondicionado doméstico · servidor dedicado del PACS · PC de laboratorio con el LIS · PC de RR. HH. con planillas · 120 estaciones y 30 puntos de consultorio.

**Redes.** Una sola red para consultorios, administración y equipos biomédicos. Internet de un proveedor, con el portal de citas en hosting contratado.

## 7. Lo que la organización responde

| Pregunta del equipo | Respuesta |
|---|---|
| ¿Existe un diagrama de arquitectura? | «Hay uno de red en una pizarra. Nunca se dibujaron los sistemas» |
| ¿Quién aprueba que un área cree una hoja de cálculo para operar? | «Nadie. Aparecen y después hay que alimentarlas» |
| ¿Quién es el dueño de cada dato? | «El sistema que lo tiene. Si está en dos, los dos» |
| ¿Qué pasa cuando dos sistemas dicen cifras distintas? | «Se pregunta al que lo lleva y se usa esa» |
| ¿Hay principios de arquitectura escritos? | «No» |

## 8. Marco de referencia

| Marco | Qué aporta |
|---|---|
| **TOGAF, 10.ª edición · ADM** | Fases B, C y D para la arquitectura de negocio, de sistemas de información y de tecnología, y el análisis de brechas |
| **ArchiMate 3.2** | El lenguaje con el que se modelan las capas y sus relaciones |
| **COBIT 2019 · APO03** | Gestión de la arquitectura empresarial |

