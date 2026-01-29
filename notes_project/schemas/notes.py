from pydantic import BaseModel, Field
from typing import Annotated

class NoteSchema(BaseModel):
    title : Annotated[str,Field(description="Title of the note")]
    content : Annotated[str,Field(description="Content of the note")]