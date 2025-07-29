from sqlalchemy.orm import Session
from .. import models, database, schemas
from fastapi import Depends, HTTPException, status, Response

get_db = database.get_db

def get_all(db: Session ):
    #getting all blogs with get request
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, db: Session):
    #creating a blog with post request
    new_blog = models.Blog(title=request.title, body=request.body, user_id = 1) 
    db.add(new_blog)
    db.commit()     
    db.refresh(new_blog)
    return new_blog
  

def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} not found"
        )
    db.delete(blog)
    db.commit()
    return {"message": "Blog deleted successfully"}


def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not db.query(models.Blog).filter(models.Blog.id == id).first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} not found" )
    blog.update(request)   
    db.commit()
    return {"message": "Blog updated successfully"}



def show(id: int, response: Response , db: Session):
    #getting a blog by id with get request
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} not found"
        )
    return blog

