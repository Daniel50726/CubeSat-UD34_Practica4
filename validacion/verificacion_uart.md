# Verificación documental y de cálculos UART

Fecha: 2026-10-25. Selección SEL-004.

- Integrada la propuesta aprobada del TXU0202DCUR en el informe, junto con sus fuentes y condiciones de cierre. El pinout empleado corresponde al encapsulado DCU.
- Entradas A90:F97: resistencias, tolerancias, envolventes de tensión, fugas y desacoplo. Se distingue dato de fabricante de hipótesis y requisito externo.
- Calculos A79:D86: fórmulas de resistencia mínima/máxima, corriente, potencia y caída por fuga. Resultados: 9900/10100 ohm; 0,196970/0,363636 mA; 0,384091/1,309091 mW; 0,1212 V.
- Sensibilidad: al duplicar la resistencia nominal, la corriente y potencia se reducen a la mitad y la caída por fuga se duplica. Restaurado 10 kohm.
- Fuga adicional cero produce 0,0202 V; restaurada a 10 uA. La fuga del traductor se conserva.
- Recalculado con Artifact Tool. Sin errores de fórmula detectados. Rangos anteriores de entradas, cálculos y restricciones conservan sus valores; fórmulas anteriores de Calculos preservadas.
- Inspeccionadas visualmente las tres regiones añadidas. No se abrió Excel nativo.
- Comprobadas referencias y correspondencia de entornos LaTeX. No se compiló PDF; revisión de maquetación pendiente.
- No se han validado físicamente umbrales, secuencia, tolerancia del módulo ADCS apagado, ESD ni implementación Altium. La caída por fuga no es por sí sola una prueba de compatibilidad lógica.
