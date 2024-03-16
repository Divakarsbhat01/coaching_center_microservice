import logging
from fastapi import FastAPI
from httpx import AsyncClient
from Configuration.config import settings
from Routers import course

app=FastAPI()
app.include_router(course.router)
client = AsyncClient()

logging.getLogger('passlib').setLevel(logging.ERROR)


@app.get("/")
def api_working_status():
    return {"Status": settings.upstatus}