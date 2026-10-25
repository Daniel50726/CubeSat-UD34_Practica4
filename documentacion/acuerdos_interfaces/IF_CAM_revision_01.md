# Interfaz de cámara — revisión 02

Estado: definición funcional parcial. Cámara de referencia: XIMEA MQ022HG-IM-SM5X5-7NIR2. Fuente: SRC-001 y SRC-002. Fecha inicial: 2026-10-24; actualizado el 2026-10-25 con el contrato de módulos externos. Se conserva el nombre de archivo para mantener sus enlaces.

| Interfaz | Definición | Pendiente para cerrar |
| --- | --- | --- |
| IF-07 | Control de cámara mediante USB_2 del Verdin 00631101 como anfitrión USB3 | SDK en esta plataforma (hipótesis de integración) y secuencia de configuración |
| IF-08 | Recepción de cuadros brutos por USB3; escenario RAW16 | Tasa efectiva, buffers, relleno, metadatos y tiempos |
| IF-02 | Cámara alimentada a través de USB3 por el conjunto externo | Topología VBUS, tensión admisible, corriente de arranque y máxima, protección externa |
| J_CAM | Puerto de la PCB y cable hacia Micro-B USB3 de cámara | Referencia del conector del lado PCB, pinout y envolvente |

IF-07 e IF-08 son funciones que comparten el enlace físico. No se añade por defecto un bus SPI para controlar esta cámara. Las señales GPIO opcionales del dispositivo no se asignan hasta justificar su uso.

La conexión USB requiere función anfitrión y controladores compatibles. No basta que el procesador tenga un puerto USB genérico. Se debe comprobar su velocidad, papel host/device, PHY, alimentación y soporte de software.

La cámara y su suministro de energía pertenecen al conjunto externo. Su consumo se mantiene como dato del sistema, sin sumarlo por defecto al presupuesto de entrada de la PCB integrada. Como la cámara recibe energía por USB, debe definirse la conexión de VBUS, retorno y prevención de retroalimentación hacia el anfitrión. No se supone una entrada de energía independiente ni se aprueba eliminar VBUS o unir fuentes. Esta topología sigue pendiente de cierre eléctrico.

No hay asignación física de contactos aprobada. La numeración se establecerá con el conector y el controlador elegidos. Las restricciones PCB-01 a PCB-05 se registran en la hoja Restricciones del libro de cálculo.
