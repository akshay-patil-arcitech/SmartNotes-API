from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.prj_config import setting

BASE = declarative_base()

DATABASE_URL = f"postgresql://{setting.DB_USER}:{setting.DB_PASSWORD}@{setting.HOST}:5432/{setting.DB_NAME}"
engine = create_engine(DATABASE_URL)
session = sessionmaker(autoflush=False,autocommit=False,bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
        