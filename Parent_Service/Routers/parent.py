from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
from Schemas import schemas
from Database import mysql_database_Config
from sqlalchemy.orm import Session 
from Models import models
from Security import security_service_contact

router=APIRouter(tags=["parent"])

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="security_service_user_login")

"""
curr_user_id=await security_service_contact.get_the_user_from_security_service(token)
if curr_user_id["Current_User"]=="Not_Possible":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")"""

@router.post("/create_mentor",status_code=status.HTTP_201_CREATED,response_model=schemas.Parent_Response)
async def create_student(new_parent:schemas.New_Parent,db:Session=Depends(mysql_database_Config.get_db),token:str=Depends(oauth2_scheme)):
    curr_user_id=await security_service_contact.get_the_user_from_security_service(token)
    if curr_user_id["Current_User"]=="Not_Possible":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")
    parent_to_be_added=models.Mentor(** new_parent.dict())
    db.add(parent_to_be_added)
    db.commit()
    db.refresh(parent_to_be_added)
    return parent_to_be_added

@router.get("/get_all_mentors")
async def getting_all_mentors(db:Session=Depends(mysql_database_Config.get_db),token:str=Depends(oauth2_scheme)):
    curr_user_id=await security_service_contact.get_the_user_from_security_service(token)
    if curr_user_id["Current_User"]=="Not_Possible":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")
    data_to_send_back=db.query(models.Mentor).all()
    return data_to_send_back

@router.get("/get_Mentor_by_id/{id}",response_model=schemas.Parent_Response)
async def getting_the_mentor(id:int,db:Session=Depends(mysql_database_Config.get_db),token:str=Depends(oauth2_scheme)):
    curr_user_id=await security_service_contact.get_the_user_from_security_service(token)
    if curr_user_id["Current_User"]=="Not_Possible":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")
    data_to_send_back=db.query(models.Mentor).filter(models.Mentor.parent_id==id).first()
    if data_to_send_back==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Id does not exist")
    return data_to_send_back

@router.delete("/delete_mentor_by_id/{id}",status_code=status.HTTP_200_OK)
async def deleting_mentor(id:int,db:Session=Depends(mysql_database_Config.get_db),token:str=Depends(oauth2_scheme)):
    curr_user_id=await security_service_contact.get_the_user_from_security_service(token)
    if curr_user_id["Current_User"]=="Not_Possible":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")
    x=db.query(models.Mentor).filter(models.Mentor.parent_id==id)
    if x==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Id does not exist")
    x.delete(synchronize_session=False)
    db.commit()
    return {"Message":"Successful"}

@router.put("/update_mentor/{id}",status_code=status.HTTP_200_OK,response_model=schemas.Parent_Response)
async def updating_mentor(id:int,update_mentor:schemas.Update_Parent,db:Session=Depends(mysql_database_Config.get_db),token:str=Depends(oauth2_scheme)):
    curr_user_id=await security_service_contact.get_the_user_from_security_service(token)
    if curr_user_id["Current_User"]=="Not_Possible":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")
    x=db.query(models.Mentor).filter(models.Mentor.parent_id==id)
    if x==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Id does not exist")
    x.update(update_mentor.dict())
    db.commit()
    send_back_to_user=db.query(models.Mentor).filter(models.Mentor.parent_id==id).first()
    return send_back_to_user