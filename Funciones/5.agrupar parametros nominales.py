# **datos seriá un diccionario con todos los parámetros nominales que no sean el nombre
def info_persona(nombre, **datos):
    print(f"""{nombre}:
    DNI = {datos['dni']}
    correo = {datos['correo']}
    edad = {datos['edad']}""")
    
info_persona("Juan", dni = "45334623G", correo = "juan@email.com", edad = 34)
# info_persona("Juan", "45334623G", "juan@email.com", 34) # ERROR: Solo funciona con parámetros nominales

def info_persona2(nombre, *aficiones, **datos):
    print(f"""{nombre}:
    DNI = {datos['dni']}
    correo = {datos['correo']}
    edad = {datos['edad']}
    aficiones = {aficiones}""")
    
    
info_persona2("Ana", "Tenis", "Viajar", dni = "23423523T", correo = "ana@email.com", edad = 35)
'''
Ana:
    DNI = 23423523T
    correo = ana@email.com
    edad = 35
    aficiones = ('Tenis', 'Viajar')
'''
