from Database.mysql_database_Config import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey

class Teacher_Course(Base):
    __tablename__="Teacher_Course"
    table_id=Column(Integer,primary_key=True,nullable=False,autoincrement="auto")
    teacher_id=Column(Integer,nullable=False)
    course_id=Column(Integer,nullable=False)
