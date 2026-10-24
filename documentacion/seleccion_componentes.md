# Selección de componentes y dispositivos externos

## SEL-001 — Cámara de referencia eléctrica

- Fecha de decisión: 2026-10-24.
- Fabricante: XIMEA.
- Referencia: **MQ022HG-IM-SM5X5-7NIR2**.
- Ubicación: carga útil externa a la PCB central y de comunicaciones.
- Estado: seleccionada como referencia eléctrica académica. No se ha validado la observación de lotes desde 550 km ni se ha seleccionado la óptica.
- Trazabilidad: RF-01; IF-07 e IF-08; interfaz de alimentación IF-02 por definir; ET-04 y ET-08 afectados por el volumen de datos y la interfaz.

### Fundamento

La comparación documentada en `comparacion_camaras_2026-10-24.md` favorece esta referencia para estudiar adquisición, almacenamiento y transmisión: producto activo, documentación de interfaz disponible y cuerpo compacto. SILIOS CMS-V conserva interés, pero falta información de consumo; MultiScape50 excede los presupuestos heredados y su integración en el 1U no está demostrada; XIMEA RN2 aparece descontinuada. No se ha realizado una comparación de precios porque no se dispone de cotizaciones.

La selección permite dimensionar la interfaz USB3 y el manejo de cuadros brutos. No acredita resolución espacial de la misión, aptitud orbital, integración mecánica completa ni consumo máximo. La óptica permanece pendiente y es necesaria para cerrar la carga útil.

### Condiciones del análisis

Se utiliza un cuadro RAW16 completo por adquisición, diez adquisiciones por día y 600 s diarios de contacto como escenario preliminar. Los 10 bits del sensor se almacenan en contenedores de 16 bits; el presupuesto no multiplica el cuadro bruto por el número de bandas. Las cabeceras y el relleno del archivo todavía deben verificarse. Telemetría y eficiencia del enlace permanecen sin valor; no se asumen iguales a cero o uno.

Los cálculos se encuentran en `calculos/calculos_y_restricciones.xlsx`. La potencia publicada sirve para una equivalencia nominal, no para seleccionar protección o corriente máxima del conector. Deben obtenerse los consumos de arranque y por modo.

### Documentación y efectos sobre el proyecto

Fuentes SRC-001 a SRC-003 en `referencias.csv`. El manual xiSpec2 se conserva en `hojas_de_datos/XIMEA_xiSpec2_manual_v2_03.pdf`. La portada indica 2.03, septiembre de 2026, mientras sus pies de página muestran V2.00.

El computador deberá admitir un anfitrión USB3 y software de adquisición compatible. Se verificará la plataforma concreta antes de seleccionarla. La cámara no forma parte de la BOM de componentes montados en nuestra PCB; su alimentación y conexión sí afectan el diseño. Los conectores y circuitos que se incorporen a la PCB tendrán sus propias referencias y designadores.

### Pendientes de cierre

1. Seleccionar el computador y comprobar compatibilidad de SDK, controlador USB y memoria.
2. Definir alimentación USB, tolerancia, corriente máxima, arranque y secuencia de encendido.
3. Comprobar formato, relleno, metadatos, tiempo por captura y transferencia efectiva.
4. Elegir óptica y comprobar campo de visión, muestreo, montaje y condiciones térmicas.
5. Dimensionar telemetría, enlace y retención de datos.

## Método para las siguientes selecciones

Agregar una entrada SEL-XXX por decisión relevante, con referencia exacta, función, alternativas, justificación, requisitos, fuentes y asuntos pendientes. Actualizar el libro, el registro de referencias y los acuerdos afectados. La BOM de Altium y las evidencias ERC se generarán cuando exista el diseño correspondiente; no se sustituyen por listas preliminares.
