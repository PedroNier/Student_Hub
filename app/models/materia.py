from ..database import Base
from sqlalchemy import Column, Integer, ForeignKey, String

class Materia(Base):
    __tablename__ = "materia"

    id = Column(Integer, primary_key=True, index=True)
    id_curso = Column(ForeignKey("cursos.id"))
    nome = Column(String, nullable=False)
    descricao = Column(String)
    professor = Column(String, nullable=False)
