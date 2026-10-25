# Comparación preliminar de módulos de procesamiento

Fecha: 2026-10-24. Estado: propuesta para discusión; no es una selección aprobada ni modifica el informe.

## Arquitectura acordada

Se permite un módulo con procesador, RAM y memoria de arranque. Las imágenes, telemetría y demás datos persistentes de misión se guardarán en almacenamiento independiente. Los buffers y el procesamiento activo usan la RAM del procesador. Ambos bloques se integran con la PCB central y de comunicaciones de hasta 90 × 90 mm.

## Comparación

| Candidato | Evidencia y evaluación |
| --- | --- |
| Raspberry Pi Compute Module 5 | USB3, RAM y eMMC opcional; 55 × 40 mm. Rango publicado −20 a +85 °C: no satisface el extremo inferior de ET-07. No aparece expresamente entre las plataformas probadas por XIMEA. Candidato para prototipo si se revisa el requisito térmico. |
| Toradex Verdin iMX8M Plus Quad 4GB IT, sin WB | USB 3.1 Gen 1 host, RAM integrada y memoria de arranque; 69,6 × 35 mm. Variante industrial con rango −40 a +85 °C sujeto a solución térmica. Candidato preferido para continuar el diseño académico por su correspondencia con ET-07 y sus datos públicos de consumo. XIMEA no lo enumera como plataforma probada: compatibilidad pendiente. |
| NVIDIA Jetson Orin Nano | XIMEA sí lo enumera como plataforma probada. Perfiles de potencia de varios vatios (7/15 W y, según configuración, 25 W); no son medidas del consumo de nuestra aplicación. Aceleración de IA sin requisito actual que la justifique; no se prioriza por presupuesto eléctrico. |

No se establece ganador absoluto: falta demostrar compatibilidad de cámara, presupuesto eléctrico, procesamiento, costo y disponibilidad de la referencia comercial. Ninguna opción queda acreditada para operación orbital.

## Cálculos iniciales reproducibles

- RAW16 completo: 2048 × 1088 × 2 = 4 456 448 bytes por cuadro.
- Dos buffers: 8 912 896 bytes = 8,912896 MB decimales.
- Diez cuadros por día: 44,56448 MB/día, sin archivos auxiliares ni telemetría.
- Proyección del Verdin: 69,6 × 35 = 2436 mm²; 2436 / (90 × 90) × 100 = 30,074 %. No incluye conector, fijaciones, disipación, separaciones ni demuestra encaje mecánico.

Los buffers no justifican por sí solos 4 GB. Esta capacidad se plantea como configuración candidata de catálogo; el dimensionamiento final debe incluir Linux, SDK, copias y algoritmo. Tampoco se presupone reconstrucción de 24 imágenes a resolución completa.

Toradex publica para 0063 Verdin iMX8M Plus Quad 4GB IT V1.1A, bajo la imagen de software indicada en su ensayo: 1,51 W medios en reposo sin pantalla; 2,69 W medios con cuatro núcleos estresados; 4,43 W medios y 5,26 W de pico en su ensayo de carga máxima con PHY del módulo. Son observaciones de ensayo, no máximos garantizados ni medidas de nuestro diseño.

Ejemplo de evaluación con cámara a sus 1,6 W publicados:

- 2,69 + 1,6 = 4,29 W; frente al antecedente global de 5 W quedan 0,71 W antes de almacenamiento, radio, otros bloques y pérdidas.
- 4,43 + 1,6 = 6,03 W; ese escenario ya excede el antecedente de 5 W.

La simultaneidad es una hipótesis para evaluación, no una medición. El consumo publicado de cámara no demuestra su máximo. No cerrar alimentación con estas sumas ni resolver picos únicamente mediante un ciclo de trabajo promedio. Aclaración del alcance: no existen otros equipos de diseño; los subsistemas externos se modelan mediante requisitos definidos por este proyecto. Los 5 W son un antecedente revisable. Véase `evaluacion_computador_verdin.md` para el dimensionamiento posterior de la rama del procesador.

## Condiciones para aprobar el candidato

1. Verificar xiAPI ARM64, distribución Linux, dependencias, controlador USB y cámara exacta; evidencia mediante prueba o confirmación del fabricante.
2. Definir procesamiento y tiempos; medir o estimar justificadamente RAM y carga.
3. Cerrar potencia por modo, arranque, transitorios y disipación. Revisar ET-07 en el conjunto, no solo el módulo.
4. Comprobar lógica de cada interfaz (incluidas señales de 1,8 V), adaptadores, conectores y asignación de pines.
5. Elegir almacenamiento externo y verificar escritura sostenida, retención, consumo y montaje.
6. Confirmar referencia comercial, revisión, cotización y disponibilidad antes de la BOM.

## Fuentes primarias consultadas

- XIMEA, plataformas probadas y contenido del SDK: https://www.ximea.com/support/wiki/apis/XIMEA_Linux_Software_Package
- Raspberry Pi, CM5 datasheet, interfaces y sección 4.4: https://datasheets.raspberrypi.com/cm5/cm5-datasheet.pdf
- Toradex, Verdin iMX8M Plus V1.1 datasheet, tablas de variantes, interfaces y secciones 8.5–8.6: https://docs.toradex.com/116795-verdin_imx8mp_datasheet.pdf
- Toradex, ensayos de consumo, apartado 0063 V1.1A: https://developer.toradex.com/hardware/hardware-resources/power-consumption/verdin-imx8m-plus-power-consumption/
- NVIDIA, perfiles de potencia Orin: https://docs.nvidia.com/jetson/archives/r36.5/DeveloperGuide/SD/PlatformPowerAndPerformance/JetsonOrinNanoSeriesJetsonOrinNxSeriesAndJetsonAgxOrinSeries.html

Los documentos en línea no se han archivado en esta etapa. Se conservan los entregables aprobados sin cambios; esta nota registra la evaluación para la siguiente decisión.
