from pydantic import BaseModel

class New_User(BaseModel):
    user_name:str
    user_password:str
    user_role:str

class User_Update(BaseModel):
    user_name:str
    user_password:str
    user_role:str

class Reset_Password(BaseModel):
    user_name:str
    user_password:str
    user_new_password:str

class User_Response(BaseModel):
    user_name:str
    user_id:int
    user_role:str

class User_Create_Response(BaseModel):
    user_name:str
    user_id:int
    user_role:str
    click_to_verify:str
