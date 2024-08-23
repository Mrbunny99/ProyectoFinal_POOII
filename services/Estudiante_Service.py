from sqlalchemy.orm import Session
from accessData.entities.models import Estudiante
from services.basedatosservices import BaseDatosServices

class EstudianteService(BaseDatosServices):

    def create(self, db: Session, entity: Estudiante):
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    def update(self, db: Session, entity_id: int, new_data: dict):
        estudiante = db.query(Estudiante).filter(Estudiante.id == entity_id).first()
        if estudiante:
            if 'nombre' in new_data:
                estudiante.nombre = new_data['nombre']
            elif 'apellido' in new_data:
                estudiante.apellido = new_data['apellido']
            elif 'edad' in new_data:
                estudiante.edad = new_data['edad']
            elif 'mail' in new_data:
                estudiante.mail = new_data['mail']
            elif 'matricula' in new_data:
                estudiante.matricula = new_data['matricula']
            elif 'carrera' in new_data:
                estudiante.carrera = new_data['carrera']
            db.commit()
            db.refresh(estudiante)
        return estudiante

    def delete(self, db: Session, entity_id: int):
        estudiante = db.query(Estudiante).filter(Estudiante.id == entity_id).first()
        if estudiante:
            db.delete(estudiante)
            db.commit()
        return estudiante

    def select_all(self, db: Session):
        return db.query(Estudiante).all()

    def select_by_id(self, db: Session, entity_id: int):
        return db.query(Estudiante).filter(Estudiante._id == entity_id).first()
