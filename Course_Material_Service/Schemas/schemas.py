from pydantic import BaseModel


class New_Course_Material(BaseModel):	
    course_id:int	
    course_material_url:str	

class Update_Course_Material(BaseModel):	
    course_material_url:str	

class Course_Material_Response(BaseModel):
    course_id:int	
    course_material_url:str		
