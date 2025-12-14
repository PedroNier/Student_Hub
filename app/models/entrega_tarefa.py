from ..database import Base
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy import ForeignKey

class Entrega_Tarefa(Base):
    __tablename__ = "entrega_tarefa"

    id = Column(Integer, primary_key=True, index=True)
    id_tarefa = Column(ForeignKey("tarefa.id"))
    id_aluno = Column(ForeignKey("alunos.id"))
    arquivo = Column(String)
    nota = Column(Integer)
    data_envio = Column(Date)
    status_envio = Column(Boolean)