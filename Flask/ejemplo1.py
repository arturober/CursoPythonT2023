from dataclasses import dataclass
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Numeric, select

app = Flask(__name__)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///productos.sqlite"
db.init_app(app) # Registramos SQLAlchemy en la aplicación

@dataclass
class Producto(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(255))
    precio: Mapped[float] = mapped_column(Numeric(10,2))
    
with app.app_context():
    db.create_all() # Creamos las tablas en la BD

@app.get("/productos")
def get_productos():
    st = select(Producto) # SELECT * FROM producto
    return db.session.execute(st).scalars().all()

app.run()