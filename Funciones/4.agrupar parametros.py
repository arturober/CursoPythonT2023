# *aficiones se transforma en tupla con todos los valores recogidos
def info_persona(nombre, *aficiones):
    print(f"Nombre: {nombre}. Aficiones: {aficiones}")
    
info_persona("Pepe", "Baloncesto", "Viajar", "Cine", "Comer" ) # Nombre: Pepe. Aficiones: ('Baloncesto', 'Viajar', 'Cine', 'Comer')
info_persona("Pepe", "Baloncesto") # Nombre: Pepe. Aficiones: ('Baloncesto',)
info_persona("Pepe") # Nombre: Pepe. Aficiones: ()

# Los parámetros que vayan después de la agrupación (*), deben pasarse de forma NOMINAL
def info_persona(nombre, *aficiones, edad):
    print(f"Nombre: {nombre}. Edad: {edad}. Aficiones: {aficiones}")
    
info_persona("Pepe", "Baloncesto", "Viajar", "Cine", "Comer", edad = 45) # Nombre: Pepe. Aficiones: ('Baloncesto', 'Viajar', 'Cine', 'Comer')

# Crea una función que reciba una cantidad indeterminada de numeros e imprima su media
def media(*nums):
    if(nums): # [] equivale a False
        print(f"Media: {sum(nums)/len(nums): .2f}")
    else:
        print("Debes pasar algún número")
    
media()
media(4, 6, 8)
media(4, 6, 8, 10, 22, 14, 9)

