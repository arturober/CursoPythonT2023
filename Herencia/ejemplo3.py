# Ejemplo de herencia múltiple (No recomendado usarla en la vida real)
class A:
    def hola(self):
        print("Soy un método heredado de A")

class B:
    def hola(self):
        print("Soy un método heredado de B")

class C(A,B):
    pass

obj = C()
obj.hola() # "Soy un método heredado de B"
print(C.mro()) # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]