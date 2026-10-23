# CubeSat UD34 — PCB central y de comunicaciones

Proyecto académico del Laboratorio de Diseño de Productos Electrónicos de la Universidad de Antioquia. La práctica 4 desarrolla el diseño electrónico y la captura esquemática de una única PCB que integra el computador de a bordo, el almacenamiento y las comunicaciones.

## Integrantes

- Daniel Felipe Yépez Taimal
- Santiago Cáceres Vásquez

Docente: Maria Katherine Plazas Olaya.

## Estado del proyecto

La arquitectura toma como antecedente la práctica 3. Se ha elaborado el contenido inicial del informe y se está organizando la documentación de la práctica 4. La selección de cámara, computador y otros componentes, las interfaces definitivas y los esquemáticos siguen en desarrollo. No se ha validado un diseño electrónico completo.

El alcance incluye componentes, cálculos, librerías, esquemático jerárquico, restricciones, validación eléctrica y costos de componentes para 10, 100 y 1000 tarjetas. El enrutamiento, los archivos de fabricación y el software de vuelo quedan fuera de esta práctica.

## Organización

| Carpeta | Contenido |
| --- | --- |
| `altium/` | Proyecto nativo y hojas esquemáticas |
| `librerias/` | Símbolos, huellas y modelos utilizados |
| `documentacion/hojas_de_datos/` | Documentación de los componentes seleccionados |
| `documentacion/notas_de_aplicacion/` | Notas y diseños de referencia |
| `documentacion/acuerdos_interfaces/` | Tablas de señales, conectores y acuerdos |
| `documentacion/referencias.csv` | Registro de fuentes y localizadores de los datos utilizados |
| `calculos/` | Cálculos, matriz de restricciones y análisis de costos editables |
| `bom/` | BOM exportada desde Altium |
| `informe/latex/` | Fuente LaTeX vigente para el repositorio |
| `validacion/` | Evidencias ERC y revisión manual |
| `entregables/` | Informe y esquemáticos finales en PDF |

Las carpetas vacías se conservan mediante archivos `.gitkeep`; su presencia no indica que el entregable esté completo.

## Abrir el proyecto de Altium

- Versión de Altium Designer: **pendiente de confirmar**.
- Archivo `.PrjPcb`: **pendiente de crear**.

Cuando exista el proyecto, abrir su archivo `.PrjPcb` desde Altium y comprobar que resuelva las librerías y los modelos incluidos. Esta sección se actualizará con la ruta exacta y las dependencias de la versión entregada.

## Compilar el informe

El archivo de trabajo es `informe/latex/main.tex`, copiado de la revisión 0.3 aceptada. Los borradores antiguos y los fragmentos de intercambio conservados en `informe/` no forman parte de la versión a publicar.

En Overleaf, cargar `informe/latex/main.tex` como documento principal y usar pdfLaTeX. Con una distribución local de LaTeX, ejecutar desde `informe/latex/`:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

La estructura del documento se ha revisado, pero su compilación y presentación visual siguen pendientes. Copiar el PDF revisado a `entregables/` cuando corresponda.

## Documentación y trazabilidad

Registrar cada fuente en `documentacion/referencias.csv`: fabricante o autor, referencia exacta, revisión, URL, fecha de consulta, archivo local y sección, tabla o página utilizada. Relacionar la fuente con el requisito o decisión que sustenta. Incorporar las hojas de datos y notas utilizadas al seleccionar los componentes.

Conservar los identificadores RF, RNF, RA, RN, ET e IF heredados. Registrar y justificar sus modificaciones. Las restricciones físicas usarán identificadores PCB-XX y mantendrán su trazabilidad.

## Historial y entrega

Realizar commits de cambios coherentes, por ejemplo:

- `docs: definir interfaces de alimentacion`
- `design: incorporar circuito de reinicio`
- `validation: corregir advertencias ERC de memoria`

Antes de entregar, comprobar la correspondencia entre proyecto, librerías, cálculos, matriz de restricciones, BOM, PDF y evidencias. Identificar la versión mediante commit o etiqueta y utilizar la misma referencia en Moodle y en la solicitud de revisión.

## Antecedentes y documentos docentes

La guía `lab004_2598575_20262.pdf` y el informe `Diseño_Lab3.pdf` se conservan localmente en la raíz como fuentes del alcance y la arquitectura heredada. Estos dos documentos no están incluidos en el repositorio público. El informe LaTeX contiene sus referencias bibliográficas y puede compilarse sin esos archivos.

Repositorio público: https://github.com/Daniel50726/CubeSat-UD34_Practica4
