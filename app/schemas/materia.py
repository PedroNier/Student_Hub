from pydantic import BaseModel
from datetime import date

#Entrada de Dados
class MateriaCreate(BaseModel):
    id_curso: int
    nome: str
    descricao: str
    professor: str

#Atualização de Dados
class MateriaUpdate(BaseModel):
    id_curso: int | None = None
    nome: str | None = None
    descricao: str | None = None
    professor: str | None = None

#Leitura de Dados
class MateriaRead(BaseModel):
    id:int
    id_curso: int
    nome: str
    descricao: str
    professor: str

    class Config:
        from_attributes = True 
