#python
from uuid import UUID
from datetime import date
from typing import Optional
#PYdantyc
from pydantic import BaseModel, EmailStr, Field
#FastAPI
from fastapi import FastAPI

app = FastAPI()

#MOdel USEBASE
class UserBase (BaseModel):
    user_id: UUID = Field
    (...)
    email: EmailStr = Field
    (...)
#Model userlogin
class UserLogin (UserBase):
    contrasena: str = Field(..., min_length=8)
#Model user
class Usuario(UserBase):
    nombre: str =  Field(
        ...,
        min_length = 1,
        max_length=20
        )
    apellido: str =  Field(
        ...,
        min_length = 1,
        max_length=20
        )
    cumple: Optional[date] = Field(default=None)

#Model Mensajes
class Mensaje():
    pass

@app.get(path="/")
def home():
    return {"Mensajes": "Sirve"}