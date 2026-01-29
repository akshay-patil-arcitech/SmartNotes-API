from fastapi import FastAPI
from routes.auth import auth_router
from routes.notes import note_router
from routes.ai import ai_router
from init_db import intitialize_database

intitialize_database()

app = FastAPI()

app.include_router(auth_router, prefix="/api", tags=["authentication"])
app.include_router(note_router, prefix="/api", tags=["notes"])
app.include_router(ai_router,prefix="/api",tags=["AI"])

@app.get("/")
def sample():
    return {"msg": "done"}
