from ..database import Base
from sqlalchemy import Column, Integer, String, Boolean, Date

class Cursos(Base):
    __tablename__="cursos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(String)
    carga_horaria = Column(String, nullable=False)