from Database.mysql_database_Config import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey

class Teacher(Base):
    __tablename__="Teacher"
    teacher_first_name=Column(String(50),nullable=False)
    teacher_last_name=Column(String(50),nullable=False)
    teacher_id=Column(Integer,primary_key=True,nullable=False,autoincrement="auto")
    teacher_email=Column(String(50),nullable=False)