from pydantic import BaseModel
from typing import List, Optional

class Blog(BaseModel):
    title: str
    body: str
    class Config:
        orm_mode = True 

    
class User(BaseModel):
    username: str
    email: str
    password: str
    
    
class showUser(BaseModel):
    username: str
    email: str
    blogs : list[Blog] =[]
    class Config:
        orm_mode = True  


class showBlog(BaseModel):
    title: str
    body: str
    creator: showUser 
    class Config:
        orm_mode = True  # This allows Pydantic to read data as dictionaries from SQLAlchemy models


class Login(BaseModel):
    username: str
    password: str
    
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
    
class TokenData(BaseModel):
    email: Optional[str] 
