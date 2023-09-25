from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import productos_blueprint
from db import db

app = Flask(__name__)

app.register_blueprint(productos_blueprint, url_prefix='/productos')

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///productos.sqlite"
# Para MySQL/MariaDB instalar esto -> pip install PyMySQL (y crear la base de datos en MySQL)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/productos"
db.init_app(app)  # Registramos SQLAlchemy en la aplicación

app.run()