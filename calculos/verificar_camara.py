"""Cálculos preliminares; no representan una selección aprobada."""

altura_m = 550_000
paso_pixel_m = 5.5e-6
for focal_mm in (25, 50, 100):
    gsd_m = altura_m * paso_pixel_m / (focal_mm / 1000)
    print(f"f={focal_mm} mm: píxel={gsd_m:.2f} m; muestra de banda={5 * gsd_m:.2f} m")

cuadro_bytes = 2048 * 1088 * 2
diario_bytes = cuadro_bytes * 10
print(f"RAW16: {cuadro_bytes} bytes/cuadro; {diario_bytes / 1e6:.5f} MB/día")
print(f"Tasa útil de imágenes: {8 * diario_bytes / 600 / 1000:.3f} kbit/s")
for objetivo_m in (30, 10):
    focal_mm = altura_m * (5 * paso_pixel_m) / objetivo_m * 1000
    print(f"Paso de banda {objetivo_m} m: focal aproximada {focal_mm:.1f} mm")
