from pydantic import BaseModel
from datetime import date

#Entrada de Dados
class EntregaTarefaCreate(BaseModel):
    id_tarefa: int
    id_aluno: int
    arquivo: str
    nota: int
    data_envio: date
    status: bool

#Atualização de Dados
class EntregaTarefaUpdate(BaseModel):
    id_tarefa: int | None = None
    id_aluno: int | None = None
    arquivo: str | None = None
    nota: int | None = None
    data_envio: date | None = None
    status: bool | None = None

#Leitura de Dados
class EntregaTarefaRead(BaseModel):
    id:int
    id_tarefa: int
    id_aluno: int
    arquivo: str
    nota: int
    data_envio: date
    status: bool

    class Config:
        from_attributes = True 
