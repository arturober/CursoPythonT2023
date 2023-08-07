def sumar(n1: int, n2: int) -> int:
    return n1 + n2

print(sumar(3, 4)) # 7

s = sumar # 2 identificadores para la misma función
print(s(4, 5)) # 9

sumar_lambda = lambda n1, n2: n1 + n2
print(type(sumar_lambda)) # <class 'function'>
print(sumar_lambda(5,7)) # 12

'''
Crea una función lambda que reciba un string y un número
Devuelve el caracter que hay en esa posición del string en mayúscula
'''
car_mayus = lambda cadena, pos: cadena[pos].upper() if pos >= 0 and pos < len(cadena) else None
print(car_mayus("Hola", 2)) # L
print(car_mayus("Hola", 34)) # None

