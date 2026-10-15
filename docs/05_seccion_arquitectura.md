# 5. Arquitectura Empresarial
## Organización: Agroexportadora Valle Viejo S.A.C.
**Documento oficial del PETI · Versión v0.10**  
**Autores / Equipo de Trabajo:**  
* Colque Quispe, Rodrigo Sídney (Código: 2023077078)  
* Perez Peralta, Fabrizio Salvador Elias (Código: 2023077476)  
* Arocutipa Arocutipa, Gianfranco (Código: 2023076790)  
**Marco Metodológico:** TOGAF Standard 10th Edition (Fases B, C, D, E y F) · ArchiMate 3.2

---

### 5.1 Principios de Arquitectura
La arquitectura empresarial de Agroexportadora Valle Viejo S.A.C. se fundamenta en seis principios de gobernanza tecnológica, formulados bajo el estándar TOGAF:

1. **Principio 1 · Dato único con dueño (Master Data Management):** Cada entidad crítica de negocio (*Lote*, *Productor Asociado*, *Pesaje*) posee una única fuente autoritativa en el sistema central y un dueño formal designado por cargo directivo (Gerencia de Producción y Jefatura de Compras).
2. **Principio 2 · Trazabilidad integral automatizada «Del Campo al Embarque»:** El flujo de información desde la recepción de la materia prima, pesaje, procesamiento y envasado hasta el despacho aduanero se registra en tiempo real y sin transcripción manual diferida, permitiendo responder a auditorías internacionales de SENASA y clientes del exterior en menos de 2 horas.
3. **Principio 3 · Integración por servicios e interfaces estandarizadas:** Todo intercambio de información entre aplicaciones, maquinaria industrial (balanza electrónica, sensores) y plataformas externas se realiza mediante APIs y servicios web programáticos, prohibiendo la doble digitación de datos.
4. **Principio 4 · Continuidad operativa, respaldo inmutable y recuperación verificada:** Toda infraestructura tecnológica crítica dispone de alta disponibilidad, alimentación eléctrica ininterrumpida y esquemas automatizados de respaldo inmutable en la nube (RPO ≤ 1 hora, RTO ≤ 4 horas) bajo el marco COBIT DSS04.
5. **Principio 5 · Seguridad, privacidad y cumplimiento legal desde el diseño (Ley N° 29733):** Toda solución tecnológica incorpora autenticación individualizada (cero credenciales compartidas), control de accesos por roles (RBAC) y un Registro formal de Actividades de Tratamiento de Datos Personales para los más de 520 trabajadores y 210 productores agrícolas.
6. **Principio 6 · Soluciones estándar mantenibles antes que desarrollos propios frágiles (Buy before Build):** Se prioriza la adopción de módulos nativos del ERP comercial o software de industria con soporte técnico vigente, erradicando aplicativos artesanales no mantenidos como el Access 2014 y las hojas de cálculo operativas.

---

### 5.2 Arquitectura Actual (*As-Is*)

#### 5.2.1 Capa de Negocio
* **Actores de negocio:** Productores asociados (210 agricultores de La Yarada), Operario de balanza, Jefe de planta y producción, Responsable de calidad y trazabilidad, Gerencia de Administración y Finanzas, SENASA y Clientes internacionales (España, EE.UU., Brasil, Chile).
* **Procesos de negocio (Cadena de Valor):**
  1. *Recepción y pesaje de materia prima:* Acopio y pesaje de aceituna en camiones.
  2. *Proceso y envasado:* Lavado, macerado, selección, prensado y embotellado de aceite.
  3. *Control de calidad y trazabilidad de lote:* Muestreo de acidez, peróxido y armado manual de trazabilidad.
  4. *Exportación y documentación aduanera:* Facturación de exportación y packing list.
  5. *Compras a productores asociados:* Liquidación de compras y pagos.
  6. *Gestión de riego y campo:* Programación de riego y fertilización en parcelas.

