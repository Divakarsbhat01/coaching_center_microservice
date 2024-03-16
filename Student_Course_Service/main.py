import logging
from fastapi import FastAPI
from httpx import AsyncClient
from Configuration.config import settings
from Routers import student_course

app=FastAPI()
app.include_router(student_course.router)
client = AsyncClient()

logging.getLogger('passlib').setLevel(logging.ERROR)


@app.get("/")
def api_working_status():
    return {"Status": settings.upstatus}