from dataclasses import dataclass
from db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

@dataclass
class Tarea(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    descripcion: Mapped[str] = mapped_column(String(255))
    realizada: Mapped[bool] = mapped_column(default=False)