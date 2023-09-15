from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Numeric

app = Flask(__name__)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///productos.db"
db.init_app(app) # Registramos SQLAlchemy en la aplicación

class Producto(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(255))
    precio: Mapped[float] = mapped_column(Numeric(10,2))
    
with app.app_context():
    db.create_all() # Creamos las tablas en la BD

@app.get("/hola")
def hola():
    return "Hola mundo"

app.run()