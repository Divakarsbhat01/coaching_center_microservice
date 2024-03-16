from pydantic import BaseModel


class New_Student(BaseModel):
    first_name:str
    last_name:str	
    student_age:int	
    email_id:str
    parent_id:int

class Update_Student(BaseModel):
    first_name:str
    last_name:str	
    student_age:int	
    email_id:str
    parent_id:int

class Student_Response(BaseModel):
    first_name:str
    last_name:str	
    student_id:int
    student_age:int	
    email_id:str
    parent_id:int
