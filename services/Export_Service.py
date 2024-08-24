import datetime
from sqlalchemy.orm import Session
from accessData.entities.models import Estudiante, Publicacion

def export_table(db: Session, table_name: str):
    date_str = datetime.datetime.now().strftime("%d-%m-%Y")
    file_name = f'{table_name}-{date_str}.txt'
    
    if table_name == 'estudiante':
        records = db.query(Estudiante).all()
    elif table_name == 'publicacion':
        records = db.query(Publicacion).all()
    else:
        raise ValueError("Tabla no soportada")

    with open(file_name, 'w') as file:
        for record in records:
            file.write(f'{record}\n')

    print(f'Exportacion completada: {file_name}')
