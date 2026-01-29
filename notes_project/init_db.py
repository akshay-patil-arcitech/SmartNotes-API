from database import BASE,engine
    
def intitialize_database():
    BASE.metadata.create_all(bind=engine)