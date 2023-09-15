from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import String, Boolean, create_engine, select

class BaseModel(DeclarativeBase):
    pass

class Tarea(BaseModel):
    __tablename__ = "tarea"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    descripcion: Mapped[str] = mapped_column(String(255))
    realizada: Mapped[bool] = mapped_column(Boolean(True), default=False)
    
    def __repr__(self) -> str:
        return f"{self.id}. {self.descripcion} ({'realizada' if self.realizada else 'no realizada'})"
    
# Conexión a la base de datos (echo=True -> Modo depuración, imprime las consultas que genera)
engine = create_engine("sqlite:///SQLAlchemy/tareas.sqlite", echo=False) 
BaseModel.metadata.create_all(engine) # Crea las tablas si no existen (CREATE TABLE)

def mostrar_tareas():
    with Session(engine) as session:
        st = select(Tarea) # SELECT * FROM tarea
        tareas = session.execute(st).scalars().all()
        for t in tareas:
            print(t)
            
# INSERT
def insertar_tarea(descripcion: str):
    tarea = Tarea(descripcion = descripcion)
    with Session(engine) as session:
        session.add(tarea) # Insert
        session.commit()
        
# UPDATE (realizada = true)
def realiza_tarea(id: int):
    with Session(engine) as session:
        tarea = session.get(Tarea, id)
        tarea.realizada = True
        session.commit()
        
# DELETE
def borra_tarea(id: int):
    with Session(engine) as session:
        tarea = session.get(Tarea, id)
        session.delete(tarea)
        session.commit()
        
opcion = -1
while opcion != 0:
    print("""MENU
1) Ver tareas
2) Añadir tarea
3) Marcar tarea como realizada
4) Borrar tarea
0) Salir
""")
    opcion = int(input("Elige una opción: "))
    match opcion:
        case 1:
            mostrar_tareas() 
        case 2:
            descripcion = input("Descripción de la tarea: ")
            insertar_tarea(descripcion)
        case 3:
            mostrar_tareas()
            id = int(input("Id de la tarea a realizar: "))
            realiza_tarea(id)
        case 4:
            mostrar_tareas()
            id = int(input("Id de la tarea a borrar: "))
            borra_tarea(id)

    print()