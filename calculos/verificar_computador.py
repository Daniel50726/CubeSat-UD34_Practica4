"""Cálculos de propuesta Verdin; no son mediciones del dispositivo.

Ejecutar con Python 3, sin dependencias. Fuentes y supuestos:
documentacion/evaluacion_computador_verdin.md.
"""
from decimal import Decimal as D

v_nom, tolerancia = D('5'), D('0.05')
v_min, v_max = v_nom * (1-tolerancia), v_nom * (1+tolerancia)
p_sostenida, p_pico, i_rama = D('8.25'), D('12.5'), D('3')
cuadro = 2048 * 1088 * 2
resultados = {
    'V_min_V': v_min, 'V_max_V': v_max,
    'I_sostenida_envolvente_A': p_sostenida / v_min,
    'I_pico_envolvente_A': p_pico / v_min,
    'capacidad_rama_a_Vmin_W': v_min * i_rama,
    'margen_pico_W': v_min * i_rama - p_pico,
    'margen_pico_porcentaje': (v_min * i_rama / p_pico - 1) * 100,
    'resistencia_max_ejemplo_ohm': (D('4.90') - v_min) / i_rama,
    'perdida_max_ejemplo_W': (D('4.90') - v_min) * i_rama,
    'cuadro_bytes': cuadro, 'dos_buffers_bytes': 2 * cuadro,
    'datos_imagen_dia_MB': D(10 * cuadro) / 1000000,
    'area_modulo_mm2': D('69.6') * 35,
    'ocupacion_proyectada_porcentaje': D('69.6') * 35 / (90 * 90) * 100,
}
if __name__ == '__main__':
    for clave, valor in resultados.items():
        print(f'{clave}: {valor}')
    print('Envolvente de fuente != consumo; rama SoM != baquela completa.')
