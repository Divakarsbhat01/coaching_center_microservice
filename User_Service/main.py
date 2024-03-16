import logging
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from Routers import user_operations
from Configuration.config import settings
from Security_and_Auth import contact_security

app=FastAPI()
app.include_router(user_operations.router)
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="user_login")

logging.getLogger('passlib').setLevel(logging.ERROR)

@app.get("/userservice")
def get_status_of_user_service():
    return {"Message":settings.upstatus}

@app.post("/test")
async def testing(token:str=Depends(oauth2_scheme)):
    curr_user_id=await contact_security.get_the_user_from_security_service(token)
    print(curr_user_id)
    return {"Message":"hi"}