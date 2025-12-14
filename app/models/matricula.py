from ..database import Base
from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy import ForeignKey

class Matricula(Base):
    __tablename__ = "matricula"

    id = Column(Integer, primary_key=True, index=True)
    id_aluno = Column(ForeignKey("alunos.id"))
    id_curso = Column(ForeignKey("cursos.id"))
    data_matricula = Column(Date, nullable=False)
    status_matricula = Column(Boolean)