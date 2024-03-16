from pydantic import BaseModel


class New_Teacher(BaseModel):
    teacher_first_name:str	
    teacher_last_name:str
    teacher_email:str	

class Update_Teacher(BaseModel):
    teacher_first_name:str	
    teacher_last_name:str
    teacher_email:str		

class Teacher_Response(BaseModel):
    teacher_first_name:str	
    teacher_id:int
    teacher_last_name:str
    teacher_email:str