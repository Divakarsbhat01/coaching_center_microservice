from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
import httpx
from Schemas import schemas
from Database import mysql_database_Config
from sqlalchemy.orm import Session 
from Models import models
from Security import security_service_contact

router=APIRouter(tags=["student"])

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="security_service_user_login")

@router.post("/create_student",status_code=status.HTTP_201_CREATED,response_model=schemas.Student_Response)
async def create_student(new_student:schemas.New_Student,db:Session=Depends(mysql_database_Config.get_db),token:str=Depends(oauth2_scheme)):
    curr_user_id=await security_service_contact.get_the_user_from_security_service(token)
    if curr_user_id["Current_User"]=="Not_Possible":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")
    student_to_be_added=models.Student(** new_student.dict())
    db.add(student_to_be_added)
    db.commit()
    db.refresh(student_to_be_added)
    return student_to_be_added

@router.get("/get_all_students")
async def getting_all_students(db:Session=Depends(mysql_database_Config.get_db),token:str=Depends(oauth2_scheme)):
    curr_user_id=await security_service_contact.get_the_user_from_security_service(token)
    if curr_user_id["Current_User"]=="Not_Possible":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")
    data_to_send_back=db.query(models.Student).all()
    return data_to_send_back

@router.get("/get_student_by_id/{id}",response_model=schemas.Student_Response)
async def getting_all_students(id:int,db:Session=Depends(mysql_database_Config.get_db),token:str=Depends(oauth2_scheme)):
    curr_user_id=await security_service_contact.get_the_user_from_security_service(token)
    if curr_user_id["Current_User"]=="Not_Possible":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")
    data_to_send_back=db.query(models.Student).filter(models.Student.student_id==id).first()
    if data_to_send_back==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Id does not exist")
    return data_to_send_back

@router.delete("/delete_student_by_id/{id}",status_code=status.HTTP_200_OK)
async def deleting_student(id:int,db:Session=Depends(mysql_database_Config.get_db),token:str=Depends(oauth2_scheme)):
    curr_user_id=await security_service_contact.get_the_user_from_security_service(token)
    if curr_user_id["Current_User"]=="Not_Possible":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")
    x=db.query(models.Student).filter(models.Student.student_id==id)
    if x==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Id does not exist")
    x.delete(synchronize_session=False)
    db.commit()
    return {"Message":"Successful"}

@router.put("/update_student/{id}",status_code=status.HTTP_200_OK,response_model=schemas.Student_Response)
async def updating_student(id:int,update_student:schemas.Update_Student,db:Session=Depends(mysql_database_Config.get_db),token:str=Depends(oauth2_scheme)):
    curr_user_id=await security_service_contact.get_the_user_from_security_service(token)
    if curr_user_id["Current_User"]=="Not_Possible":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")
    x=db.query(models.Student).filter(models.Student.student_id==id)
    if x==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Id does not exist")
    x.update(update_student.dict())
    db.commit()
    send_back_to_user=db.query(models.Student).filter(models.Student.student_id==id).first()
    return send_back_to_user

@router.get("/student_count",status_code=status.HTTP_200_OK)
async def course_count(db:Session=Depends(mysql_database_Config.get_db),token:str=Depends(oauth2_scheme)):
    curr_user_id=await security_service_contact.get_the_user_from_security_service(token)
    if curr_user_id["Current_User"]=="Not_Possible":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")
    x=db.query(models.Student).count()
    return {"Student_Count":x}

@router.get("/student_mentor")
async def student_with_their_mentors(db:Session=Depends(mysql_database_Config.get_db),token:str=Depends(oauth2_scheme)):
    curr_user_id=await security_service_contact.get_the_user_from_security_service(token)
    if curr_user_id["Current_User"]=="Not_Possible":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")
    client=httpx.AsyncClient()
    token_sending_string=f"Bearer {token}=="
    header={"Authorization":token_sending_string}
    result=db.query(models.Student.student_id,
                    models.Student.first_name,
                    models.Student.last_name,
                    models.Student.parent_id).all()
    mentor_response = await client.get("http://localhost:8003/get_all_mentors",headers=header)
    mentor=mentor_response.json()
    flist=[]
    for i in result:
        fdict={}
        for j in mentor:
            if i[3]==j["parent_id"]:
                fdict.update({"student_id":i[0],"first_name":i[1],"last_name":i[2],"parent_id":i[3]})
                fdict.update({"parent_first_name":j["first_name"],"parent_email":j["email_id"]})
                flist.append(fdict)
    return flist



