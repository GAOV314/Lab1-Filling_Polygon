import pygame
from gl import Renderer


width = 800
height = 450

#Se configura la pantalla
screen = pygame.display.set_mode((width,height), pygame.SCALED)

rend = Renderer(screen)

#Mantiene los cuadros por segundo de la pantalla
clock = pygame.time.Clock()

# Paleta de colores convertida de hexadecimal a RGB normalizado (0-1)
COLORS = {
    'light_pink': [0.94, 0.85, 0.85],     # #F0D8D9
    'lavender': [0.90, 0.90, 0.98],       # #E6E6FA
    'light_gray': [0.83, 0.83, 0.83],     # #D3D3D3
    'pink': [1.0, 0.75, 0.80],            # #FFC0CB
    'lavender_blush': [1.0, 0.94, 0.96]   # #FFF0F5
}

def drawPolygon(points):
    
    rend.glColor(1, 1, 1)  
    for i in range(len(points)):
        p1 = points[i]
        p2 = points[(i + 1) % len(points)]  
        rend.glLine(p1, p2)

def fillPolygon(points, color=None):
   
    if len(points) < 3:
        return
    
    # Encontrar los límites del polígono
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)
    
    # Para cada línea de escaneo (scanline)
    for y in range(int(min_y), int(max_y) + 1):
        # Encontrar intersecciones con los bordes del polígono
        intersections = []
        
        for i in range(len(points)):
            p1 = points[i]
            p2 = points[(i + 1) % len(points)]
            
            y1, y2 = p1[1], p2[1]
            x1, x2 = p1[0], p2[0]
            
            # Verificar si la línea de escaneo intersecta con este borde
            if min(y1, y2) < y <= max(y1, y2) and y1 != y2:
                # Calcular la intersección x
                x_intersect = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                intersections.append(x_intersect)
        
        # Ordenar las intersecciones
        intersections.sort()
        
        # Rellenar entre pares de intersecciones
        for i in range(0, len(intersections), 2):
            if i + 1 < len(intersections):
                x_start = int(intersections[i])
                x_end = int(intersections[i + 1])
                
                for x in range(x_start, x_end + 1):
                    rend.glPoint(x, y, color)

def fillPolygonWithHole(outer_points, hole_points, color=None):
   
    if len(outer_points) < 3:
        return
    
   
    min_y = min(point[1] for point in outer_points)
    max_y = max(point[1] for point in outer_points)
    
 
    for y in range(int(min_y), int(max_y) + 1):
        # Encontrar intersecciones con el polígono exterior
        outer_intersections = []
        
        for i in range(len(outer_points)):
            p1 = outer_points[i]
            p2 = outer_points[(i + 1) % len(outer_points)]
            
            y1, y2 = p1[1], p2[1]
            x1, x2 = p1[0], p2[0]
            
            if min(y1, y2) < y <= max(y1, y2) and y1 != y2:
                x_intersect = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                outer_intersections.append(x_intersect)
        
        # Encontrar intersecciones con el agujero
        hole_intersections = []
        
        for i in range(len(hole_points)):
            p1 = hole_points[i]
            p2 = hole_points[(i + 1) % len(hole_points)]
            
            y1, y2 = p1[1], p2[1]
            x1, x2 = p1[0], p2[0]
            
            if min(y1, y2) < y <= max(y1, y2) and y1 != y2:
                x_intersect = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                hole_intersections.append(x_intersect)
        
        # Ordenar intersecciones
        outer_intersections.sort()
        hole_intersections.sort()
        
        
        for i in range(0, len(outer_intersections), 2):
            if i + 1 < len(outer_intersections):
                x_start = int(outer_intersections[i])
                x_end = int(outer_intersections[i + 1])
                
                
                hole_start = None
                hole_end = None
                
                if len(hole_intersections) >= 2:
                    hole_start = int(hole_intersections[0])
                    hole_end = int(hole_intersections[1])
                
                # Rellenar evitando el agujero
                for x in range(x_start, x_end + 1):
                    # Si no hay agujero o el punto está fuera del agujero, dibujarlo
                    if hole_start is None or x < hole_start or x > hole_end:
                        rend.glPoint(x, y, color)

def poligono1():
    points = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), 
              (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]
    fillPolygon(points, COLORS['light_pink']) 
    drawPolygon(points)  

def poligono2():
    points = [(321, 335), (288, 286), (339, 251), (374, 302)]
    fillPolygon(points, COLORS['lavender'])  
    drawPolygon(points)  

def poligono3():
    points = [(377, 249), (411, 197), (436, 249)]
    fillPolygon(points, COLORS['light_gray'])  
    drawPolygon(points)  

def poligono4():
    points = [(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), 
              (660, 52), (750, 145), (761, 179), (672, 192), (659, 214), (615, 214), 
              (632, 230), (580, 230), (597, 215), (552, 214), (517, 144), (466, 180)]
    
    hole_points = [(682, 175), (708, 120), (735, 148), (739, 170)]
    
  
    fillPolygonWithHole(points, hole_points, COLORS['pink']) 
    drawPolygon(points)  
    drawPolygon(hole_points)  

#Esqueleto de como funciona la pantalla
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    rend.glClear()
    
    poligono1()
    poligono2()
    poligono3()
    poligono4()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()