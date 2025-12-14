from pydantic import BaseModel
from datetime import date

#Entrada de Dados
class AlunoCreate(BaseModel):
    nome: str
    email: str
    dob: date

#Atualização de Dados
class AlunoUpdate(BaseModel):
    nome: str | None = None
    email: str | None = None
    dob: date | None = None

#Leitura de Dados
class AlunoRead(BaseModel):
    id:int
    nome: str
    email: str
    dob: date

    class Config:
        from_attributes = True 

    