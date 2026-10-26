# Entrada de alimentación del SoM — propuesta en revisión

Fecha: 2026-10-26. Arquitectura de protección de rama y contrato de 5 V ±2 % en la entrada aprobados por el usuario. Selección eléctrica de la eFuse todavía en revisión.

## Frontera y arquitectura

El EPS externo entrega alimentación regulada. La PCB integrada contiene el SoM, almacenamiento y comunicaciones. Los 3 A aprobados corresponden exclusivamente al SoM; no permiten cerrar la corriente nominal del conector común J_EPS_PWR.

Trayecto propuesto: J_EPS_PWR → +5V_EPS_IN → protección de rama → +5V_SOM → desacoplo y X1.251/253/255/257/259. El retorno es GND. No unir las dos redes de 5 V por etiquetas o puentes que anulen la protección.

Se estudia la familia TI TPS25947 como eFuse por sus funciones de limitación, arranque controlado, bloqueo de corriente inversa y protección de polaridad. La variante exacta, respuesta a fallos, umbrales, pasivos, disipación y librería están pendientes.

Fuente primaria: https://www.ti.com/product/TPS25947 y https://www.ti.com/lit/ds/symlink/tps25947.pdf

## Presupuesto preliminar de caída

Requisito aprobado: 4,75–5,25 V en los pines VCC del SoM, con capacidad de rama de 3 A.

Contrato adicional aprobado: 4,90–5,10 V en la entrada de la PCB, antes de su protección. La frontera se define entre los nodos +5V_EPS_IN y GND de la PCB, después del conector de entrada. Esto exige regular el EPS considerando el cable y sus contactos anteriores a esa frontera.

Con ese contrato, margen estático inferior disponible: 4,90 - 4,75 = 0,15 V. Resistencia total máxima equivalente desde esa frontera hasta los pines del módulo, incluido retorno: 0,15/3 = 0,050 ohm. Consumir todo este margen dejaría cero reserva para transitorios; el objetivo final debe ser menor.

TPS25947: Ron típica publicada 0,0283 ohm. A 3 A: caída típica 0,0849 V; pérdidas típicas I²R = 0,2547 W. Estos valores no prueban cumplimiento a temperatura extrema: debe usarse Ron máxima garantizada y sumar pistas, retorno y otros elementos de la rama. La corriente límite no debe fijarse simplemente en 3 A nominales sin considerar tolerancias y arranque.

## Desacoplo capturado

Cinco condensadores de 4,7 uF ±10 % y uno de 22 uF ±20 %, todos nominalmente 10 V, en paralelo entre +5V_SOM y GND. Base: guía Toradex V1.2, página 89, conjunto C1–C6 del circuito de referencia.

Fuente: https://docs.toradex.com/108140-verdin-carrier-board-design-guide.pdf

Cnom = 5 × 4,7 + 22 = 45,5 uF.
Cmin considerando solo tolerancia = 5 × 4,7 × 0,90 + 22 × 0,80 = 38,75 uF.
Cmax considerando solo tolerancia = 5 × 4,7 × 1,10 + 22 × 1,20 = 52,25 uF.
Uso de tensión nominal a 5,25 V = 5,25/10 = 52,5 %.

Faltan referencias comerciales y curvas de capacidad efectiva a tensión, temperatura y envejecimiento. Para evaluar corriente de carga debe considerarse la capacidad máxima real de toda la salida, incluida la del módulo, y su carga durante el arranque. No se ha validado respuesta transitoria ni estabilidad del EPS.

## Condiciones de cierre

### Verificación de eFuse del 2026-10-26

TI TPS25947 Rev. C, sección 6.5: Ron máxima 45 mΩ a 3 A, entrada 2,7–23 V y Tj entre −40 y 125 °C. Caída máxima resistiva: 0,135 V; pérdidas de conducción: 0,405 W. Quedan solo 15 mV (5 mΩ a 3 A) del margen inicial de 150 mV para el resto del trayecto y transitorios. No se adopta aún como selección definitiva.

Alternativa en estudio: TPS25948, hoja de datos Rev. D, sección 6.5: Ron máxima 20 mΩ a 3 A, entrada 3,5–23 V y Tj entre −40 y 125 °C. Caída resistiva: 0,060 V; pérdidas: 0,180 W; reserva restante: 90 mV. Fuente: https://www.ti.com/lit/ds/symlink/tps25948.pdf. El encapsulado es PowerWCSP de 12 contactos y paso 0,5 mm. No se considera sustituto directo: falta verificar montaje, protección frente a entrada negativa (distinta del bloqueo de corriente inversa), variante, umbrales y circuito auxiliar. No se ha aprobado esta alternativa.

Los límites resistivos no incluyen pérdidas de conmutación/arranque, tolerancias del EPS fuera del contrato ni efectos térmicos de la PCB. La comparación es de conducción estática, no una validación del circuito completo.

- Corrientes máximas por riel de la PCB completa, incluido radio, memoria y auxiliares.
- Conector, contactos, cableado, resistencia y reducción de corriente por temperatura.
- Contrato de tensión EPS con margen de distribución y transitorios.
- Variante eFuse, parámetros garantizados, protección de sobretensión, comportamiento de fallo y reinicio.
- Coordinación con corriente disponible y limitación del EPS; arranque e inrush.
- Secuenciación de periféricos y ausencia de alimentación parásita.
- Integración de la propuesta aprobada en el informe y libro de cálculo.
