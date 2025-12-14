from pydantic import BaseModel
from datetime import date

#Entrada de Dados
class CursoCreate(BaseModel):
    nome: str
    descricao: str | None = None
    carga_horaria: str

#Atualização de Dados
class CursoUpdate(BaseModel):
    nome: str | None = None
    descricao: str | None = None
    carga_horaria: date | None = None

#Leitura de Dados
class CursoRead(BaseModel):
    id:int
    nome: str
    descricao: str
    carga_horaria: str

    class Config:
        from_attributes = True 
