"""Escenarios de diseño aprobados el 2026-10-25; no son mediciones.

Fuente de entradas y justificación: documentacion/propuesta_almacenamiento.md.
Unidades decimales: MB=10**6 bytes, GB=10**9 bytes.
"""
from decimal import Decimal as D

CUADRO_BYTES = 2048 * 1088 * 2
IMAGENES_DIA = 10
RESULTADOS_FRACCION_RAW = D('1')
AUXILIARES_MB_DIA = D('2')
OCUPACION_INICIAL_GB = D('1')
RESERVA_LIBRE_GB = D('3')
CAPACIDAD_UTIL_ACEPTACION_GB = D('15')

raw_mb_dia = D(CUADRO_BYTES * IMAGENES_DIA) / 10**6
total_mb_dia = raw_mb_dia * (1 + RESULTADOS_FRACCION_RAW) + AUXILIARES_MB_DIA
def capacidad_requerida_gb(dias):
    return OCUPACION_INICIAL_GB + total_mb_dia * dias / 1000 + RESERVA_LIBRE_GB

if __name__ == '__main__':
    print(f'RAW_MB_dia={raw_mb_dia}')
    print(f'total_presupuestado_MB_dia={total_mb_dia}')
    for dias in (30, 90, 180):
        requerida = capacidad_requerida_gb(dias)
        print(f'dias={dias}; capacidad_util_requerida_GB={requerida}; cumple_umbral_15GB={requerida <= CAPACIDAD_UTIL_ACEPTACION_GB}')
    print(f'margen_90_dias_GB={CAPACIDAD_UTIL_ACEPTACION_GB-capacidad_requerida_gb(90)}')
    print(f'dias_limite_capacidad={(CAPACIDAD_UTIL_ACEPTACION_GB-OCUPACION_INICIAL_GB-RESERVA_LIBRE_GB)*1000/total_mb_dia}')
    print(f'bus_4bits_25MHz_MB_s={D(4)*25/8}')
    print(f'escritura_objetivo_par_en_2s_MB_s={D(2*CUADRO_BYTES)/2/10**6}')
    print(f'volumen_logico_anual_GB={total_mb_dia*365/1000}')
