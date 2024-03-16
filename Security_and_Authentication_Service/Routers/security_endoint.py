from fastapi import APIRouter
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from Schemas import schemas
from Database import mongo_database_Config as mongodb
from fastapi import HTTPException,status
from Security_and_Auth import authentication,pass_hash


router=APIRouter(tags=["Security Endpoint"])

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

@router.post("/user_login",status_code=status.HTTP_202_ACCEPTED,response_model=schemas.User_Login_Response)
def user_login(user_cred:OAuth2PasswordRequestForm=Depends()):
    x=mongodb.user_login_var.find_one({"user_name":user_cred.username})
    if x==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid user credentials")
    db_user_id=x["user_id"]
    db_user_password=x["user_password"]
    if pass_hash.verify_the_password(user_cred.password,db_user_password)==False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid user credentials of password")
    access_token=authentication.create_access_token(data={"user_id":db_user_id})
    return {"access_token":access_token,"type":"Bearer"}

@router.post("/verify_logged_in_user")
def loggedin_user_verification(token_dict:schemas.Token_Receive):
    try:
        token=token_dict.access_token
        curr=authentication.get_current_user(token)
        return {"Current_User":curr}
    except Exception as e:
        return {"Current_User":"Not_Possible"}