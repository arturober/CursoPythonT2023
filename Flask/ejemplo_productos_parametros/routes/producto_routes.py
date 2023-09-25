from flask import Blueprint, jsonify, request
from models import Producto
from sqlalchemy import select
from db import db
from schemas import validate_json, ProductoSchema

productos = Blueprint('productos', __name__)

@productos.get("")
def get_productos():
    query = request.args
    st = select(Producto)  # SELECT * FROM producto
    if query.get('nombre'):
        st = st.where(Producto.nombre.like('%' + query.get("nombre") + '%'))
    if query.get('order'):
        st = st.order_by(query.get('order'))
    productos = db.session.execute(st).scalars().all()
    return jsonify(productos)


@productos.get("/<int:id>")
def get_producto(id: int):
    producto = db.get_or_404(Producto, id)
    return jsonify(producto)


@productos.post("")
@validate_json(ProductoSchema)
def insert_producto():
    json = request.validated_data
    producto = Producto(nombre=json["nombre"], precio=json["precio"])
    db.session.add(producto)
    db.session.commit()
    return jsonify(producto), 201  # 201 (CREATED)


@productos.put("/<int:id>")
@validate_json(ProductoSchema)
def update_producto(id: int):
    json = request.validated_data
    producto = db.session.get(Producto, id)
    if not producto:
        return {"error": "Producto no encontrado"}, 404
    producto.nombre = json["nombre"]
    producto.precio = json["precio"]
    db.session.commit()
    return jsonify(producto)


@productos.delete("/<int:id>")
def delete_producto(id: int):
    producto = db.session.get(Producto, id)
    if not producto:
        return {"error": "Producto no encontrado"}, 404
    db.session.delete(producto)
    db.session.commit()
    return "", 204  # No Content(204)