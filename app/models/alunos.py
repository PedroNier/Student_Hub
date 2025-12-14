from ..database import Base
from sqlalchemy import Column, Integer, String, Boolean, Date

class Aluno(Base):
    __tablename__= "alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    dob = Column(Date)
