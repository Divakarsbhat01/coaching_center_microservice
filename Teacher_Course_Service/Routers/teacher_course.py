from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
import httpx
from Schemas import schemas
from Database import mysql_database_Config
from sqlalchemy.orm import Session 
from Models import models
from Security import security_service_contact
from sqlalchemy import func

router=APIRouter(tags=["Teacher_Course"])

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="security_service_user_login")

"""
curr_user_id=await security_service_contact.get_the_user_from_security_service(token)
if curr_user_id["Current_User"]=="Not_Possible":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")"""

@router.post("/teacher_course",response_model=schemas.Teacher_Course_response)
async def student_course(new_teacher_course:schemas.Teacher_Course,db:Session=Depends(mysql_database_Config.get_db),token:str=Depends(oauth2_scheme)):
    curr_user_id=await security_service_contact.get_the_user_from_security_service(token)
    if curr_user_id["Current_User"]=="Not_Possible":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")
    teacher_course_to_be_added=models.Teacher_Course(** new_teacher_course.dict())
    db.add(teacher_course_to_be_added)
    db.commit()
    db.refresh(teacher_course_to_be_added)
    return teacher_course_to_be_added

@router.get("/course_teacher_count")
async def course_teacher_count(db:Session=Depends(mysql_database_Config.get_db),token:str=Depends(oauth2_scheme)):
    curr_user_id=await security_service_contact.get_the_user_from_security_service(token)
    if curr_user_id["Current_User"]=="Not_Possible":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")
    client=httpx.AsyncClient()
    token_sending_string=f"Bearer {token}=="
    header={"Authorization":token_sending_string}
    result=db.query(models.Teacher_Course.course_id,func.count(models.Teacher_Course.teacher_id)).group_by(models.Teacher_Course.course_id).all()
    course_response = await client.get("http://localhost:8004/get_all_courses",headers=header)
    courses=course_response.json()
    flist=[]
    for i in result:
        fdict={}
        for j in courses:
            if i[0]==j["course_id"]:
                fdict.update({"course_id":j["course_id"],"course_name":j["course_name"],"course_desc":j["course_desc"]})
                fdict.update({"teacher_count":i[1]})
                flist.append(fdict)
    return flist

