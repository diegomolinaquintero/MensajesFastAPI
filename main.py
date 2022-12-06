#python
from uuid import UUID
from datetime import date, datetime
from typing import Optional, List
import json
#PYdantyc
from pydantic import BaseModel, EmailStr, Field
#FastAPI
from fastapi import FastAPI, status, Body

app = FastAPI()

#MOdel USEBASE
class UserBase (BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)
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
    
#Model userRegister
class UserRegister (Usuario):
    contrasena: str = Field(..., min_length=8,max_length=20)

#Model Mensajes
class Mensaje(BaseModel):
    mensaje_id: UUID = Field(...)
    contenido: str =  Field(
        ...,
        min_length = 1,
        max_length=300
        )
    fechaCreacion: datetime = Field(default=datetime.now())
    fechaModificado:Optional[datetime] = Field(default=None)
    credoPor: Usuario = Field(...)


#path operation user
@app.post(
    path="/registro",
    response_model= Usuario,
    status_code= status.HTTP_201_CREATED,
    summary="Registrar usuario",
    tags=["usuarios"]
    )
def registro(user: UserRegister = Body(...)):
    """
    Registrar usuario
    
    Esta ruta crea un usuario en la app
    Parametros:
        -Request body 
            -User: UsuarioRegistro
    Retorna los json con la info del usuario
        -UserID: UUID
        -Emal: str
        -Nombre
        -apellido
        -cumple 
    """
    with open("users.json","r+", encoding="utf-8") as f:
        resultado = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["cumple"] = str(user_dict["cumple"])
        resultado.append(user_dict)
        f.seek(0)
        f.write(json.dumps(resultado))
        return user
    
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
    """_Ver todos los usuarios_

    Returns:
        json con todos los usduarios sin las password
        - UserID: UUID
        - Emal: str
        - Nombre
        - apellido
        - cumple 
    """
    with open("users.json","r", encoding="utf-8") as f:
        resultado = json.loads(f.read())
        
        return resultado


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

#path operation mensajes


@app.get(
    path="/",
    response_model= List[Mensaje],
    status_code= status.HTTP_200_OK,
    summary="Ver todos los mensajes",
    tags=["mensajes"]
    )
def home():
    pass

@app.post(
    path="/enviarmensaje",
    response_model= Mensaje,
    status_code= status.HTTP_201_CREATED,
    summary="Enviar mensajes",
    tags=["mensajes"]
    )
def enviarmensaje():
    pass

@app.get(
    path="/mensaje/{mensaje_id}",
    response_model= Mensaje,
    status_code= status.HTTP_200_OK,
    summary="Ver un mensajes",
    tags=["mensajes"]
    )
def verUnMensaje():
    pass

@app.delete(
    path="/mensaje/{mensaje_id}/delete",
    response_model= Mensaje,
    status_code= status.HTTP_200_OK,
    summary="Eliminar un mensajes",
    tags=["mensajes"]
    )
def DeleteMEnsaje():
    pass

@app.put(
    path="/mensaje/{mensaje_id}/update",
    response_model= Mensaje,
    status_code= status.HTTP_200_OK,
    summary="update un mensajes",
    tags=["mensajes"]
    )
def update():
    pass