# Con la sintaxis with, Python cierra automáticamente el archivo cuando acaba el bloque
# f.close()
with open("Ficheros/archivos/a.txt") as f:
    print(f.read()) # Devuelve todo el contenido como un string

# Leer las 3 primeras líneas
with open("Ficheros/archivos/a.txt") as f:
    print(f.readline().strip())
    print(f.readline().strip())
    print(f.readline().strip())

print("\nLeer línea a línea todo el fichero:")
with open("Ficheros/archivos/a.txt") as f:
    linea = f.readline()
    while(linea): # Mientras devuelva contenido
        print(linea.strip())
        linea = f.readline()
        
print("\nLeer línea a línea todo el fichero estilo Python:")
with open("Ficheros/archivos/a.txt") as f:
    for linea in f:
        print(linea.strip())     
        
print("\nDevolver el contenido de un archivo como una lista de líneas:")
with open("Ficheros/archivos/a.txt") as f:
    lineas = [linea.strip() for linea in f.readlines()] # Quitamos salto de línea con strip
    print(lineas)
    
    