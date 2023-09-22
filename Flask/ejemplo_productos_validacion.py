from dataclasses import dataclass
from functools import wraps
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, ValidationError,fields, validate
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Numeric, select

app = Flask(__name__)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///productos.sqlite"
# Para MySQL/MariaDB instalar esto -> pip install PyMySQL (y crear la base de datos en MySQL)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/productos"
db.init_app(app)  # Registramos SQLAlchemy en la aplicación


@dataclass
class Producto(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(255))
    precio: Mapped[float] = mapped_column(Numeric(10, 2))

class ProductoSchema(Schema): # Validar los datos del producto del cliente
    nombre = fields.String(required=True, validate=validate.Length(min=4))
    precio = fields.Number(required=True, validate=validate.Range(min=0))

def validate_json(schema):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            try:
                data = request.json
                schema_instance = schema()
                validated_data = schema_instance.load(data)
                request.validated_data = validated_data # Almacena los datos validados
                return view_func(*args, **kwargs)
            except ValidationError as error:
                return jsonify(
                    {
                    'error': 'Datos de entrada no válidos',
                    'messages': error.messages
                    }
                ), 400
        return wrapper
    return decorator

with app.app_context():
    db.create_all()  # Creamos las tablas en la BD


@app.get("/productos")
def get_productos():
    st = select(Producto)  # SELECT * FROM producto
    productos = db.session.execute(st).scalars().all()
    return jsonify(productos)

@app.get("/productos/<int:id>")
def get_producto(id: int):
    producto = db.get_or_404(Producto, id)
    return jsonify(producto)

@app.post("/productos")
def insert_producto():
    json = request.json
    producto = Producto(nombre=json["nombre"], precio=json["precio"])
    db.session.add(producto)
    db.session.commit()
    return jsonify(producto), 201 # 201 (CREATED)

@app.put("/productos/<int:id>")
def update_producto(id: int):
    json = request.json
    producto = db.session.get(Producto, id)
    if not producto:
        return { "error" : "Producto no encontrado" }, 404
    producto.nombre = json["nombre"]
    producto.precio = json["precio"]
    db.session.commit()
    return jsonify(producto)

@app.delete("/productos/<int:id>")
def delete_producto(id: int):
    producto = db.session.get(Producto, id)
    if not producto:
        return { "error" : "Producto no encontrado" }, 404
    db.session.delete(producto)
    db.session.commit()
    return "", 204 # No Content(204)

app.run()
