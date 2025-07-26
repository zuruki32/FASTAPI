from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
app = FastAPI()
#here i wrote the path(the basic url)

@app.get("/")
def index():
    return {'data':{'blog list'}}
    
@app.get("/about")
def about():
    return {'data':{'about page'}}

@app.get("/blog")
def inside(limit = 10,published = True, sort: Optional[str] = None):
    
    if published == 'true':
        return {'data': f' {limit} published blog from list'}
    else:
         return {'data':f' {limit} didnt published blog from list'}

    
    
@app.get("/blog/{id}")
def show(id: int):
    #fetch blog with id = id
    return {'data': id}
    
@app.get("/blog/{id}/comments")
def comments(id: int):
    return {'data': {'comments for blog id': id}}

@app.get("/blog?limit={limit}&published=true")
def index():
    return {'data': 'blog with limit and published status'}



class Blog(BaseModel):
  title: str
  body: str
  published: Optional[bool]

@app.post("/blog")
def create(request: Blog):
    return {'data': f'blog is created with title {request.title}'}


if __name__ == "__main__":
    uvicorn.run(app, host="172.16.4.129",port=8000)
