from typing import List
from fastapi import APIRouter, Depends,status, HTTPException, Response
from .. import schemas,database, models, hashing
from ..hashing import Hash
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix= "/user",
    tags= ["users"]
)
get_db = database.get_db

@router.post("/", response_model= schemas.showUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request,db)
            
@router.get("/{id}", response_model=schemas.showUser)
def get_user(id: int, db: Session = Depends(get_db)):         
    return user.get_user(id,db)   