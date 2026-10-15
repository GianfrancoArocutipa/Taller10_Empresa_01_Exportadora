# AR01 · Principios de Arquitectura Empresarial
## Organización: Agroexportadora Valle Viejo S.A.C.
**Documento:** `05_arquitectura/AR01_principios.md`  
**Estándar:** TOGAF Standard 10th Edition (Architecture Principles)  
**Trazabilidad:** Sección 3.1 (Diagnóstico interno), Sección 3.3 (Incidentes y Riesgos) y Sección 4.1 (Cumplimiento normativo) del PETI

---

### Principio 1: Dato único con dueño (Master Data Management para Lotes y Productores)
* **Declaración:** Cada entidad fundamental del negocio (en particular *Lote de Producción*, *Productor Asociado* y *Pesaje*) posee una única fuente autoritativa de verdad registrada en el sistema central y un dueño de dato designado formalmente por cargo directivo.
* **Razón:** En el diagnóstico se detectó que el dato de *Lote* reside disperso en cuatro repositorios no sincronizados (Access, ERP Almacén, Balanza y Excel), arrojando discrepancias de hasta un 6% en peso acumulado. Asimismo, existen 32 productores registrados en cuadernos de campo que no figuran en el ERP. Esta divergencia causó que un reclamo de calidad en 2024 demorara 11 días en reconstruirse.
* **Implicancias:** Queda estrictamente prohibida la creación de bases de datos o libros de Excel paralelos para registrar lotes o productores. Todo sistema o módulo debe consultar o alimentar el repositorio maestro. La Gerencia de Producción asume la propiedad del dato *Lote* y la Jefatura de Compras la del dato *Productor Asociado*.
* **Trazabilidad:** Hallazgo de Sección 3.1.3 (Silos de información e inconsistencia de existencias) e Incidente 2024 (Pérdida de trazabilidad por corrupción de archivo local).

---

### Principio 2: Trazabilidad integral automatizada «Del Campo al Embarque» (Field-to-Fork)
* **Declaración:** El ciclo de vida de la materia prima, procesamiento, control analítico y despacho aduanero debe registrarse de manera continua y en tiempo real, garantizando la trazabilidad bidireccional inmediata sin intervención de digitación manual intermedia.
* **Razón:** Los mercados internacionales de destino (España, Estados Unidos, Brasil y Chile) y los entes reguladores (SENASA, FDA) exigen auditorías de trazabilidad de lote en menos de 2 horas. La reconstrucción manual en Excel expone a la empresa al rechazo de contenedores en puerto y pérdida de certificaciones internacionales.
* **Implicancias:** El pesaje de balanza y las variables de procesamiento industrial deben capturarse mediante interfaces de red directas hacia el sistema de trazabilidad. Se establece como métrica obligatoria del PETI reducir el tiempo de cierre de trazabilidad de 11 días a menos de 2 horas.
* **Trazabilidad:** Objetivo declarado de la organización (Ficha Institucional, Sección A) y requerimiento de inocuidad SENASA/Codex Alimentarius.

---

### Principio 3: Integración mediante servicios e interfaces estandarizadas (No más digitación diferida)
* **Declaración:** Toda comunicación e intercambio de información entre aplicaciones, maquinaria industrial (balanza, sensores) y plataformas externas se realiza mediante interfaces programáticas estandarizadas (APIs, web services o colas de mensajes), prohibiendo la digitación manual diferida y las transferencias por archivos planos no validados.
* **Razón:** La balanza electrónica funciona en una PC aislada y los pesajes se transcriben a mano al ERP al día siguiente. El personal copia manualmente registros del ERP a un archivo Access y envía libros de Excel por correo a la empresa de planillas, introduciendo errores humanos, retrasos operativos y pérdida de trazabilidad.
* **Implicancias:** Todo nuevo componente de software o equipo adquirido debe contar con capacidad de conexión TCP/IP e interfaces abiertas de integración. Ninguna aplicación entrará en producción si requiere digitación manual secundaria de datos ya existentes en otro sistema.
* **Trazabilidad:** Sección 3.1.2 (Evaluación de sistemas e integraciones punto a punto) y Política de Cero Digitación Duplicada.

