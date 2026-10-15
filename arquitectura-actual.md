<div align="center">
  <strong>AGROEXPORTADORA VALLE VIEJO S.A.C.</strong><br>
  <em>Documento del caso</em>
</div>

---

# Inventario de la arquitectura actual

| | |
|---|---|
| **Organización** | AGROEXPORTADORA VALLE VIEJO S.A.C. |
| **Documento** | Inventario de la arquitectura actual |
| **Entregado por** | Tecnologías de la Información, a pedido del equipo |
| **Fecha de entrega** | 14 de julio de 2026 |
| **Clasificación** | Restringido |

> Documento de una organización ficticia, elaborado para el curso. Cualquier parecido con una empresa real es coincidencia.

---

## 1. Qué es este documento

Es lo que el área de tecnologías de la información entrega cuando se le pide **cómo están armados sus sistemas**. No existía. Se armó a pedido del equipo con lo que el área sabe, y el propio jefe advierte que «faltan cosas que solo están en la cabeza de alguien».

## 2. Aplicaciones que operan

Los sistemas de la ficha, más **las hojas de cálculo que operan como sistema**. El área reconoce que sin ellas la organización no funciona.

| Aplicación | Qué es | Dónde corre | ¿Tiene soporte vigente? |
|---|---|---|---|
| **ERP** | Sistema comercial peruano, módulos de compras, ventas, almacén y contabilidad | On-premise, servidor único | Sí, contrato anual |
| **Trazabilidad de lotes** | Desarrollo a medida en Access, mantenido por un exempleado | PC de planta | No |
| **Planillas** | Servicio tercerizado, se envían Excel por correo | SaaS del proveedor | Sí |
| **Balanza y control de ingreso de materia prima** | Software del fabricante de la balanza | PC de balanza, sin red | No |
| **Riego tecnificado** | Consola del proveedor de fertirriego, acceso web | Nube del proveedor | Sí |
| **Hoja de cálculo · Trazabilidad por lote, un libro por campaña** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |
| **Hoja de cálculo · Costo por tonelada, libro de Finanzas** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |
| **Hoja de cálculo · Programación de riego, libro de campo** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |

## 3. Qué sistema soporta cada proceso

| Proceso de negocio | Sistema que lo soporta |
|---|---|
| Recepción y pesaje de materia prima | Balanza y control de ingreso de materia prima |
| Proceso y envasado | Trazabilidad de lotes |
| Control de calidad y trazabilidad de lote | Trazabilidad de lotes |
| Exportación y documentación aduanera | ERP |
| Compras a productores asociados | ERP |
| Gestión de riego y campo | Riego tecnificado |

## 4. Integraciones entre sistemas

| De | A | Cómo se integra hoy |
|---|---|---|
| Balanza | ERP | Manual. El pesaje se digita en el ERP al día siguiente |
| ERP | Trazabilidad de lotes | Manual. Los lotes se copian a mano al Access |
| ERP | Planillas | Un libro de cálculo por correo, cada quincena |
| Riego tecnificado | Nadie | Ninguna. La consola del proveedor no exporta |

## 5. Entidades de datos y dónde viven

Lo que el área pudo reconstruir. Los conteos son los que cada sistema devuelve hoy; cuando no coinciden, el área no sabe cuál es el bueno.

| Entidad | Sistemas donde reside | Registros por sistema | ¿Fuente autoritativa declarada? | Dueño del dato, por cargo | Discrepancia que el área conoce | Clasificación | ¿Datos personales? |
|---|---|---|---|---|---|---|---|
| Lote | Trazabilidad de lotes · ERP almacén · Balanza · Libro de exportación | 2 300 · 410 ítems · 9 800 pesadas · 22 embarques | Ninguna | Ninguno | Los kilos por lote difieren hasta 6 % entre sistemas | Interna | No |
| Productor asociado | ERP proveedores · Libro de campo · Contratos en papel | 71 · 210 · 180 | ERP, declarada | Jefe de compras | 32 productores del libro de campo no están en el ERP | Confidencial | Sí |
| Trabajador | Planillas · Usuarios del ERP · Asistencia en papel | 142 · 97 · 520 en campaña | Planillas | Administración | Los eventuales de campaña no entran a ningún sistema | Restringida | Sí, sensibles |
| Cliente internacional | ERP ventas · Casilla de correo compartida · Documentos aduaneros | 14 · — · — | ERP | Gerencia General | Las condiciones comerciales viven en el correo | Confidencial | Sí, de contacto |

## 6. Nodos, dispositivos y redes

**Nodos.** Un servidor único del ERP en la oficina, sin autonomía de energía más allá de diez minutos · la PC de planta con el Access · la PC de balanza sin red · 38 estaciones · la nube del proveedor de riego y el SaaS de planillas.

**Redes.** Red plana de oficina. La planta se conecta por un enlace inalámbrico propio. Un solo proveedor de internet.

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

