# Algoritmo de Relleno de Polígonos - Gráficos por Computadora

## Información del Estudiante

**Nombre:** Gadiel Ocaña  
**Carnet:** 231279  
 
## Descripción del Proyecto

Este proyecto implementa un algoritmo para rellenar polígonos complejos sin el uso de librerías externas, desarrollado en Python utilizando Pygame como base de renderizado. La implementación es capaz de manejar polígonos de cualquier número de vértices, incluyendo figuras cóncavas y polígonos con agujeros internos.

## Características del Proyecto

- Renderizado de 5 polígonos diferentes con formas y complejidades variadas
- Soporte para polígonos convexos, cóncavas y con agujeros
- Contornos blancos para mejor definición visual
- Paleta de colores suaves y armoniosa
- Implementación completamente desde cero sin librerías externas de gráficos

## Polígonos Implementados

1. **Polígono Complejo**: Figura de 10 vértices con forma irregular - Color rosa claro (#F0D8D9)
2. **Cuadrilátero**: Figura de 4 vértices - Color lavanda (#E6E6FA)
3. **Triángulo**: Figura básica de 3 vértices - Color gris claro (#D3D3D3)
4. **Polígono con Agujero**: Figura compleja de 18 vértices con hueco interno - Color rosa (#FFC0CB)

## Solución Algorítmica: Scanline Fill

### Algoritmo Seleccionado

Se implementó el algoritmo **Scanline Fill** (Relleno por Líneas de Escaneo) por sus ventajas en precisión y eficiencia para el relleno de polígonos complejos.

### Funcionamiento del Algoritmo

El algoritmo opera bajo el siguiente principio:

1. **Análisis Horizontal**: Procesa el polígono línea por línea horizontalmente (scanlines)
2. **Cálculo de Intersecciones**: Para cada línea horizontal, determina dónde intersecta con los bordes del polígono
3. **Ordenamiento**: Organiza las intersecciones de izquierda a derecha
4. **Relleno por Pares**: Rellena entre cada par de intersecciones (entrada y salida del polígono)

### Ventajas de la Implementación

- **Precisión**: Garantiza relleno exacto sin desbordamiento de bordes
- **Eficiencia**: Complejidad temporal O(n×h) donde n = número de bordes, h = altura del polígono
- **Versatilidad**: Funciona con polígonos convexos, cóncavos y complejos
- **Soporte para Agujeros**: Manejo nativo de polígonos con huecos internos

### Casos Especiales Manejados

- **Polígonos Cóncavos**: El algoritmo maneja correctamente las indentaciones
- **Agujeros Internos**: Implementación específica para polígonos con huecos
- **Vértices en Scanline**: Manejo adecuado de casos límite
- **Bordes Horizontales**: Procesamiento correcto de segmentos horizontales

## Compilación y Ejecución

### Requisitos

- Python 3.7 o superior
- Pygame (única librería permitida para el contexto de ventana)

### Instalación de Dependencias

```bash
pip install pygame
