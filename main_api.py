from typing import Optional
from pydantic import BaseModel, EmailStr

app=FastAPI()

class Persona(BaseModel):
    id: Optional[int] = None
    user: str
    mensaje: str

mensajes_db= []

@app.get("/mensajes")    
def get_mensajes():
    return mensajes_db

from fastapi import HTTPException

@app.get("/mensajes/{mensaje_id}")
def get_mensaje(mensaje_id: int):
    for mensaje in mensajes_db:
        if mensaje.id == mensaje_id:
            return mensaje
    raise HTTPException(status_code=404, detail="Mensaje no encontrado")
@app.post("/mensajes")
def crear_mensaje(mensaje: Persona):
    # Si el mensaje no tiene ID, se lo asignamos automáticamente
    mensaje.id = len(mensajes_db) + 1
    mensajes_db.append(mensaje)
    return mensaje