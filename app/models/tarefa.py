from ..database import Base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import ForeignKey

class Tarefa(Base):
    __tablename__ = "tarefa"

    id = Column(Integer, primary_key=True, index=True)
    id_materia = Column(ForeignKey("materia.id"))
    titulo = Column(String)
    data_entrega = Column(Date, nullable=False)
