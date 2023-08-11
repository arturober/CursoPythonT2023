# Ejemplo de Mixin. Clase que tiene un método para convertir cualquier objeto a formato JSON

import json

class JsonMixin:
    def to_json(self):
        return json.dumps(self, default=self._serialize_object, indent=2)
    
    def _serialize_object(self, obj):
        if isinstance(obj, (str, int, float, bool, type(None))):
            return obj.__repr__()
        elif isinstance(obj, (list, tuple)):
            return [self._serialize_object(item) for item in obj]
        elif isinstance(obj, dict):
            return {key: self._serialize_object(value) for key, value in obj.items()}
        else:
            return obj.__dict__
        
class Direccion(JsonMixin):
    def __init__(self, calle: str, numero: int) -> None:
        self.calle = calle
        self.numero = numero

class Persona(JsonMixin):
    def __init__(self, nombre: str, edad: int, direccion: Direccion) -> None:
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        
p = Persona("Pedro", 35, Direccion("Calle perdida", 25))
print(p.to_json())
