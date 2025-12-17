from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import aula
from app.schemas.aulaSchema import AulaCreate, AulaRead, AulaUpdate

router = APIRouter(prefix="/aula", tags=["aula"])

@router.post("/aula/", response_model=AulaCreate)
def create_aula(aula: AulaCreate, db: Session = Depends(get_db)):
    aula = aula(**aula.dict())
    db.add(aula)
    db.commit()
    db.refresh(aula)
    return aula

@router.get("/aula/", response_model=list[AulaRead])
def read_aula(skip: int = 0, db: Session = Depends(get_db)):
    db_aulas = db.query(aula).all()
    return db_aulas

@router.get("aula/{id}", response_model=list[AulaRead])
def read_aula_by_id(aula_id: int, db: Session = Depends(get_db)):
    db_aula = db.query(aula).filter(aula.id == aula_id).first()
    if db_aula is None:
        raise HTTPException(status_code=404, detail="Aula não encontrada.")
    return db_aula

@router.put("aula/{id}", response_model=AulaUpdate)
def update_aula(aula_id: int, db: Session = Depends(get_db)):
    db_aula = db.query(aula).filter(aula.id == aula_id).first()
    if db_aula is None:
        raise HTTPException(status_code=404, detail="Aula não encontrada.")
    for key, value in db_aula:
        setattr(db_aula, key, value)
    db.commit()
    db.refresh(db_aula)
    return db_aula

@router.delete("aulas/{id}")
def delete_aula(aula_id: int, db: Session = Depends(get_db)):
    db_aula = db.query(aula).filter(aula.id == aula_id).first()
    if db_aula is None:
        raise HTTPException(status_code=404, detail="Aula não encontrada.")
    db.delete(db_aula)
    return {"Mensagem":"Aula deletada com sucesso."}