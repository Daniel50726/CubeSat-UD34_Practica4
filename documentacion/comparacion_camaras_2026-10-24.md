# Comparación preliminar de cámaras y óptica

Fecha de consulta: 24 de octubre de 2026. Estado: análisis para discusión; no constituye selección final ni modifica las especificaciones del informe. Fuentes primarias consultadas en línea; los PDF técnicos aún no se han archivado localmente.

## Comparación

| Candidata | Datos publicados | Evaluación para el proyecto |
| --- | --- | --- |
| XIMEA MQ022HG-IM-SM5X5-7NIR2 | Activa; 24 canales, 665–960 nm; USB3; 1,6 W; 26,4 × 26,4 × 36,8 mm; 35 g; 0–50 °C. | Candidata principal para estudiar la interfaz electrónica. Consumo máximo, óptica y viabilidad orbital pendientes. |
| SILIOS CMS-V | 8 bandas y un canal B&W; 550–830 nm; USB3; 1280 × 1024 bruto, 426 × 339 espectral; cuerpo 35 × 35 × 40 mm. | Alternativa con menor volumen bruto de datos; consumo no publicado en la página consultada. La página mezcla masas menores de 75 g y 90 g: requiere confirmación. |
| Simera MultiScape50 | 7 bandas VNIR y PAN; 5,5 W en captura; 120,5 × 95,88 × 90,17 mm; 0,51 kg; control SPI/I²C entre otras opciones y datos LVDS/SpaceWire. | Referencia espacial. No se ha demostrado su integración en el satélite 1U; excede por sí sola el presupuesto máximo de potencia heredado de 5 W. |
| XIMEA MQ022HG-IM-SM4X4-RN2 | El fabricante indica fin de vida y producto descontinuado. | No se prioriza para un diseño nuevo. |

Fuentes y localizadores:

