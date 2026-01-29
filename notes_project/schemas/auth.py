from pydantic import BaseModel, Field
from typing import Annotated

class UserSchema(BaseModel):
    name : Annotated[str,Field(...,description="Name of the user")]
    email : Annotated[str,Field(..., description="Email of the user")]
    password : Annotated[str,Field(...,description="Password")]
    
class UserLoginSchema(BaseModel):
    email : Annotated[str,Field(..., description="Email of the user")]
    password : Annotated[str,Field(...,description="Password")]  