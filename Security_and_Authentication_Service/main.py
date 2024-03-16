import logging
from fastapi import FastAPI

from Configuration.config import settings
from Routers import security_endoint


app=FastAPI()
app.include_router(security_endoint.router)

logging.getLogger('passlib').setLevel(logging.ERROR)

@app.get("/securityservice")
def get_status_of_security_service():
    return {"Message":settings.upstatus}