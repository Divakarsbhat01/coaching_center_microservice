from Database.mysql_database_Config import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey

class course_material(Base):
    __tablename__="Course_Material"
    course_material_id=Column(Integer,primary_key=True,nullable=False,autoincrement="auto")
    course_material_url=Column(String(100),nullable=False)
    course_id=course_id=Column(Integer,nullable=False)