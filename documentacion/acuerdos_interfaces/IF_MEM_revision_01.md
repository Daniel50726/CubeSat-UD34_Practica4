# IF-09 — Almacenamiento de misión

Fecha: 2026-10-25. Referencia adoptada: Kingston SDCIT2/16GBSP. Estado: selección de arquitectura aprobada; circuito auxiliar en desarrollo.

El bus SD_1/USDHC2 del Verdin se reserva para la microSD. Modo inicial: cuatro bits, 25 MHz, señalización de 3,3 V. La eMMC interna sigue dedicada al arranque. No es un módulo adaptador SPI.

Fuente de asignación: SRC-009, tabla 53. Reservas en el conector del SoM:

| Señal | Pin SoM | Observación |
| --- | ---: | --- |
| SD_1_CMD | 74 | Comandos |
| SD_1_D0 | 80 | Datos |
| SD_1_D1 | 82 | Datos |
| SD_1_D2 | 70 | Datos |
| SD_1_D3 | 72 | Datos |
| SD_1_CLK | 78 | Reloj |
| SD_1_CD# | 84 | Detección; cierre según zócalo |
| SD_1_PWR_EN | 76 | Habilitación lógica de 1,8 V; no salida de potencia |

Las reservas no sustituyen la revisión de multiplexación ni asignan los contactos del zócalo aún no elegido. Seguir las recomendaciones Toradex de pull-ups; no añadir resistencias a 3,3 V por costumbre. El suministro de tarjeta es una rama separada de 3,3 V, cuyo máximo y arranque deben establecerse antes de cerrar protección.

Verificación prevista: al menos 15 GB útiles, RAW más resultado equivalente en hasta 2 s como objetivo, retención mecánica y estados ante reinicio/corte. Las cuotas y cálculo de retención se definen en `../propuesta_almacenamiento.md`; conservar la reserva y evitar doble conteo de registros.
