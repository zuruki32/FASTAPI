from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str
    
    
class showBlog(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True  # This allows Pydantic to read data as dictionaries from SQLAlchemy models
