from ..database import Base
from sqlalchemy import Column, Integer, ForeignKey, String, Date

class Aula(Base):
    __tablename__ = "aula"
    
    id = Column(Integer, primary_key=True, index=True)
    id_materia = Column(ForeignKey("materia.id"))
    titulo = Column(String)
    Data = Column(Date, nullable=False)