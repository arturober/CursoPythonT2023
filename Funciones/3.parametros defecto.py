def info_punto(x = 1, y = 1):
    print(f"Punto coordenadas: {x=}, {y=}")
    
info_punto(4, 6) # Punto coordenadas: x=4, y=6
info_punto(5) # Punto coordenadas: x=5, y=1
info_punto() # Punto coordenadas: x=1, y=1
info_punto(y = 6) # Punto coordenadas: x=1, y=6 (x por defecto)