from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from models import models
from schemas import schemas
import crud

from config.db import engine, SessionLocal

from typing import List, ClassVar

models.Base.metadata.create_all(engine)


user = APIRouter()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@user.get("/users", response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    usuarios = crud.get_users(db, skip=skip, limit=limit)
    return usuarios


@user.get(
    "/users/{id}", response_model=schemas.User_response, response_description="sucess"
)
def get_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="usuario no encontrado")
    return schemas.User_response(
        message="ok",
        id=db_user.id,
        name=db_user.name,
        email=db_user.email,
        password=db_user.password,
    )


@user.post("/users")
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    db_user = crud.create_user(db=db, user=user)
    return f"el usuario {db_user.name} ha sido creado"


@user.delete("/users/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(user_id=id, db=db)
    return f"El usuario {db_user.name} con el id {db_user.id} ha sido eliminado"


@user.put("/users/{id}/")
def rename_user(id: int, new_name: str, db: Session = Depends(get_db)):
    db_user = crud.modify_name(user_id=id, name=new_name, db=db)
    return f"el nombre del usuario ha sido cambiado a {db_user.name}"

@user.put("/users/{id}")
def modify_pasword(id: int, new_password: str, db: Session=Depends(get_db)):
    db_user = crud.modify_password(user_id=id, password=new_password, db=db)
    return f"la contraseña del usuario ha sido cambiada a {db_user.password}"