"""@app.post("/test")
async def testing(token:str=Depends(oauth2_scheme)):
    curr_user_id=await contact_security.get_the_user_from_security_service(token)
    print(curr_user_id)
    return {"Message":"hi"}"""

import json
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
import httpx

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="security_service_user_login")

async def get_the_user_from_security_service(token:str):
    client=httpx.AsyncClient()
    x = {"access_token": token,"type":"Bearer"}
    y = json.dumps(x)
    response = await client.post("http://localhost:8001/verify_logged_in_user",data=y)
    user_id = response.json()
    return user_id