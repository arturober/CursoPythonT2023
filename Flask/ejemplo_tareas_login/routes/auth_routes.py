from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from schemas import validate_json, UsuarioSchema
from models import Usuario
from db import db

auth = Blueprint('auth', __name__)

@auth.post("/registro")
@validate_json(UsuarioSchema)
def registro():
    json = request.json
    usuario = Usuario(nombre=json["nombre"], email=json["email"], password=json["password"])
    db.session.add(usuario)
    db.session.commit()
    return jsonify(usuario), 201  # 201 (CREATED)

@auth.post("/login")
def login():
    json = request.json
    select = (
        db.select(Usuario)
        .where(Usuario.email == json["email"])
        .where(Usuario.password == json["password"])
    )
    usuario = db.session().execute(select).scalars().one_or_none()
    if not usuario:
        return { "error" : "Usuario y/o contraseña no válidos"}, 401 # Not authorized
    token = create_access_token(usuario.id)
    return { "accessToken" : token }
    