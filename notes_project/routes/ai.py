from fastapi import APIRouter, Depends, HTTPException
from chat_service import AIService
from typing import Annotated
from sqlalchemy.orm import Session
from database import get_db
from auth_jwt.auth import get_current_user
from models.notes import Note

ai_router = APIRouter(prefix="/ai")

@ai_router.get("/notes/{note_id}/summarize")
def summerize_note(note_id:int,db:Annotated[Session,Depends(get_db)],current_user:Session = Depends(get_current_user)):
    note = db.query(Note).filter(Note.id==note_id,Note.owner_id==current_user.id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    ai = AIService()
    summary = ai.summarize(note.content)
    return {
        "summary": summary
    }

@ai_router.get("/notes/{id}/suggest-title")
def suggest_title(id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    note = db.query(Note).filter(Note.id == id, Note.owner_id == current_user.id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    ai = AIService()
    title = ai.generate_title(note.content)
    return {"title": title}
