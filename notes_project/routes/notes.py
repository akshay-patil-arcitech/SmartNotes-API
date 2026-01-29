from fastapi import APIRouter, Depends, status, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from models.notes import Note
from schemas.notes import NoteSchema
from fastapi.responses import JSONResponse
from auth_jwt.auth import get_current_user


note_router = APIRouter(prefix="/notes")


@note_router.get("/")
def get_all_notes(db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    notes = db.query(Note).filter(
    Note.owner_id == current_user.id
    ).all()

    return {
        "Success": notes
    }
    

@note_router.get("/{id}")
def get_note_by_id(id: int, db: Session = Depends(get_db),current_user=Depends(get_current_user)):
    note = db.query(Note).filter(
    Note.id == id,
    Note.owner_id == current_user.id
    ).first()

    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id {id} not found"
        )
    return {"Success": note}

    
@note_router.post("/add")
def add_note(note:NoteSchema,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    new_note = Note(
        title=note.title,
        content=note.content,
        owner_id=current_user.id
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return {
        "status":status.HTTP_201_CREATED,
        "message":"Note added Successfully"
    }
    
@note_router.put("/update/{id}")
def update_note(id:int,note_data:NoteSchema,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    note = db.query(Note).filter(
    Note.id == id,
    Note.owner_id == current_user.id
    ).first()

    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id {id} not found"
        )
    note.title = note_data.title
    note.content = note_data.content
    
    db.commit()
    
    return {
        "status":status.HTTP_200_OK,
        "message":"Note updated sucessfully"
    }
    
    
@note_router.delete("/delete/{id}")
def delete_note(id:int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    note = db.query(Note).filter(
    Note.id == id,
    Note.owner_id == current_user.id
    ).first()

    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id {id} not found"
        )
    db.delete(note)
    db.commit()
    return {
        "status":status.HTTP_200_OK,
        "message":f"note with id {id} deleted successfully"
    }
    
        
    
    


