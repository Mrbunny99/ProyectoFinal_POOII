from services.BaseDatosServices import BaseDatosServices

class GenericService(BaseDatosServices):
    def __init__(self, db, model):
        self.db = db
        self.model = model

    def create(self, obj):
        session = self.db.get_session()
        session.add(obj)
        session.commit()
        session.close

    def update(self, obj):
        session = self.db.get_session()
        db_obj = session.query(self.model).filter(self.model.id == obj.id).first()
        if db_obj:
            for attr, value in vars(obj).items():
                setattr(db_obj,attr,value)
            session.commit()
        session.close()

    def delete(self, obj_id: int):
        session = self.db.get_session()
        db_obj = session.query(self.model).filter(self.model.id == obj_id).first()
        if db_obj:
            session.delete(db_obj)
            session.commit()
        session.close()

    def select_all(self):
        session = self.db.get_session()
        objs = session.query(self.model).all()
        session.close()
        return objs
    
    def select_by_id(self, obj_id: int):
        session = self.db.get_session()
        obj = session.query(self.model).filter(self.model.id == obj_id).first()
        session.close()
        return obj