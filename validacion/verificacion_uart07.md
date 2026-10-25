# Revisión UART07 — versión para captura inicial

Fecha: 2026-10-25. Actualiza la revisión UART anterior.

- Informe integrado con asignaciones X1.206 y X1.214, pull-up A2Y de 47 kohm, pasivos y TVS propuesto. Citas y entornos comprobados; PDF no compilado.
- Libro: añadidos coeficiente térmico, tolerancia, resistencia independiente de A2Y y márgenes por dirección. Resultados anteriores a Calculos!A79 conservados.
- Carga A2Y: 46,1826 uA; carga B1Y: 87,9256 uA. La prueba temporal con 10 kohm en A2Y supera 100 uA; restaurados 47 kohm.
- Márgenes hacia Verdin: 0,185/0,395 V; hacia ADCS bajo contrato: 0,38/0,80 V. No validan los márgenes hacia las entradas del TXU0202.
- Recalculado y escaneado sin errores de fórmula; revisadas visualmente las regiones modificadas. Sin comprobación en Excel nativo.
- Márgenes completos de entrada TXU0202 y coordinación ESD siguen abiertos. No se ha modificado ni validado el esquemático de Santiago.
- La copia local de IMX8MPIEC permanece pendiente por fallo de descarga; la fuente consultada y su localizador están registrados. Las fichas de pasivos y TVS se archivaron.
