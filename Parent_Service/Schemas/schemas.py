from pydantic import BaseModel


class New_Parent(BaseModel):
    first_name:str	
    last_name:str		
    email_id:str	

class Update_Parent(BaseModel):
    first_name:str	
    last_name:str			
    email_id:str	

class Parent_Response(BaseModel):
    first_name:str	
    last_name:str	
    email_id:str