from fastapi import FastAPI, Depends, status , Response, HTTPException
import uvicorn
from . import schemas, database
from .database import Base, engine, SessionLocal
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import models
models.Base.metadata.create_all(bind=database.engine)


app = FastAPI()
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    #creating a blog with post request
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()     
    db.refresh(new_blog)
    return new_blog
  
  
@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} not found"
        )
    db.delete(blog)
    db.commit()
    return {"message": "Blog deleted successfully"}

@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not db.query(models.Blog).filter(models.Blog.id == id).first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} not found" )
    blog.update(request)   
    db.commit()
    return {"message": "Blog updated successfully"}


@app.get("/blog")
def get_all(db: Session = Depends(get_db)):
    #getting all blogs with get request
    blogs = db.query(models.Blog).all()
    return blogs

@app.get("/blog/{id}", status_code=200, response_model=schemas.showBlog)
def get_blog(id: int, response: Response , db: Session = Depends(get_db)):
    #getting a blog by id with get request
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} not found"
        )
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"Blog with the {id} not found"}
    return blog

if __name__ == "__main__":
    uvicorn.run(app, host="172.16.4.129",port=8000)
