# Evaluación del computador — selección de diseño aprobada

Investigación: 2026-10-24. Revisión 02, aprobada el 2026-10-25. Los cambios correspondientes se incorporan al informe. Los fragmentos de sugerencias permanecen únicamente locales.

## Resultado y alcance

Se adopta Toradex Verdin iMX8M Plus Quad 4GB IT, familia comercial 0063, revisión V1.1B, referencia 00631101. El aviso PCN documenta el reemplazo de 00631100/V1.1A y cambios de RAM y sensor de temperatura [S2]. No se afirma existencia en inventario ni precio confirmado. Es una selección para captura esquemática académica, con compatibilidad de xiAPI en esta plataforma asumida como hipótesis explícita; no es validación funcional ni orbital.

No hay equipos externos a los que solicitar alimentación. Se especifica lo que una fuente externa ideal debe entregar; el diseño de esa fuente no forma parte de la baquela. Su idealización no elimina pérdidas, límites ni secuencias de los componentes de nuestra tarjeta.

## Configuración y funciones

Procesador y RAM se alojan en el SoM; su eMMC interna se reserva para arranque, sistema operativo y aplicación. El almacenamiento persistente de misión será un dispositivo o módulo independiente. Las imágenes se procesan en RAM; el almacenamiento conserva entradas y resultados.

La variante propuesta ofrece 4 GB de RAM, 32 GB eMMC, USB_2 anfitrión SuperSpeed y formato 69,6 × 35 mm [S1]. La elección sin WB evita incorporar una radio auxiliar no requerida. Los 4 GB son una configuración de catálogo con margen, no un mínimo demostrado por las imágenes.

Se propone como carga de trabajo base adquirir RAW16, verificar recepción, guardar archivos y metadatos, preparar bloques para comunicaciones y supervisar estados. No se justifica la selección por IA, vídeo ni procesamiento espectral avanzado. Los plazos y la simultaneidad de tareas deberán comprobarse cuando se concrete el algoritmo; esta evaluación no demuestra prestaciones de control de actitud en tiempo real.

## Compatibilidad documental

| Aspecto | Resultado |
| --- | --- |
| Conexión de cámara | Reservar USB_2 (nombre del puerto, no velocidad USB 2.0) para USB 3.1 Gen 1 host. USB_1 queda disponible para recuperación [S1]. |
| Plataforma de software | Linux ARM64 sobre BSP compatible con la revisión B. El PCN exige, para la rama BSP 6, 6.2.0 o posterior compatible; no autoriza asumir compatibilidad de cualquier versión futura [S2]. |
| SDK | XIMEA ofrece Linux ARM y controladores USB, pero no enumera Verdin entre sus plataformas probadas [S4]. No se ha instalado el SDK ni comprobado dependencias/ABI. |
| Resultado | Viabilidad arquitectónica documentada; funcionamiento conjunto no demostrado. Hipótesis del diseño académico aprobada por el autor. |

Una validación futura deberá fijar las versiones de BSP y SDK, comprobar dependencias ARM64, enumeración USB SuperSpeed, apertura de la cámara exacta y captura RAW16 sin pérdidas. Que Linux reconozca un dispositivo USB no basta. La prueba también debe registrar RAM, tiempo y tamaño real de archivos. No se ha contactado al fabricante.

## Alimentación: especificación calculada

Se propone 5 V ±5 % EN LOS PINES VCC del SoM: 4,75–5,25 V, contenido en el rango recomendado 3,135–5,5 V [S1]. Se conserva 5 V por coherencia con ET-02 y para evitar una conversión adicional dedicada al SoM; la energía de cámara se entrega mediante el conjunto externo, con topología VBUS y protección por definir en su contrato.

La guía de familia recomienda provisionar hasta 12,5 W de pico y distingue 8,25 W sostenidos [S3, §3.1]. Estas cifras son una envolvente de dimensionamiento de la familia, NO el consumo medido de este módulo. Se adopta esa envolvente por no disponer de un máximo validado para nuestra aplicación y revisión.

I_sostenida = 8,25 / 4,75 = 1,736842 A.

I_pico = 12,5 / 4,75 = 2,631579 A.

Se especifica una capacidad de suministro de 3 A para la rama dedicada al SoM, capaz de mantener la tensión durante los transitorios. A 4,75 V equivale a 14,25 W: margen de 1,75 W, o 14 %, frente a 12,5 W. La capacidad nominal a 5 V es 15 W; no se usa como consumo en energía diaria. La envolvente incluye las cargas propias del módulo; no sumar otra vez sus memorias internas.

La tolerancia se exige en el SoM: si se aplica únicamente al conector de entrada, hay que descontar caída en cable, protección, pistas y contactos. Ejemplo de presupuesto de caída, HIPÓTESIS de diseño: con al menos 4,90 V antes de la rama y 4,75 V requeridos en carga, a 3 A se exige R_total ≤ (4,90−4,75)/3 = 0,050 ohm. Es una cota a verificar; no una resistencia instalada. A esa cota, I²R = 0,45 W. Ese ejemplo cambia la exigencia al origen de la rama y no se deduce de una fuente que solo garantice 4,75 V en su salida.

