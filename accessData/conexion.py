from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from accessData.entities.models import BaseDeDatos

DATABASE_URL = 'mysql+pymysql://root:admin@localhost:3307/instituto'

engine = create_engine(DATABASE_URL)
BaseDeDatos.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
