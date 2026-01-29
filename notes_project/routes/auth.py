from fastapi import APIRouter, HTTPException, status
from schemas.auth import UserSchema, UserLoginSchema
from typing import Annotated
from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from models.auth import User
from fastapi.responses import JSONResponse
from auth_jwt.auth import hashed_password,verify_user,create_token 
from fastapi.security import OAuth2PasswordRequestForm

auth_router = APIRouter(prefix="/auth")

@auth_router.post("/register")
def register(user:UserSchema,db:Annotated[Session,Depends(get_db)]):
    db_user = db.query(User).filter(User.email==user.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User already exists")
        
    db_user = User(name=user.name,email=user.email,password=hashed_password(user.password))
    db.add(db_user)
    db.commit()
    return JSONResponse({
        "Success":"User Register Successfully"
    })
    

    
@auth_router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email==form_data.username).first()
    if not db_user or not verify_user(form_data.password,db_user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Username or password")
    access_token = create_token({"sub":db_user.email})     
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }