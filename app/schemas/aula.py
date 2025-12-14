from pydantic import BaseModel
from datetime import date

#Entrada de Dados
class AulaCreate(BaseModel):
    id_materia: int
    titulo: str | None = None
    data: date

#Atualização de Dados
class AulaUpdate(BaseModel):
    id_materia: int | None = None
    titulo: str | None = None
    data: date | None = None

#Leitura de Dados
class AulaRead(BaseModel):
    id:int
    id_materia: int
    titulo: str
    data: date

    class Config:
        from_attributes = True 
