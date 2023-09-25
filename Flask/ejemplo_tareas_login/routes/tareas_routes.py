from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from models import Tarea
from db import db
from sqlalchemy import select
from schemas import validate_json, TareaSchema

tareas = Blueprint('tareas', __name__)

@tareas.get("")
def get_tareas():
    st = select(Tarea)  # SELECT * FROM tarea
    tareas = db.session.execute(st).scalars().all()
    return jsonify(tareas)

@tareas.get("/mias")
@jwt_required()
def get_tareas_logueado():
    id_usuario=get_jwt_identity()
    st = select(Tarea).where(Tarea.id_usuario == id_usuario)
    tareas = db.session.execute(st).scalars().all()
    return jsonify(tareas)


@tareas.post("")
@validate_json(TareaSchema)
@jwt_required()
def insert_tarea():
    json = request.json
    id_usuario=get_jwt_identity()
    tarea = Tarea(descripcion=json["descripcion"], id_usuario=id_usuario)
    db.session.add(tarea)
    db.session.commit()
    return jsonify(tarea), 201  # 201 (CREATED)


@tareas.put("/<int:id>/realizar")
@jwt_required()
def realizar_tarea(id: int):
    id_usuario=get_jwt_identity()
    tarea = db.session.get(Tarea, id)
    if not tarea:
        return {"error": "Tarea no encontrada"}, 404
    if tarea.id_usuario != id_usuario:
        return {"error": "La tarea no te pertenece"}, 403 # Forbidden
    tarea.realizada = True
    db.session.commit()
    return jsonify(tarea)


@tareas.delete("/<int:id>")
@jwt_required()
def delete_tarea(id: int):
    tarea = db.session.get(Tarea, id)
    id_usuario=get_jwt_identity()
    if not tarea:
        return {"error": "Tarea no encontrada"}, 404
    if tarea.id_usuario != id_usuario:
        return {"error": "La tarea no te pertenece"}, 403 # Forbidden
    db.session.delete(tarea)
    db.session.commit()
    return "", 204  # No Content(204)