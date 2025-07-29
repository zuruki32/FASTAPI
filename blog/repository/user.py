from sqlalchemy.orm import Session
from .. import models, database, schemas,hashing
from ..hashing import Hash
from fastapi import Depends, HTTPException, status, Response


def create_user(request: schemas.User, db: Session):
    new_user = models.User(username = request.username, email = request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit() 
    db.refresh(new_user)
    return new_user

def get_user(id: int, db: Session ):  
    user = db.query(models.User).filter(models.User.id == id).first() 
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"user with this id {id} not found")         
    return user     