#python
from uuid import UUID
from datetime import date, datetime
from typing import Optional, List
#PYdantyc
from pydantic import BaseModel, EmailStr, Field
#FastAPI
from fastapi import FastAPI, status

app = FastAPI()

#MOdel USEBASE
class UserBase (BaseModel):
    user_id: UUID = Field
    (...)
    email: EmailStr = Field
    (...)
#Model userlogin
class UserLogin (UserBase):
    contrasena: str = Field(..., min_length=8,max_length=20)
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
    mensaje_id: UUID = Field(...)
    contenido: str =  Field(
        ...,
        min_length = 1,
        max_length=300
        )
    fechaCreacion: datetime = Field(default=datetime.now())
    fechaModificado:Optional[datetime] = Field(default=None)
    credoPor: Usuario = Field(...)

@app.get(path="/")
def home():
    return {"Mensajes": "Sirve"}

#path operation user
@app.post(
    path="/registro",
    response_model= Usuario,
    status_code= status.HTTP_201_CREATED,
    summary="Registrar usuario",
    tags=["usuarios"]
    )
def registro():
    pass

@app.post(
    path="/login",
    response_model= Usuario,
    status_code= status.HTTP_200_OK,
    summary="Login usuario",
    tags=["usuarios"]
    )
def login():
    pass

@app.get(
    path="/usuarios",
    response_model= List[Usuario],
    status_code= status.HTTP_200_OK,
    summary="Ver todos los usuario",
    tags=["usuarios"]
    )
def usuarios():
    pass


@app.get(
    path="/usuario/{user_id}",
    response_model= Usuario,
    status_code= status.HTTP_200_OK,
    summary="Ver un usuario",
    tags=["usuarios"]
    )
def usuarioID():
    pass

@app.delete(
    path="/usuario/{user_id}/delete",
    response_model= Usuario,
    status_code= status.HTTP_200_OK,
    summary="Eliminar un usuario",
    tags=["usuarios"]
    )
def DeleteusuarioID():
    pass

@app.put(
    path="/usuario/{user_id}/update",
    response_model= Usuario,
    status_code= status.HTTP_200_OK,
    summary="Eliminar un usuario",
    tags=["usuarios"]
    )
def updateUsuarioID():
    pass