Los transitorios, rampa, desacoplo, secuencia, protección y caída real se cerrarán al seleccionar circuitos. Una especificación de 3 A no sustituye esas verificaciones. Se seguirá la sección 3 de [S3], usando la hoja específica del módulo ante diferencias con la guía de familia.

El requerimiento TOTAL de entrada de la baquela se obtendrá añadiendo almacenamiento de misión, comunicaciones y auxiliares con pérdidas y simultaneidad. No se declara que 5 V/3 A alimenten toda la baquela. Los 5 W y 300 mW heredados se conservan solo como antecedentes.

## Recursos y geometría

RAW16: 2048 × 1088 × 2 = 4 456 448 bytes/cuadro. Dos buffers: 8 912 896 bytes = 8,912896 MB. Diez cuadros sin cabeceras: 44,56448 MB/día. Esto no contabiliza Linux, SDK, copias o algoritmo, ni dimensiona el almacenamiento externo final.

Área proyectada: 69,6 × 35 = 2436 mm²; fracción de una PCB 90 × 90 mm = 30,074074 %. Falta comprobar conector, fijación, altura, solución térmica y espacio de RF. El rango industrial −40 a +85 °C está condicionado por la disipación [S1]; no demuestra que el conjunto opere en todo ese rango.

## Consecuencias para el esquemático

- Reservar bloques para zócalo del SoM, alimentación supervisada, USB de cámara, recuperación, almacenamiento y enlace digital a comunicaciones.
- Muchas señales del SoM son de 1,8 V [S3]; verificar cada pin antes de conectar periféricos de 3,3 V. Alimentación de 5 V no significa lógica de 5 V.
- La energía de cámara procede del conjunto externo. El contrato USB debe cerrar VBUS, retorno y prevención de retroalimentación; la PCB conserva la responsabilidad de adaptar y proteger sus señales. No se asigna una rama de potencia de cámara a esta tarjeta.
- Reservar programación, recuperación y consola; cerrar buses de almacenamiento y radio sin conflictos de multiplexación.
- Elegir posteriormente zócalo, adaptadores de nivel y supervisores como componentes con referencias y cálculos propios.

## Consumo de operación frente a capacidad de fuente

Los ensayos disponibles para 0063 V1.1A reportan 1,51 W en reposo sin pantalla, 2,69 W con cuatro núcleos bajo estrés y 4,43 W medios/5,26 W pico en el ensayo de carga máxima con PHY del módulo [S5]. Son antecedentes de otra revisión y entorno de software, no garantía para V1.1B. No se extrapolan como valores finales de energía o corriente máxima.

E_día = suma(P_modo × t_modo) requiere tiempos y consumos del escenario definido; no se asignan tiempos arbitrarios. La capacidad de 15 W de la rama no equivale a 360 Wh/día consumidos.

## Fuentes y documentos locales

- S1: Toradex, Verdin iMX8M Plus V1.1 Datasheet, revisión documental 1.8, 2026-06-22. Tablas 7, 30 y 72; secciones 5.5 y 8.5–8.6. https://docs.toradex.com/116795-verdin_imx8mp_datasheet.pdf — `hojas_de_datos/Toradex_Verdin_iMX8M_Plus_V1_1_datasheet.pdf`.
- S2: PCN 0063 V1.1A a V1.1B, actualizado 2023-12-12. https://docs.toradex.com/114344-pcn-0063-v11a-v11b-20231127.pdf — `hojas_de_datos/Toradex_PCN_0063_V1_1A_V1_1B.pdf`.
- S3: Verdin Carrier Board Design Guide V1.2, 2022-09-15, §3.1, p.73 impresa y gestión de potencia §3. https://docs.toradex.com/108140-verdin-carrier-board-design-guide.pdf — `notas_de_aplicacion/Toradex_Verdin_Carrier_Board_Design_Guide_V1_2.pdf`.
- S4: XIMEA Linux Software Package, Supported platforms y Contents. https://www.ximea.com/support/wiki/apis/XIMEA_Linux_Software_Package
- S5: Toradex, Verdin iMX8M Plus Power Consumption, 0063 V1.1A. https://developer.toradex.com/hardware/hardware-resources/power-consumption/verdin-imx8m-plus-power-consumption/

Todas las fuentes consultadas el 2026-10-24. Cálculos reproducibles: `../calculos/verificar_computador.py`. Los cambios aprobados están integrados en `../informe/latex/main.tex` y registrados en SEL-002. El fragmento de sugerencias permanece local, excluido de Git. Los cálculos principales se incorporaron al libro XLSX el 2026-10-25: Calculos!A62:D72, con entradas y fuentes en Entradas.
