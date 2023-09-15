from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import String, Numeric, create_engine, select

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
BaseModel.metadata.create_all(engine) # Crea las tablas si no existen (CREATE TABLE)

def mostrarProductos():
    with Session(engine) as session:
        st = select(Producto) # SELECT * FROM producto
        productos = session.execute(st).scalars().all()
        print(productos)

# mostrarProductos()

def mostrarProducto(id: int):
    with Session(engine) as session:
        st = select(Producto).where(Producto.id == id) # SELECT * FROM producto WHERE id = X
        producto = session.execute(st).scalars().one_or_none()
        print(producto)
        
# mostrarProducto(3)

# INSERT
def insertarProductos():
    mesa = Producto(nombre="Mesa", precio=100)
    estanteria = Producto(nombre="Estantería", precio=85.5)
    armario = Producto(nombre="Armario", precio=234.85)
    with Session(engine) as session:
        session.add(mesa)
        session.add_all([estanteria, armario])
        session.commit()
        
# insertarProductos()

def updateProducto(id: int, nombre: str, precio: float):
    with Session(engine) as session:
        producto = session.get(Producto, id) # Equivale a select(Producto).where(Producto.id == id)
        producto.nombre = nombre
        producto.precio = precio
        session.commit()
        
# updateProducto(2, "Lámpara", 33)

def deleteProducto(id: int):
    with Session(engine) as session:
        producto = session.get(Producto, id)
        session.delete(producto)
        session.commit()
        
# deleteProducto(3)