---

### Principio 4: Continuidad operativa, respaldo inmutable y recuperación verificada
* **Declaración:** Toda la infraestructura tecnológica y los activos de datos críticos de la empresa deben contar con esquemas de alta disponibilidad, redundancia eléctrica y respaldos periódicos automatizados con almacenamiento inmutable fuera de la sede y pruebas periódicas de restauración.
* **Razón:** La organización opera con un único servidor ERP en oficina con un UPS de solo 10 minutos de autonomía y una PC de planta en ambiente corrosivo/industrial que sufrió la pérdida total de la base de datos Access de la campaña 2024 sin respaldo, requiriendo 3 semanas de rescate manual.
* **Implicancias:** Se deben migrar los servicios críticos a un entorno híbrido/nube o servidor con arreglo RAID redundante y UPS con respaldo de grupo electrógeno. Se programarán copias inmutables diarias (estrategia 3-2-1) y pruebas trimestrales obligatorias de restauración con RTO ≤ 4 horas y RPO ≤ 1 hora.
* **Trazabilidad:** Sección 3.3 (Incidente de la campaña 2024), Riesgo H.2 (Sin respaldo verificado) y marco COBIT 2019 DSS04 (Gestión de la Continuidad).

---

### Principio 5: Seguridad, privacidad y cumplimiento legal desde el diseño (Privacy and Security by Design)
* **Declaración:** Los controles de ciberseguridad, gestión de identidades individuales y salvaguardas de protección de datos personales deben ser componentes intrínsecos de la arquitectura desde su concepción, garantizando el cumplimiento de la Ley N° 29733.
* **Razón:** Actualmente conviven cuentas de administrador compartidas entre el personal de TI, no existe segundo factor de autenticación (2FA), y los datos de más de 520 trabajadores eventuales de campaña y 210 productores asociados se manejan en hojas sueltas y cuadernos sin medidas de seguridad técnica ni registro de tratamiento ante la ANPD.
* **Implicancias:** Se prohíbe el uso de credenciales genéricas o compartidas. Todo acceso debe autenticarse de forma nominal y registrar trazabilidad de auditoría (logs). Se debe implementar un Registro de Actividades de Tratamiento de Datos Personales y cifrado en reposo para bases de datos con información sensible.
* **Trazabilidad:** Sección B y F de la Ficha (Situación de TI), Sección 4.1 (Cumplimiento de la Ley 29733 y Directiva de Seguridad de la Información).

---

### Principio 6: Soluciones estándar mantenibles antes que desarrollos propios frágiles (Buy before Build)
* **Declaración:** Se priorizará la adopción de módulos nativos del ERP comercial o soluciones de software especializadas con soporte técnico vigente de fabricante, restringiendo los desarrollos a medida únicamente a los procesos que confieran una ventaja competitiva diferencial única.
* **Razón:** El núcleo de la trazabilidad industrial de la empresa descansa sobre un aplicativo artesanal desarrollado en Microsoft Access en el año 2014 por un extrabajador, el cual carece de soporte, documentación y mantenimiento desde hace más de diez años, generando una vulnerabilidad crítica de continuidad del negocio.
* **Implicancias:** Se sustituirá el aplicativo Access y las tres hojas de cálculo críticas por módulos consolidados dentro del ERP o un WMS/MES con soporte corporativo y acuerdos de nivel de servicio (SLA). Toda excepción requerirá autorización expresa del Comité de TI.
* **Trazabilidad:** Sección C (Sistemas de información), Riesgo H.1 (Dependencia de una sola persona) y práctica TOGAF de racionalización de aplicaciones.
