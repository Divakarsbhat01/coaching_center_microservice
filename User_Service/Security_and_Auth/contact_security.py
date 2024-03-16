import json
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
import httpx

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="user_login")

async def get_the_user_from_security_service(token:str):
    client=httpx.AsyncClient()
    x = {"access_token": token,"type":"Bearer"}
    y = json.dumps(x)
    response = await client.post("http://localhost:8001/verify_logged_in_user",data=y)
    user_id = response.json()
    return user_id