- [XIMEA 7NIR2, tablas Sensor, Camera y Mechanical properties](https://www.ximea.com/products/hyperspectral-imaging/xispec-hyperspectral-miniature-cameras/imec-sm-range-600-1000-usb3-hyperspectral-camera).
- [SILIOS CMS, Specifications y Spectral Specifications](https://www.silios.com/cms-series).
- [Simera MultiScape50, Technical specifications](https://simera-sense.com/products/multiscape50/).
- [Estado del modelo XIMEA RN2](https://www.ximea.com/products/hyperspectral-imaging/xispec-hyperspectral-miniature-cameras/imec-sm-range-rednir-usb3-hyperspectral-camera).

Las dimensiones son del dispositivo publicado, no del conjunto con óptica, soporte y cable. No se ha obtenido cotización; no se asigna un costo estimado ni cero.

## Muestreo espacial: limitación principal

El manual xiSpec2 indica aproximadamente 409 × 217 muestras por banda para el mosaico 5 × 5. Para capturar datos originales recomienda RAW8 o RAW16; la reconstrucción espectral necesita procesamiento y calibración adicionales. También recomienda ángulos de incidencia menores de 5° en el sensor, idealmente con óptica telecéntrica del lado imagen. Estos criterios impiden elegir la lente únicamente por su montura.

Fuente: [manual xiSpec2, portada versión 2.03 de septiembre de 2026; secciones 3.4, 4.1 y 10.1, páginas 15, 16 y 68](https://www.ximea.com/getattachment/b750b3ca-2b30-42bf-bc83-4c5261ef52c6/xiSpec-Hyperspectral-HSI-mini-cameras_Technical-manual-DWL_manual.pdf). Los pies de página aún indican V2.00; conservar esa discrepancia al registrar la revisión.

Cálculo propio de primer orden, con observación al nadir, plano local y sin evaluar desenfoque, movimiento, atmósfera ni respuesta óptica:

`GSD_pixel ≈ H × p / f`

Para H = 550000 m y paso físico p = 5,5 µm, una muestra de la misma banda se repite cada cinco píxeles; su separación nominal es `5 × GSD_pixel`.

| Focal supuesta | Paso proyectado de píxel físico | Separación nominal entre muestras de una banda |
| --- | --- | --- |
| 25 mm | 121 m | 605 m |
| 50 mm | 60,5 m | 302,5 m |
| 100 mm | 30,25 m | 151,25 m |

Estos resultados son escalas de muestreo, no una demostración de resolución efectiva. La interpolación no crea mediciones independientes. Para 30 m entre muestras de una banda se necesitarían aproximadamente 504 mm de focal; para 10 m, 1513 mm. Focal y longitud física no son equivalentes, pero esos valores requieren una solución óptica que no está definida para este 1U.

Referencia conceptual: [Edmund Optics, Imaging Lenses for UAVs](https://www.edmundoptics.com/knowledge-center/application-notes/imaging/imaging-lenses-for-uavs/).

Se revisó como ejemplo real la [Kowa LM50HC-VIS-SW](https://www.kowavision.com/products/lm50hc-vis-sw): focal de 50 mm, montura C, cobertura de 1 pulgada, enfoque a infinito, cuerpo Ø39,5 × 71 mm y masa de 155 g. Con el cuerpo de cámara, la masa aritmética es 190 g antes de soporte y cable. No se adopta: falta comprobar incidencia, corrección espectral y dimensiones del conjunto ensamblado; tampoco resuelve el muestreo de lotes pequeños. No se suman longitudes de catálogo como si fueran un plano de montaje.

## Consecuencias electrónicas de evaluar la XIMEA

La tabla del modelo publica sensor de 2048 × 1088, paso de 5,5 µm, conversión de 10 bits y alimentación por USB3. Se usan los datos específicos del modelo frente a descripciones generales de familia. El valor de 1,6 W no identifica un máximo de arranque; su equivalencia a 5 V es 0,32 A, únicamente como estimación de trabajo.

Para un cuadro completo, sin cabeceras ni relleno por línea:

- RAW16: 2048 × 1088 × 2 = 4 456 448 bytes ≈ 4,456 MB.
- Diez cuadros/día: 44,56448 MB/día.
- Descarga en 600 s: 594 193 bit/s ≈ 594,2 kbit/s útiles solo para imágenes.
- RAW8 ocuparía la mitad, pero implica revisar si la precisión de 8 bits satisface la medición; no se adopta como reducción gratuita.

Una adquisición se define aquí como un único cuadro bruto, no una secuencia ni un cubo reconstruido. El supuesto RAW16 mantiene las muestras de 10 bits en contenedores de 16 bits. No se multiplica nuevamente por 24. La tasa interna de entrega y el enlace con tierra deben dimensionarse por separado.

XIMEA publica soporte de xiAPI para Linux ARM y plataformas probadas, entre ellas Raspberry Pi 4 y varias Jetson. Esto permite investigar un computador anfitrión USB3, pero no valida automáticamente cualquier módulo ARM ni su consumo. Fuente: [XIMEA Linux Software Package, Supported platforms](https://www.ximea.com/support/wiki/apis/XIMEA_Linux_Software_Package).

## Recomendación y decisión pendiente

Priorizar la XIMEA 7NIR2 para evaluar la electrónica por su estado activo y documentación. No declararla solución final de observación de lotes a 550 km. Antes debe definirse el tamaño mínimo del área que la misión pretende distinguir y comprobar la óptica correspondiente.

Si el objetivo académico se limita a demostrar adquisición, almacenamiento y transmisión espectral, puede adoptarse como cámara de referencia eléctrica, registrando que la capacidad de observación orbital de lotes no queda demostrada. Esto constituye una delimitación de alcance que debe aceptarse explícitamente, no una consecuencia automática de utilizar componentes industriales.

Si se mantiene la observación detallada de lotes desde 550 km como requisito verificable, debe continuar el análisis de carga útil y posiblemente revisar el formato del satélite. Ninguna alternativa examinada demuestra hoy el cumplimiento simultáneo de detalle de lote, 1U, potencia e integración.
