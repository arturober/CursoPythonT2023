def info_punto(x, y):
    print(f"Punto coordenadas: {x=}, {y=}")
    
info_punto(4, 6) # Parámetros posicionales
info_punto(y = 6, x = 4) # Parámetros nominales

def info_punto_3d(x, y, z):
    print(f"Punto 3D coordenadas: {x=}, {y=}, {z=}")
    
info_punto_3d(4, z = 8, y = -2) # x posicional, z,y nominales
#info_punto_3d(y = 5, x = 7, 3) # ERROR: No puede haber argumentos posicionales después de nominales


