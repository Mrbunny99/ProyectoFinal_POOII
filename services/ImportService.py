import threading
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from accessData.entities.models import BaseDeDatos
from accessData.conexion import engine

class HistorialImportacion(BaseDeDatos):
    __tablename__ = 'historial_importacion'
    id = Column(Integer, primary_key=True, autoincrement=True)
    accion = Column(String(255))

BaseDeDatos.metadata.create_all(engine)

def import_historial(db: Session):
    # Leer todas las líneas del archivo 'historial.txt'
    with open('historial.txt', 'r') as file:
        lines = file.readlines()

    def insert_line(line):
        accion = HistorialImportacion(accion=line.strip())
        db.add(accion)
        db.commit()


    threads = []
    for line in lines:
        thread = threading.Thread(target=insert_line, args=(line,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
