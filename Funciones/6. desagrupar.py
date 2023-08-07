def info_punto_3d(x, y, z):
    print(f"Punto 3D coordenadas: {x=}, {y=}, {z=}")
    
punto = (6, 8, 4)
info_punto_3d(punto[0],punto[1],punto[2]) # Punto 3D coordenadas: x=6, y=8, z=4
info_punto_3d(*punto) # Desagrupamos tupla -> Punto 3D coordenadas: x=6, y=8, z=4
    
    
puntoDict = { "y": 8, "z": 4, "x": 6}
info_punto_3d(puntoDict["x"], puntoDict["y"], puntoDict["z"]) # Punto 3D coordenadas: x=6, y=8, z=4
info_punto_3d(**puntoDict) # Desagrupamos diccionario -> Punto 3D coordenadas: x=6, y=8, z=4

# Extraer los valores de una tupla/lista y generar nuevas tuplas o listas
nums1 = [1, 2, 3]
nums2 = (4, 5, 6)
#nums3 = nums1 + nums2
nums3 = (*nums1, *nums2)
print(nums3) # (1, 2, 3, 4, 5, 6)

# Extraer los valores de un diccionario para generar nuevos diccionarios
dic1 = { "a": 23, "b": 15 }
dic2 = { "c": 10, "d": 9 }
dic3 = { **dic1, **dic2 }
print(dic3) # {'a': 23, 'b': 15, 'c': 10, 'd': 9}
