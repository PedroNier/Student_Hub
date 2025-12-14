from pydantic import BaseModel
from datetime import date

#Entrada de Dados
class TarefaCreate(BaseModel):
    id_materia: int
    titulo: str
    data_entrega: date

#Atualização de Dados
class TarefaUpdate(BaseModel):
    id_materia: int | None = None
    titulo: str | None = None
    data_entrega: date | None = None

#Leitura de Dados
class TarefaRead(BaseModel):
    id:int
    id_materia: int
    titulo: str
    data_entrega: date

    class Config:
        from_attributes = True 
