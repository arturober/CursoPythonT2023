from flask import Flask
from flask_jwt_extended import JWTManager
from db import db
from routes import tareas_blueprint, auth_blueprint

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tareas_login.sqlite"
app.config["JWT_SECRET_KEY"] = "clave_token"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 36000 # 10 horas

JWTManager(app)

db.init_app(app)  # Registramos SQLAlchemy en la aplicación

app.register_blueprint(tareas_blueprint, url_prefix="/tareas")
app.register_blueprint(auth_blueprint, url_prefix="/auth")

with app.app_context():
    db.create_all()  # Creamos las tablas en la BD


app.run()
