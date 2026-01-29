from passlib.context import CryptContext
from jose import jwt,JWTError
from datetime import datetime,timedelta
from config.prj_config import setting 
from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from database import get_db
from sqlalchemy.orm import Session
from models.auth import User

pwd_context = CryptContext(schemes=["bcrypt"])

def hashed_password(password:str):
    return pwd_context.hash(password)

def verify_user(plain:str,hashed:str):
    return pwd_context.verify(plain,hashed)

def create_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,setting.SECRET_KEY,algorithm=setting.ALGORITHM)


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

# def get_current_user(token:str = Depends(oauth2_scheme)):
#     try:
#         payload = jwt.decode(token,setting.SECRET_KEY,algorithms=[setting.ALGORITHM])
#         return payload["sub"]
#     except:
#         raise HTTPException(status_code=401,detail="Invalid token")

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/auth/login"
)



def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            setting.SECRET_KEY,
            algorithms=[setting.ALGORITHM]
        )
        email: str | None = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception

    return user
