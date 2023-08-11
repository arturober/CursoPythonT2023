import sqlite3
import os

# Ruta desde el archivo actual
db = sqlite3.connect(os.path.dirname(__file__) + "/tareas.sqlite")


def crear_tablas():
    cursor = db.cursor()
    create_table_query = """
    DROP TABLE IF EXISTS tarea;

    CREATE TABLE tarea (
        id INTEGER PRIMARY KEY,
        descripcion TEXT,
        realizada INT
    );
    """
    cursor.executescript(
        create_table_query
    )  # Ejecuta 1 o más instrucciones SQL seguidas


def mostrar_tareas():
    cursor = db.cursor()
    tareas = cursor.execute("SELECT * FROM tarea").fetchall()
    for t in tareas:
        print(f"{t[0]}. {t[1]} ({'realizada' if t[2] else 'no realizada'})")


def add_tarea():
    cursor = db.cursor()
    desc = input("Descripción nueva tarea: ")
    cursor.execute("INSERT INTO tarea(descripcion, realizada) VALUES(?, FALSE)", (desc,))
    db.commit()

def realiza_tarea():
    mostrar_tareas()
    id = int(input("Id de tarea realizada: "))
    cursor = db.cursor()
    cursor.execute("UPDATE tarea SET realizada = TRUE WHERE id = ?", (id,))
    db.commit()


def borra_tarea():
    mostrar_tareas()
    id = int(input("Id de tarea a borrar: "))
    cursor = db.cursor()
    cursor.execute("DELETE FROM tarea WHERE id = ?", (id,))
    db.commit()


# crear_tablas()

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
            add_tarea()
        case 3:
            realiza_tarea()
        case 4:
            borra_tarea()

    print()
    
db.close()
