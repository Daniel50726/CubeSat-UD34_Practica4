# Selección de almacenamiento de misión

Fecha: 2026-10-25. Estado: aprobada como SEL-003 e integrada al informe y al libro de cálculos. Se conserva el nombre de archivo para mantener los enlaces existentes.

## Recomendación

Se adopta una microSD industrial Kingston SDCIT2/16GBSP (16 GB, sin adaptador SD) en un zócalo propio de la PCB. SDCIT2/16GB es la presentación con adaptador; no se requiere el adaptador para el montaje. El módulo de memoria queda separado físicamente del SoM. No se propone una placa adaptadora genérica SPI.

La ficha de Kingston identifica estas referencias, alimentación nominal de 3,3 V, rango −40 a +85 °C, NAND TLC en modo pSLC y funciones de integridad. No publica corriente máxima o de arranque. Sus cifras de hasta 80 MB/s de escritura no son un rendimiento garantizado en nuestra interfaz; el TBW máximo de la familia corresponde a la capacidad mayor, no se atribuye a 16 GB. [S1]

## Alternativas y criterio de decisión

| Alternativa | Valor para este proyecto | Motivo de prioridad |
| --- | --- | --- |
| microSD industrial independiente | Memoria extraíble con controlador interno; integración por bus nativo SD. | Opción prioritaria por simplicidad y separación del arranque. Se debe asegurar retención mecánica. |
| eMMC adicional soldada | Evita un contacto extraíble; puede ser preferible si la retención mecánica domina. | Requiere elegir encapsulado, compatibilidad de arranque/controlador y circuito. El almacenamiento interno del SoM no satisface la separación acordada. |
| SSD NVMe | Alternativa de gran capacidad y velocidad. | La carga propuesta no demuestra necesidad de PCIe ni SSD; añade un diseño de interfaz y montaje que no se justifica por estos datos. No se afirma que todo SSD consuma más sin una referencia concreta. |

La comparación es arquitectónica; no es una cotización entre tres dispositivos ni prueba de superioridad universal. La aptitud orbital no queda demostrada.

## Escenario propuesto y supuestos

Los 16 GB son el requisito heredado ET-04. Para probar su suficiencia se plantea:

- 10 cuadros RAW16 completos por día, cada uno de 2048 × 1088 × 2 = 4 456 448 bytes: 44,56448 MB/día. Se conserva el escenario ya aprobado, no se supone vídeo continuo.
- Retención: 90 días sin descarga, escenario de contingencia deliberadamente amplio, sin derivarlo de un análisis orbital. Se muestran también 30 y 180 días.
- Resultados: cuota diaria igual al volumen RAW (44,56448 MB). Es una reserva para productos derivados, NO un algoritmo definido ni una segunda copia redundante. No asignar ese mismo espacio a ambas funciones.
- Metadatos, telemetría, índices y eventos: cuota conjunta propuesta de 2 MB/día, no medición ni recuperación de la estimación antigua de 1,2 MB/día. Habrá que comprobar que la configuración de registros la respete.
- Ocupación inicial máxima de 1 GB al comenzar la contingencia. Se deberá implementar una política de descarga/depuración que mantenga esa condición; si ya hay más datos, recalcular.
- Reserva libre de 3 GB para operación y contingencias. No es un porcentaje garantizado por el fabricante ni espacio ocupado por formato.
- Capacidad útil de aceptación de al menos 15 GB decimales, a verificar después del formato y la configuración. No se identifica la capacidad nominal de 16 GB con 16 GB útiles; el GB y el GiB son unidades diferentes.

Se propone exigir las cuotas en operación y recalcular si el algoritmo, número de cuadros, registro de eventos o retención cambia.

## Cálculo y sensibilidad

D_total = 44,56448 + 44,56448 + 2 = 91,12896 MB/día.

C_requerida = C_inicial + D_total × T + C_reserva.

| Días sin descarga | Capacidad útil requerida, GB decimales | Frente a 15 GB útiles |
| --- | ---: | --- |
| 30 | 6,7338688 | Cumple bajo los supuestos |
| 90 | 12,2016064 | Cumple bajo los supuestos |
| 180 | 20,4032128 | No cumple |

El margen de 90 días frente a 15 GB útiles es 2,7983936 GB ADICIONALES a la reserva de 3 GB ya incluida. No se vuelve a sumar la reserva. El límite aritmético es aproximadamente 120,71 días bajo las mismas cuotas; no se ofrece como garantía de retención física de NAND.

