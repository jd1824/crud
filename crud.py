from sqlalchemy.orm import Session
from models import models
from schemas import schemas
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key=key)



def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.User):
    db_user = models.User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db:Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return db_user

def modify_name(db: Session, user_id: int, name: str):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db_user.name = name
    db.commit()
    db.refresh(db_user)
    return db_user

def modify_password(db: Session, user_id: int, password: str):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db_user.password = password
    db.commit()
    db.refresh(db_user)
    return db_user