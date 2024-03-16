from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
import httpx
from sqlalchemy import func
from Schemas import schemas
from Database import mysql_database_Config
from sqlalchemy.orm import Session 
from Models import models
from Security import security_service_contact

router=APIRouter(tags=["Student Course"])

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="security_service_user_login")

"""
curr_user_id=await security_service_contact.get_the_user_from_security_service(token)
if curr_user_id["Current_User"]=="Not_Possible":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")"""

@router.post("/student_course",response_model=schemas.Student_Course_response)
async def student_course(new_student_course:schemas.Student_Course,db:Session=Depends(mysql_database_Config.get_db),token:str=Depends(oauth2_scheme)):
    curr_user_id=await security_service_contact.get_the_user_from_security_service(token)
    if curr_user_id["Current_User"]=="Not_Possible":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")
    student_course_to_be_added=models.Student_Course(** new_student_course.dict())
    db.add(student_course_to_be_added)
    db.commit()
    db.refresh(student_course_to_be_added)
    return student_course_to_be_added

@router.get("/student_with_course")
async def student_with_their_course(db:Session=Depends(mysql_database_Config.get_db),token:str=Depends(oauth2_scheme)):
    curr_user_id=await security_service_contact.get_the_user_from_security_service(token)
    if curr_user_id["Current_User"]=="Not_Possible":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")
    client=httpx.AsyncClient()
    token_sending_string=f"Bearer {token}=="
    header={"Authorization":token_sending_string}
    student_response = await client.get("http://localhost:8002/get_all_students",headers=header)
    course_response = await client.get("http://localhost:8004/get_all_courses",headers=header)
    students=student_response.json()
    courses = course_response.json()
    student_course_link=db.query(models.Student_Course).all()
    student_course_link_list=[]
    for i in student_course_link:
        student_course_link_dict={}
        student_course_link_dict.update({"student_id":i.student_id,"course_id":i.course_id})
        student_course_link_list.append(student_course_link_dict)
    ddict={}
    dlist=[]
    for i in student_course_link_list:
        for j in students:
            ddict={}
            if j["student_id"]==i["student_id"]:
                ddict.update({"student_id":j["student_id"],"first_name":j["first_name"],"last_name":j["last_name"],"parent_id":j["parent_id"]})
                for k in courses:
                    if i["course_id"]==k["course_id"]:
                        ddict.update(k)
                dlist.append(ddict)
                break
    return dlist

@router.get("/course_student_count")
async def course_student_count(db:Session=Depends(mysql_database_Config.get_db),token:str=Depends(oauth2_scheme)):
    curr_user_id=await security_service_contact.get_the_user_from_security_service(token)
    if curr_user_id["Current_User"]=="Not_Possible":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")
    client=httpx.AsyncClient()
    token_sending_string=f"Bearer {token}=="
    header={"Authorization":token_sending_string}
    result=db.query(models.Student_Course.course_id,func.count(models.Student_Course.student_id)).group_by(models.Student_Course.course_id).all()
    course_response = await client.get("http://localhost:8004/get_all_courses",headers=header)
    courses=course_response.json()
    flist=[]
    for i in result:
        fdict={}
        for j in courses:
            if i[0]==j["course_id"]:
                fdict.update({"course_id":j["course_id"],"course_name":j["course_name"],"course_desc":j["course_desc"]})
                fdict.update({"student_count":i[1]})
                flist.append(fdict)
    return flist

@router.get("/course_with_material")
async def course_whth_coursematerial(status_code=status.HTTP_200_OK,db:Session=Depends(mysql_database_Config.get_db),token:str=Depends(oauth2_scheme)):
    curr_user_id=await security_service_contact.get_the_user_from_security_service(token)
    if curr_user_id["Current_User"]=="Not_Possible":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")
    client=httpx.AsyncClient()
    token_sending_string=f"Bearer {token}=="
    header={"Authorization":token_sending_string}
    course_response = await client.get("http://localhost:8004/get_all_courses",headers=header)
    course_material_response = await client.get("http://localhost:8005/get_all_course_materials",headers=header)
    courses=course_response.json()
    course_material=course_material_response.json()
    flist=[]
    for i in courses:
        fdict={}
        fdict.update(i)
        for j in course_material:
            if i["course_id"]==j["course_id"]:
                fdict.update({"link":j["course_material_url"]})
            flist.append(fdict)
    return flist


