from flask import Blueprint, jsonify, request
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


@tareas.post("")
@validate_json(TareaSchema)
def insert_tarea():
    json = request.json
    tarea = Tarea(descripcion=json["descripcion"])
    db.session.add(tarea)
    db.session.commit()
    return jsonify(tarea), 201  # 201 (CREATED)


@tareas.put("/<int:id>/realizar")
def realizar_tarea(id: int):
    tarea = db.session.get(Tarea, id)
    if not tarea:
        return {"error": "Tarea no encontrada"}, 404
    tarea.realizada = True
    db.session.commit()
    return jsonify(tarea)


@tareas.delete("/<int:id>")
def delete_tarea(id: int):
    tarea = db.session.get(Tarea, id)
    if not tarea:
        return {"error": "Tarea no encontrada"}, 404
    db.session.delete(tarea)
    db.session.commit()
    return "", 204  # No Content(204)