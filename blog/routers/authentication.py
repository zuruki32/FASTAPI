from fastapi import APIRouter, Depends,status, HTTPException
from .. import schemas,database, models,token
from fastapi.security import OAuth2PasswordRequestForm 
from ..hashing import Hash
from sqlalchemy.orm import Session
from ..token import create_access_token

get_db = database.get_db
router = APIRouter(
    
    tags=["authentication"]
)

@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid credentials"
        )
        
    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="incorrect pass"
        )
    #if everything is fine then we should generate jwt token
    access_token = create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
