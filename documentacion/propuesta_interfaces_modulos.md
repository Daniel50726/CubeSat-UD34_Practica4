# Contrato funcional de interfaces de la PCB integrada

Estado: arquitectura funcional aprobada el 2026-10-25 e integrada al informe y al libro de cálculo. El pinout, los componentes de adaptación y la implementación Altium aún no están cerrados. Los parámetros eléctricos y la temporización de SPI siguen abiertos.

## Frontera del diseño

La PCB contiene SoM Verdin, microSD y comunicaciones. Potencia, cámara y actitud son subsistemas externos definidos mediante contratos de interfaz. La potencia de cámara y actuadores se entrega externamente; no se asigna por defecto a la PCB central. Las entradas de nuestra tarjeta y la adaptación/protección de sus señales sí pertenecen al diseño.

## Asignación funcional adoptada

| Relación | Interfaz | Señales o redes funcionales | Justificación |
| --- | --- | --- | --- |
| Potencia → PCB | Alimentación regulada | +5V_IN, +3V3_IN, GND | Conservar ET-02. 5 V para SoM, 3,3 V para microSD y circuitos compatibles; alimentación de RF según selección de Santiago. Corrientes totales aún por sumar. |
| Computador ↔ potencia | I2C dedicado a 100 kHz | EPS_SCL, EPS_SDA, GND | Consultar medidas y estados mediante registros sin asignar un puerto SPI adicional. Verdin controlador; EPS destino direccionado. Dirección por asignar. |
| Potencia → supervisión local | Señales discretas propuestas | EPS_PGOOD, EPS_ALERT_N | PGOOD alimenta la lógica de supervisión; alerta comunica eventos sin depender solo de consultas I2C. Comportamiento eléctrico y estado sin alimentación deben cerrarse. |
| Computador ↔ actitud | UART a 115200 bit/s, 8N1 | ADCS_TX, ADCS_RX, GND | Conexión punto a punto con un controlador externo que agrupa mediciones y ejecuta controladores de actuadores. No implica conectar sensores crudos por UART. |
| Computador ↔ cámara | USB3 por USB_2 | D+/D−, pares SS_TX/SS_RX, GND y tratamiento explícito de VBUS | La cámara elegida determina el bus. Control y datos comparten USB. |
| Computador ↔ microSD | SD_1, 4 bits, 25 MHz | CMD, CLK, DAT0..3, CD, habilitación | Selección ya aprobada, distinta de SPI. |
| Computador ↔ comunicaciones | SPI_1, Verdin controlador | SPI_MOSI, SPI_MISO, SPI_SCK, SPI_CS_N | Acuerdo con Santiago; conexión interna sin conector intermedio. |
| Mantenimiento ↔ computador | USB_1 y UART_3 | USB de recuperación; DBG_TX, DBG_RX, GND, referencia lógica | Separar recuperación/consola de buses operativos. JTAG solo si se justifica. |

Las señales adicionales de comunicaciones COM_IRQ y COM_RESET_N son reservas propuestas, no requisitos confirmados por su dispositivo. Frecuencia SPI, CPOL/CPHA, polaridad CS, latencias, tamaño de transferencias y protocolo deben verificarse con la referencia de comunicaciones. El nombre CS_N explicita la propuesta activa en bajo; el nombre existente SPI_CS puede conservarse si su polaridad queda documentada.

## Niveles y responsabilidades

Se adopta 3,3 V en los conectores digitales externos de EPS y ADCS, con adaptación desde el dominio de 1,8 V del SoM cuando corresponda. El rango de 5 V de alimentación del módulo no es un nivel permitido en sus señales. Para I2C se requiere una adaptación apta para drenador abierto y pull-ups dimensionados a partir de capacitancia, tiempos de subida y capacidad de hundimiento; no se fijan resistencias sin esos datos.

El SPI se conectará directamente solo si el dispositivo de comunicaciones acepta los niveles del SoM. Si utiliza 3,3 V, se seleccionará adaptación con direcciones coherentes: MOSI/SCK/CS salen del OBC; MISO entra. Las reservas IRQ y RESET también requieren revisión de niveles.

