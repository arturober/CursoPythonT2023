
# Abre el archivo para escribir. Con 'w' sobrescribe el contenido
with open('Ficheros/archivos/prueba.txt', "w") as f:
    f.write("Casa\n")
    f.write("Coche\n")
    f.write("Árbol\n")
    
# Abre el archivo para escribir. Con 'a' añade al final
with open('Ficheros/archivos/prueba2.txt', "a") as f:
    f.write("Casa\n")
    f.write("Coche\n")
    f.write("Árbol\n")
    
    