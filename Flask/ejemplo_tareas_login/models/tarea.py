from dataclasses import dataclass
from db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String

@dataclass
class Tarea(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    descripcion: Mapped[str] = mapped_column(String(255))
    realizada: Mapped[bool] = mapped_column(default=False)
    id_usuario: Mapped[int] = mapped_column(ForeignKey("usuario.id")) # tabla.columna
