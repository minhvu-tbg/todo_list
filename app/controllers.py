from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()


def get_todo_by_id(db: Session, pk: int):
    return db.query(models.Todo).filter(models.Todo.id == pk).first()


def create_todo(db: Session, item: schemas.TodoCreate):
    db_item = models.Todo(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_todo(db: Session, db_item: models.Todo, item: schemas.TodoUpdate):
    for key, value in item:
        if hasattr(db_item, key):
            setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item
