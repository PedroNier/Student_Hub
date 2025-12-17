from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import matricula
from app.schemas.matriculaSchema import MatriculaCreate, MatriculaRead, MatriculaUpdate

router = APIRouter(prefix="/matricula", tags=["matricula"])

@router.post("/matriculas/", response_model=MatriculaCreate)
def create_matricula(matricula: MatriculaCreate, db: Session = Depends(get_db)):
    matricula = matricula(**matricula.dict())
    db.add(matricula)
    db.commit()
    db.refresh(matricula)
    return matricula

@router.get("/matricula/{id}", response_model=MatriculaRead)
def read_matricula(matricula_id: int, db: Session = Depends(get_db)):
    db_matricula = db.query(matricula).filter(matricula.id == matricula_id).first()
    if db_matricula is None:
        raise HTTPException(status_code=404, detail="Matricula não encontrada.")
    return db_matricula

@router.put("/matriculas/{id}", response_model=MatriculaUpdate)
def update_matricula(matricula_id: int, db: Session = Depends(get_db)):
    db_matricula = db.query(matricula).filter(matricula.id == matricula_id).first()
    if db_matricula is None:
        raise HTTPException(status_code=404, detail="Matricula não encontrada.")
    for key, value in db_matricula:
        setattr(db_matricula, key, value)
    db.commit()
    db.refresh(db_matricula)
    return db_matricula

@router.delete("/matriculas/{id}")
def update_matricula(matricula_id: int, db: Session = Depends(get_db)):
    db_matricula = db.query(matricula).filter(matricula.id == matricula_id).first()
    if db_matricula is None:
        raise HTTPException(status_code=404, detail="Matricula não encontrada.")
    db.delete(db_matricula)
    return {"Mensagem": "Matricula deletada com sucesso."}