La UART externa de 3,3 V se adopta para cableado corto dentro del 1U, con referencia de masa común y recorrido separado de potencia de actuadores. No se garantiza inmunidad con el nombre UART: si longitud, ruido o diferencia de tierras lo requieren, revisar una capa física diferencial. A 115200 bit/s y 8N1, el techo de carga es 115200/10 = 11520 bytes/s, antes de cabeceras y comprobaciones. Esto es capacidad del enlace, no demanda de actitud ni prueba de suficiente ancho de banda. Se propone trama con longitud, tipo, secuencia y CRC; su detalle pertenece al contrato funcional.

Se adopta un controlador ADCS externo que agrupa sensores y controladores de actuadores. Esta decisión modifica la partición funcional heredada: el computador intercambia comandos y telemetría con el módulo, sin controlar directamente cada dispositivo de actitud.

## Alimentación de cámara: condición pendiente real

La cámara XIMEA seleccionada recibe energía por su conexión USB. Asignar potencia a un módulo externo exige definir el conjunto de conexión o inyección de alimentación, VBUS, retorno y prevención de retroalimentación hacia el anfitrión. No basta eliminar el conductor de 5 V de un cable USB ni suponer que la cámara tiene una entrada independiente. El bloque externo puede resolver la entrega de energía, pero nuestra interfaz debe especificar cómo se conecta. El diseño de ese bloque externo queda fuera de alcance; el contrato eléctrico no.

Hasta cerrar esa conexión, el cambio de responsabilidad de alimentación se refleja como decisión funcional, no como un cableado USB ya validado. El informe y la evaluación del computador se han corregido para reflejar esta frontera.

## Reservas de recursos y jerarquía Altium

Se reserva SPI_1 para radio, I2C_1 para EPS, UART_1 para ADCS y UART_3 para consola; USB_2 y SD_1 mantienen sus asignaciones aprobadas. Reservar las funciones estándar evita recurrir inicialmente a alternativas que comparten los pines SD. El pinout físico definitivo y las referencias de conectores se cierran en una tabla posterior.

En la imagen compartida se observan las cuatro redes SPI entre los símbolos de hoja. Deben existir puertos con los mismos nombres en las hojas hijas; una imagen no demuestra correspondencia eléctrica ni configuración de ERC. Direcciones previstas en el OBC: MOSI, SCK y CS como salidas; MISO como entrada; inversas en comunicaciones. Compartir GND y documentar los dominios de alimentación aunque no aparezcan en esa imagen.

Los conectores hacia módulos externos se colocarán en la hoja del computador si allí se captura toda su circuitería, de acuerdo con la organización solicitada por Santiago. TOP integra las relaciones entre hojas; una señal usada solo dentro de una hoja no necesita salir artificialmente a TOP. Alimentaciones comunes y puertos de hoja deben seguir una convención acordada.

## Fuente primaria

Toradex, Verdin iMX8M Plus V1.1 Datasheet, secciones 5.5, 5.7, 5.10, 5.11 y 5.14: https://docs.toradex.com/116795-verdin_imx8mp_datasheet.pdf. Documento local registrado como SRC-009. Las velocidades EPS/ADCS, el dominio externo de 3,3 V y las señales discretas son decisiones del diseño, no requisitos del fabricante de un módulo externo seleccionado.

## Adaptación UART aprobada — 2026-10-25

Se adopta SEL-004: TXU0202DCUR, A=1,8 V y B=3,3 V local. Pin 5 desde X1.131; pin 8 hacia J_ADCS.2; pin 1 desde J_ADCS.3; pin 4 hacia X1.129; OE pin 6 con pull-down. El ADCS externo debe tolerar hasta 3,6 V en sus pines apagados, sin alimentación parásita y con fuga máxima de 10 uA por pin. La protección del traductor no detecta un apagado remoto mientras sus fuentes locales sigan activas. GPIO de OE, umbrales, protección ESD y secuencias siguen por cerrar. El informe detalla resistencias, desacoplo y cálculos.
