from datetime import datetime,timedelta
from fastapi import Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt,JWTError
from Configuration.config import settings
from Database import mongo_database_Config as mongodb


SECRET_KEY=settings.SECRET_KEY
ALGORITHM=settings.ALGORITHM
Access_token_expire_time=settings.Access_token_expire_time
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="user_login")

def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=Access_token_expire_time)
    to_encode.update({"exp":expire})
    encoded_jwt_token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt_token

def verify_access_token(token:str,credentials_exception):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        extracted_id:str=payload.get("user_id")
        if extracted_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return extracted_id

def get_current_user(token:str=Depends(oauth2_scheme)):
    credentials_exception=HTTPException(status_code=status.HTTP_400_BAD_REQUEST
                                        ,detail="Incorrect Credentials"
                                        ,headers={"WWW_Authenticate":"Bearer"})
    token_user_id=verify_access_token(token,credentials_exception)
    x=mongodb.user_login_var.find_one({"user_id":token_user_id})
    if x==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Credentials")
    return x["user_id"]