#### 5.2.2 Capa de Datos
* **Diagnóstico de Entidades de Datos:**
  * **Entidades evaluadas:** 7 entidades principales (*Lote*, *Productor asociado*, *Trabajador*, *Cliente internacional*, *Pesaje de materia prima*, *Costo por tonelada*, *Programación de riego*).
  * **Entidades sin fuente autoritativa:** **5 de 7 entidades (71.4%)** no cuentan con una fuente autoritativa declarada ni única.
  * **Entidades sin dueño asignado:** **5 de 7 entidades (71.4%)** carecen de un cargo directivo que responda por su integridad.
  * **Discrepancia crítica:** El dato *Lote* arroja discrepancias de hasta el 6% en kilos acumulados entre el Access de planta, el ERP y las hojas de cálculo. Asimismo, 32 productores registrados en cuadernos de campo no existen en la base de datos del ERP.
  * **Protección de datos personales:** El 100% de los datos personales de trabajadores eventuales de campaña (520 trabajadores) se gestiona al margen de los sistemas formales, violando la Ley N° 29733.

#### 5.2.3 Capa de Aplicación
* **Sistemas formales en operación:**
  * *ERP Comercial (2016):* Servidor local con soporte anual; cubre compras, ventas, almacén y contabilidad.
  * *Trazabilidad de lotes (2014):* Base de datos en **Microsoft Access**, sin soporte ni mantenimiento desde hace 10 años.
  * *Software de Balanza (2012):* Aplicativo propietario en PC aislada sin red.
  * *Consola de Fertirriego (2021):* Plataforma web SaaS en nube cerrada sin capacidades de exportación.
  * *Sistema de Planillas (2019):* SaaS externo alimentado por libros de Excel remitidos por correo quincenalmente.
* **Hojas de cálculo que operan como sistemas (Shadow IT crítico):**
  1. *Hoja de cálculo · Trazabilidad por lote:* Un libro Excel por campaña operado en planta.
  2. *Hoja de cálculo · Costo por tonelada:* Libro en Finanzas donde se calculan mermas y costos indirectos de forma paralela al ERP.
  3. *Hoja de cálculo · Programación de riego:* Libro en campo no sincronizado con la nube de fertirriego.

#### 5.2.4 Capa de Tecnología
* **Nodos e Infraestructura:**
  * Un único servidor de ERP on-premise en la oficina central, con respaldo eléctrico por UPS doméstico limitado a 10 minutos de autonomía (sin grupo electrógeno conectado a TI).
  * PC de planta en ambiente corrosivo e industrial albergando la base de datos Access sin arreglo RAID ni copias de seguridad automáticas.
  * PC de caseta de balanza desprovista de tarjeta de red ni conectividad a la red corporativa.
* **Redes y Comunicaciones:**
  * Red LAN plana sin segmentación por VLANs donde conviven tráfico administrativo y puestos de producción.
  * Enlace inalámbrico punto a punto monoproveedor entre oficinas y planta agroindustrial, vulnerable a interferencias climáticas.

#### 5.2.5 Vista de Cooperación Proceso-Aplicación
* **Procesos con soporte deficiente:** **3 de 6 procesos (50%)** presentan soporte deficiente (*Recepción y pesaje*, *Proceso y envasado*, *Control de calidad y trazabilidad*).
* **Procesos con soporte parcial:** **3 de 6 procesos (50%)** presentan soporte parcial (*Exportación*, *Compras*, *Riego*).
* **Procesos con soporte bueno:** **0 de 6 procesos (0%)**. La operación crítica de la empresa descansa en un aplicativo obsoleto en Access y libros de cálculo no gobernados.

---

### 5.3 Arquitectura Objetivo (*To-Be*)

#### 5.3.1 Derivación Estratégica
La arquitectura objetivo se deriva rigurosamente de los objetivos institucionales y capacidades requeridas:
* **De la Visión y Métrica Central:** «Reducir el cierre de trazabilidad de campaña de 11 días a menos de 2 horas» exige sustituir el Access y los Excel por un **Módulo Integrado de Trazabilidad y Producción (MES)** conectado en tiempo real al ERP.
* **De la Política de Integración:** La eliminación de la transcripción manual diferida exige conectar la balanza electrónica vía **servicios TCP/IP / REST** hacia el ERP.
* **De la Continuidad del Negocio (COBIT DSS04):** Mitigar el riesgo del incidente 2024 exige implementar un **cluster de servidores híbrido con copias inmutables en la nube**.

#### 5.3.2 Cambios por Capa y Origen del Cambio

