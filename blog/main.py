from fastapi import FastAPI
import uvicorn
from . import  database
from .database import engine
from . import models
from .hashing import Hash
from .routers import blog, users, authentication




app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(users.router)


   
if __name__ == "__main__":
    uvicorn.run(app, host="172.16.4.129",port=8001)
