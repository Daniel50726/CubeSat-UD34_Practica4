# Interfaz de cámara — revisión 01

Estado: definición funcional parcial. Cámara de referencia: XIMEA MQ022HG-IM-SM5X5-7NIR2. Fuente: SRC-001 y SRC-002. Fecha: 2026-10-24.

| Interfaz | Definición | Pendiente para cerrar |
| --- | --- | --- |
| IF-07 | Control de cámara mediante interfaz USB3 y software compatible | Computador anfitrión, SDK y secuencia de configuración |
| IF-08 | Recepción de cuadros brutos por USB3; escenario RAW16 | Tasa efectiva, buffers, relleno, metadatos y tiempos |
| IF-02 | Cámara alimentada a través de su interfaz USB3 | Origen del riel, tensión admisible, corriente de arranque y máxima, protección |
| J_CAM | Puerto de la PCB y cable hacia Micro-B USB3 de cámara | Referencia del conector del lado PCB, pinout y envolvente |

IF-07 e IF-08 son funciones que comparten el enlace físico. No se añade por defecto un bus SPI para controlar esta cámara. Las señales GPIO opcionales del dispositivo no se asignan hasta justificar su uso.

La conexión USB requiere función anfitrión y controladores compatibles. No basta que el procesador tenga un puerto USB genérico. Se debe comprobar su velocidad, papel host/device, PHY, alimentación y soporte de software.

La cámara es externa a nuestra PCB. Si el puerto anfitrión suministra su energía desde la tarjeta integrada, la entrada desde potencia deberá presupuestar esa carga, las pérdidas y sus transitorios, evitando contar el consumo dos veces en el presupuesto global.

No hay asignación física de contactos aprobada. La numeración se establecerá con el conector y el controlador elegidos. Las restricciones PCB-01 a PCB-05 se registran en la hoja Restricciones del libro de cálculo.
