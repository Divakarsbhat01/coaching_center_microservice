from pydantic import BaseModel

class New_Course(BaseModel):
    course_name:str		
    course_desc:str	
    course_credit:int	

class Update_Course(BaseModel):
    course_name:str		
    course_desc:str	
    course_credit:int		

class Course_Response(BaseModel):
    course_name:str	
    course_id:int	
    course_desc:str	
    course_credit:int