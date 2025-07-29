from typing import List
from fastapi import APIRouter, Depends,status, HTTPException, Response
from .. import schemas,database, models
from sqlalchemy.orm import Session
from ..repository import blog
from .. import oaut2


router = APIRouter(
    prefix= "/blog",
    tags= ["blogs"]
)

get_db = database.get_db



@router.get("/")
def get_all(db: Session = Depends(get_db),current_user: schemas.User = Depends(oaut2.get_current_user)):
    #getting all blogs with get request
    return blog.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db),current_user:schemas.User = Depends(oaut2.get_current_user)):
    return  blog.create(request,db)
  
  
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db),current_user:schemas.User = Depends(oaut2.get_current_user)):
    return blog.destroy(id,db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db),current_user:schemas.User = Depends(oaut2.get_current_user)):
    return blog.update(id,request,db)


@router.get("/{id}", status_code=200, response_model=schemas.showBlog)
def show(id: int, response: Response , db: Session = Depends(get_db),current_user:schemas.User = Depends(oaut2.get_current_user)):
    return blog.show(id, response, db)


