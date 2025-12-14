from pydantic import BaseModel
from datetime import date

#Entrada de Dados
class MatriculaCreate(BaseModel):
    id_aluno: int
    id_curso: int
    data_matricula: date
    status_matricula: bool

#Atualização de Dados
class MatriculaUpdate(BaseModel):
    id_aluno: int | None = None
    id_curso: int | None = None
    data_matricula: date | None = None
    status_matricula: bool | None = None

#Leitura de Dados
class MatriculaRead(BaseModel):
    id: int
    id_aluno: int
    id_curso: int
    data_matricula: date
    status_matricula: bool

    class Config:
        from_attributes = True 

    