| Capa | Elemento Actual (*As-Is*) | Elemento Objetivo (*To-Be*) | Origen del Cambio |
|---|---|---|---|
| **Negocio** | Recepción con pesaje diferido en papel | Recepción con pesaje automatizado e identificación RFID/QR | Métrica de trazabilidad (Visión) |
| **Negocio** | Trazabilidad manual reconstruida en 11 días | Trazabilidad inmediata digital en menos de 2 horas | Exigencia SENASA y clientes Unión Europea |
| **Datos** | Lote disperso en 4 sistemas con 6% de desvío | Maestro de Lotes único en ERP como fuente autoritativa | Principio 1 (Dato único con dueño) |
| **Datos** | 32 productores agrícolas fuera del ERP | Padrón unificado de productores integrado al módulo de compras | Principio 1 y Control fiscal SUNAT |
| **Datos** | 520 trabajadores eventuales sin registro formal | Registro automatizado de personal y cumplimiento Ley 29733 | Sección 4.1 (Obligación legal ANPD) |
| **Aplicación** | Access 2014 sin soporte y Excel por campaña | Módulo de Trazabilidad y Producción (MES) integrado al ERP | Principio 6 e Incidente de campaña 2024 |
| **Aplicación** | Balanza en PC aislada con digitación manual | Servicio de integración directa de balanza con ERP (API REST) | Principio 3 (Cero digitación diferida) |
| **Aplicación** | Costeo por tonelada en libro Excel de Finanzas | Módulo de costeo estándar automático en ERP contable | Estrategia E-03 (Control de rentabilidad) |
| **Aplicación** | Consola de riego aislada sin exportación | Conector de telemetría de campo al ERP | Principio 3 y Eficiencia hídrica |
| **Tecnología** | Servidor único con UPS de 10 min | Cluster híbrido con RAID y réplica inmutable en la nube | Principio 4 y COBIT DSS04 |
| **Tecnología** | PC de planta en ambiente corrosivo | Terminales industriales táctiles rugerizados IP65 | Mitigación del incidente de planta 2024 |
| **Tecnología** | Red LAN plana y enlace monoproveedor | Segmentación VLAN (Planta, Oficina, DMZ) y enlace redundante | COBIT DSS05 (Seguridad perimetral) |

---

### 5.4 Análisis de Brechas y Paquetes de Trabajo

#### 5.4.1 Resumen Estadístico de Brechas
* **Brechas identificadas:** 13 brechas totales distribuidas en las 4 capas de arquitectura empresarial (3 en Datos, 6 en Aplicación, 3 en Tecnología y 1 en Negocio).
* **Distribución por esfuerzo:** 3 brechas de esfuerzo Alto, 6 de esfuerzo Medio y 4 de esfuerzo Bajo.

#### 5.4.2 Paquetes de Trabajo Derivados (Insumo de Sección 7)
Las brechas se consolidaron en seis paquetes de trabajo prioritarios:
1. **PT-01 Gobierno y Calidad del Dato Maestro (MDM):** Saneamiento y consolidación de los maestros de Lotes, Productores y Trabajadores.
2. **PT-02 Sistema Integrado de Trazabilidad y Producción (MES):** Reemplazo definitivo de Microsoft Access y las hojas de cálculo por software industrial.
3. **PT-03 Automatización de Pesaje y Telemetría Industrial:** Conexión programática de la balanza de materia prima y sensores de fertirriego.
4. **PT-04 Infraestructura, Respaldo Inmutable y Continuidad:** Adquisición de hardware tolerante a fallos, UPS corporativo y respaldo cloud inmutable.
5. **PT-05 Integración Financiera, Costeo y Nómina:** Integración de costos de producción en ERP y servicios web de planillas.
6. **PT-06 Gobierno de TI, Políticas y Protección de Datos:** Creación formal del Comité de TI y Registro de Protección de Datos Personales.

#### 5.4.3 Secuencia Obligada por Dependencias
* **Fase 1 · Habilitadores Críticos:** PT-01 (Gobierno del dato), PT-04 (Infraestructura y respaldo) y PT-06 (Gobierno de TI). *Sin datos saneados ni infraestructura estable, cualquier sistema nuevo fracasa.*
* **Fase 2 · Soluciones Core y Automatización:** PT-02 (Trazabilidad y producción MES) y PT-03 (Pesaje y telemetría). *Dependen estrictamente de la capa de datos de PT-01 y la conectividad de PT-04.*
* **Fase 3 · Optimización y Consolidación Financiera:** PT-05 (Costeo estándar y nómina). *Requiere la información operativa en línea generada en las Fases 1 y 2.*
