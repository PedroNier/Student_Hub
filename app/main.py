from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
from app.routers import alunos, aula, cursos, entrega_tarefa, materia, matricula, tarefa 
from app.database import engine, SessionLocal, Base
from sqlalchemy.orm import Session

app = FastAPI()

app.include_router(alunos.router)