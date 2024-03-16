from pydantic import BaseModel


class Teacher_Course(BaseModel):
    teacher_id:int	
    course_id:int

class Teacher_Course_response(BaseModel):
    teacher_id:int	
    course_id:int
