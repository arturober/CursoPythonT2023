from pathlib import Path

# path = Path("Ficheros", "archivos", "a.txt")
# print(path)
# print(path.absolute())

# with open(path) as f:
#     for linea in f:
#         print(linea.strip())
        
        
path = Path("Ficheros", "nuevo")
if(not path.exists()):
    path.mkdir()
    
archivo = path.joinpath("archivo.txt")
print(archivo)
with open(archivo, 'w') as f:
    f.write("Hola")