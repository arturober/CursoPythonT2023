from dataclasses import dataclass
from db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

@dataclass
class Usuario(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))
