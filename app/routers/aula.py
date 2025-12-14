from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Aula

router = APIRouter(prefix="/alunos", tags=["Alunos"])

@router.post("/")
def criar_aula(
    id: int,
    nome:str,
    email: str,
    dob: str,
    db: Session = Depends(get_db)):
        aluno = Aula(id=id, nome=nome,email=email,dob=dob)
        db.add(aluno)
        db.commit()
        db.refresh(aluno)
        
        return aluno