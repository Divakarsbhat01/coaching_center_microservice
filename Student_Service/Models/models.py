from Database.mysql_database_Config import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey

class Student(Base):
    __tablename__="Student"
    first_name=Column(String(50),nullable=False)
    last_name=Column(String(50),nullable=False)
    student_id=Column(Integer,primary_key=True,nullable=False,autoincrement="auto")
    student_age=Column(Integer,nullable=False)
    email_id=Column(String(100),nullable=False)
    parent_id=Column(Integer,nullable=False)