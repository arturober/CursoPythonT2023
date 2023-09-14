from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import String, Numeric, create_engine

class BaseModel(DeclarativeBase):
    pass

class Producto(BaseModel):
    __tablename__ = 'producto' # Tabla correspondiente a esta clase
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(150)) # Varchar(150)
    precio: Mapped[float] = mapped_column(Numeric(10, 2))

    def __repr__(self) -> str:
        return f"{self.id} - {self.nombre} ({self.precio: .2f})"

# Conexión a la base de datos (echo=True -> Modo depuración, imprime las consultas que genera)
engine = create_engine("sqlite:///SQLAlchemy/productos.sqlite", echo=True) 
BaseModel.metadata.create_all(engine)

silla = Producto(nombre="Silla 2", precio=50.95)
with Session(engine) as session:
    session.add(silla)
    session.commit()
    print(silla)