La producción lógica anual es 33,2620704 GB. No es escritura física de NAND: faltan amplificación, sistema de archivos y tareas internas. Por ello no se deduce vida útil ni TBW disponible para la variante de 16 GB.

## Interfaz prevista

Toradex expone USDHC2/SD_1 con cuatro bits, separado de la eMMC interna. Su modo Default Speed admite 25 MHz con señalización de 3,3 V; la documentación Linux muestra uso de tarjeta SD en Verdin iMX8M Plus. [S2, S3]

Se propone comenzar en ese modo para reducir exigencias de velocidad y evitar depender de la conmutación UHS a 1,8 V. El controlador y su configuración deben mantener esa elección; la inicialización tiene su secuencia propia. El techo bruto es 4 × 25 MHz / 8 = 12,5 MB/s. No es velocidad sostenida del sistema de archivos.

Como objetivo de diseño, escribir un RAW y un resultado de igual tamaño (8 912 896 bytes) en hasta 2 s exige 4,456448 MB/s útiles. Es una meta propuesta a comprobar, no una prestación demostrada por la clase comercial de la tarjeta. Las ráfagas y bloqueos requieren buffers; diez cuadros diarios no justifican por sí solos el desempeño instantáneo. Si el objetivo falla, revisar modo SD, planificación o dispositivo.

SD_1_PWR_EN trabaja a 1,8 V aunque el bus SD opere a 3,3 V; se necesita un interruptor de alimentación cuyo EN sea compatible o una adaptación. No es una salida que alimente la tarjeta. No añadir pull-ups externos por costumbre: seguir el diseño Toradex y revisar configuración de los existentes. [S2]

## Alimentación, integridad y montaje

La rama de 3,3 V de la tarjeta se dimensionará separadamente de los 3 A reservados al SoM. No se asigna consumo inventado. Sin corriente de pico ni arranque publicadas, la selección de regulador, interruptor y protección queda abierta. P = 3,3 × I permite actualizar el cálculo cuando se disponga de un límite aplicable; un presupuesto asignado no se presentará como dato de Kingston.

Las funciones publicadas de protección ante fallo de energía no equivalen a garantía de conservación del último archivo o consistencia de Linux. Se prevé cerrar/sincronizar archivos, comprobar integridad y no retirar energía mientras hay escrituras; la política concreta y cualquier reserva de energía requieren diseño posterior. Mantener RAW y resultados en la misma tarjeta no da redundancia frente a fallo de tarjeta.

La microSD debe quedar retenida mecánicamente, protegida contra expulsión accidental y accesible solo en mantenimiento. El zócalo, ESD, desacoplo y circuito de alimentación serán selecciones posteriores. El formato FAT32 que describe la ficha no obliga a conservar ese sistema de archivos; su selección queda abierta. El almacenamiento de misión no contendrá una imagen arrancable que altere el arranque previsto desde eMMC.

## Decisión aprobada y alcance

Se aprobaron la referencia Kingston SDCIT2/16GBSP, los 90 días con las cuotas y reservas anteriores y el bus SD nativo de cuatro bits a 3,3 V y 25 MHz como modo inicial. La aprobación no cierra consumo, circuito auxiliar ni rendimiento experimental.

## Fuentes primarias

- S1: Kingston, Industrial microSD Memory Card, SDCIT2; ficha de dos páginas, identificación MKD-02122026 (se conserva sin reinterpretar su fecha). https://www.kingston.com/datasheets/sdcit2_en.pdf
- S2: Toradex, Verdin iMX8M Plus V1.1 Datasheet, §5.14, tablas 51–53. https://docs.toradex.com/116795-verdin_imx8mp_datasheet.pdf
- S3: Toradex, SD/MMC Card (Linux). https://developer.toradex.com/linux-bsp/application-development/peripheral-access/sdmmc-card-linux/

Consulta: 2026-10-25. El script `../calculos/verificar_almacenamiento.py` reproduce los escenarios. El libro `../calculos/calculos_y_restricciones.xlsx` contiene las entradas en Entradas!B24:B26 y B46:B55, los cálculos en Calculos!A38:D58 y las restricciones PCB-06 a PCB-08. La sección está incorporada en el informe; el fragmento LaTeX de consulta se conserva únicamente local. Fuentes equivalentes del registro: S1 = SRC-012, S2 = SRC-009, S3 = SRC-013.
