# Verificación de interfaces

Fecha: 2026-10-25.

- Contratos funcionales aprobados: módulos externos EPS y ADCS, lógica externa de 3,3 V, energía de cámara externa y SPI interno con comunicaciones.
- Informe, evaluación Verdin, acuerdo de cámara y restricciones del libro sincronizados. No se asignan pines físicos ni se declara validada la topología VBUS.
- UART 115200 bit/s, 8N1: 10 bits transmitidos por byte y techo de 11520 bytes/s antes de cabeceras. No demuestra suficiencia frente a una demanda aún desconocida.
- Prueba de dependencia: 57600 bit/s produce 5760 bytes/s; restaurados 115200 bit/s.
- Los resultados previos de Calculos!B6:B72 permanecen iguales después de recalcular.
- Escaneo de errores de fórmulas sin coincidencias. Revisadas visualmente las tres regiones añadidas del libro.
- Citas y correspondencia de entornos LaTeX comprobadas. No se compiló PDF ni se abrió Microsoft Excel nativo.
- Sin validación eléctrica, ERC, prueba física o modificación de los esquemáticos de Altium.
