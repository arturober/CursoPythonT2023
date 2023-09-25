from dataclasses import dataclass
from functools import wraps
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, select
from marshmallow import Schema, ValidationError, fields, validate
from db import db
from routes import tareas_blueprint

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tareas.sqlite"
db.init_app(app)  # Registramos SQLAlchemy en la aplicación

app.register_blueprint(tareas_blueprint, url_prefix="/tareas")

with app.app_context():
    db.create_all()  # Creamos las tablas en la BD


app.run()
