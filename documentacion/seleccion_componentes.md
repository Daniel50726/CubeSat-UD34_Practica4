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

1. Comprobar compatibilidad de SDK, controlador USB y memoria en el computador adoptado en SEL-002.
2. Definir alimentación USB, tolerancia, corriente máxima, arranque y secuencia de encendido.
3. Comprobar formato, relleno, metadatos, tiempo por captura y transferencia efectiva.
4. Elegir óptica y comprobar campo de visión, muestreo, montaje y condiciones térmicas.
5. Dimensionar telemetría, enlace y retención de datos.

## SEL-002 — Computador de a bordo

- Fecha de aprobación: 2026-10-25.
- Fabricante: Toradex.
- Referencia de diseño: Verdin iMX8M Plus Quad 4GB IT V1.1B, 00631101.
- Estado: selección de diseño académico aprobada. Compatibilidad de xiAPI en esta plataforma asumida como hipótesis de integración; no validada experimentalmente.
- Arquitectura: RAM y eMMC de arranque dentro del SoM; almacenamiento de misión independiente.
- Interfaz de cámara: puerto USB_2 como anfitrión USB 3.1 Gen 1; USB_1 reservado para recuperación.
- Alimentación: rama exclusiva de 5 V ±5 % en pines VCC y capacidad de 3 A, dimensionada a partir de la envolvente de pico de 12,5 W de la familia. No equivale a consumo permanente ni al requerimiento total de la PCB.
- Trazabilidad: IF-07/08/09; ET-02/03/04/07/08; revisión de los presupuestos heredados.

La evaluación, las fuentes primarias y sus archivos locales se encuentran en `evaluacion_computador_verdin.md`. Los cálculos se reproducen con `calculos/verificar_computador.py` y están integrados en el libro XLSX, Calculos!A62:D72. La referencia se adopta para captura esquemática; no se ha confirmado inventario, precio ni aptitud orbital. Los circuitos auxiliares, conectores, disipación y pinout completo se seleccionarán en las siguientes etapas. El almacenamiento externo se adopta en SEL-003.

## SEL-003 — Almacenamiento independiente de misión

- Fecha de aprobación: 2026-10-25.
- Referencia: Kingston SDCIT2/16GBSP, microSD industrial de 16 GB nominales sin adaptador SD.
- Ubicación: zócalo de la PCB central y de comunicaciones, separado del SoM y su eMMC de arranque.
- Interfaz: SD_1/USDHC2, cuatro bits, modo inicial Default Speed de 25 MHz y señalización de 3,3 V.
- Capacidad: exigir al menos 15 GB útiles después del formato. El escenario aprobado de 90 días requiere 12,2016064 GB incluyendo 1 GB inicial y 3 GB libres de reserva.
- Cuotas: diez cuadros RAW16/día, resultados hasta otro volumen RAW y 2 MB/día conjuntos de metadatos, telemetría, índices y eventos. Son supuestos aprobados que deben cumplirse o recalcularse.
- Justificación y sensibilidad: `propuesta_almacenamiento.md`; fórmulas en el libro XLSX y cálculo independiente en `calculos/verificar_almacenamiento.py`.
- Fuentes: SRC-009, SRC-012 y SRC-013; trazabilidad ET-04, IF-09 y PCB-06/07/08.
- Límites: corriente máxima y arranque no publicados en la ficha consultada; no se han elegido protección, zócalo ni interruptor. Capacidad útil, tiempos de escritura y retención mecánica requieren verificación. No se acredita redundancia ni aptitud orbital.

## SEL-004 — Adaptación UART de actitud

- Aprobada: 2026-10-25. Texas Instruments TXU0202DCUR, DCU de 8 contactos.
- Función: dos canales opuestos entre el dominio de 1,8 V del SoM y el de 3,3 V externo. Trazabilidad: IF-14/15; cambio C-11.
- Alternativa: SN74AXC2T245 con dirección configurable; se prefiere la dirección fija y los terminales accesibles del DCU para esta UART.
- Soporte: dos condensadores de 100 nF; tres pull-ups de 10 kohm y un pull-down de OE de 10 kohm, 1 %. Referencias comerciales de pasivos pendientes.
- Condición externa aprobada: pines UART tolerantes hasta 3,6 V sin alimentación, alta impedancia y fuga máxima de 10 uA por pin. Es requisito del módulo idealizado, no validación de un dispositivo real.
- Pendientes: GPIO OE y estado de reinicio, fuente/secuencia 1,8 V, umbrales/fugas garantizados del Verdin, ESD, carga dinámica, pinout y huella verificados en Altium. La selección no equivale a circuito liberado.
- Cálculos: Entradas!A90:F97 y Calculos!A79:D86. Cotas por resistencia, no consumo permanente total. Fuentes SRC-014/015.

## Método para las siguientes selecciones

Agregar una entrada SEL-XXX por decisión relevante, con referencia exacta, función, alternativas, justificación, requisitos, fuentes y asuntos pendientes. Actualizar el libro, el registro de referencias y los acuerdos afectados. La BOM de Altium y las evidencias ERC se generarán cuando exista el diseño correspondiente; no se sustituyen por listas preliminares.
