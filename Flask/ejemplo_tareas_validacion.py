from dataclasses import dataclass
from functools import wraps
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, select
from marshmallow import Schema, ValidationError, fields, validate

def validate_json(schema):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            try:
                data = request.json
                schema_instance = schema()
                validated_data = schema_instance.load(data)
                request.validated_data = validated_data  # Almacena los datos validados
                return view_func(*args, **kwargs)
            except ValidationError as error:
                return (
                    jsonify(
                        {
                            "error": "Datos de entrada no válidos",
                            "messages": error.messages,
                        }
                    ),
                    400,
                )

        return wrapper

    return decorator

app = Flask(__name__)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tareas.sqlite"
db.init_app(app)  # Registramos SQLAlchemy en la aplicación


@dataclass
class Tarea(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    descripcion: Mapped[str] = mapped_column(String(255))
    realizada: Mapped[bool] = mapped_column(default=False)


class TareaSchema(Schema):  # Validar los datos del producto del cliente
    descripcion = fields.String(
        required=True,
        error_messages={"required": "La descripción es obligatoria"},
        validate=validate.Length(min=5, error="La descripción debe tener al menos 5 letras"),
    )

with app.app_context():
    db.create_all()  # Creamos las tablas en la BD


@app.get("/tareas")
def get_tareas():
    st = select(Tarea)  # SELECT * FROM tarea
    tareas = db.session.execute(st).scalars().all()
    return jsonify(tareas)


@app.post("/tareas")
@validate_json(TareaSchema)
def insert_tarea():
    json = request.json
    tarea = Tarea(descripcion=json["descripcion"])
    db.session.add(tarea)
    db.session.commit()
    return jsonify(tarea), 201 # 201 (CREATED)

@app.put("/tareas/<int:id>/realizar")
def realizar_tarea(id: int):
    tarea = db.session.get(Tarea, id)
    if not tarea:
        return { "error" : "Tarea no encontrada" }, 404
    tarea.realizada = True
    db.session.commit()
    return jsonify(tarea)

@app.delete("/tareas/<int:id>")
def delete_tarea(id: int):
    tarea = db.session.get(Tarea, id)
    if not tarea:
        return { "error" : "Tarea no encontrada" }, 404
    db.session.delete(tarea)
    db.session.commit()
    return "", 204 # No Content(204)

app.run()
