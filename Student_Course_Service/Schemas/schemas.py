from pydantic import BaseModel


class Student_Course(BaseModel):
    student_id:int	
    course_id:int

class Student_Course_response(BaseModel):
    student_id:int	
    course_id:int