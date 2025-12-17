from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.Aluno import Aluno
from app.schemas.alunosSchema import AlunoCreate, AlunoRead, AlunoUpdate

router = APIRouter(prefix="/alunos", tags=["alunos"])


#Cria uma entrada de aluno
@router.post("/alunos/", response_model=AlunoCreate)
def create_aluno(aluno: AlunoCreate, db: Session = Depends(get_db)):
    aluno = Aluno(**Aluno.dict())
    db.add(aluno)
    db.commit()
    db.refresh(aluno)
    return aluno

#Retorna todos os alunos cadastrados
@router.get("/alunos/", response_model=list[AlunoRead])
def read_aluno(skip: int = 0, db: Session = Depends(get_db)):
    return db.query(Aluno).all()

#Retorna um aluno específico
@router.get("/alunos/{id}", response_model=AlunoRead)
def read_aluno_by_id(aluno_id: int, db: Session = Depends(get_db)):
    db_aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    if db_aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    return db_aluno

#Atualiza os dados de um aluno
@router.put("alunos/{id}", response_model=AlunoUpdate)
def update_aluno(aluno_id: int, db: Session = Depends(get_db)):
    db_aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    if db_aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    for key, value in db_aluno.dict().items():
        setattr(db_aluno, key, value)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno

#Deleta os dados de um aluno.
@router.delete("alunos/{id}")
def delete_aluno(aluno_id: int, db: Session = Depends(get_db)):
    db_aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    if db_aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    db.delete(db_aluno)
    db.commit()
    return{"Mensagem": "Aluno deletado da base de dados."}