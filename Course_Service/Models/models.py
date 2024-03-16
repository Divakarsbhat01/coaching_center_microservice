from Database.mysql_database_Config import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey

class Course(Base):
    __tablename__="Course"
    course_name=Column(String(50),nullable=False,unique=True)
    course_id=Column(Integer,primary_key=True,nullable=False,autoincrement="auto")
    course_desc=Column(String(100),nullable=False)
    course_credit=Column(Integer,nullable=False)