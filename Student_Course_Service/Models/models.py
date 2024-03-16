from Database.mysql_database_Config import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey

class Student_Course(Base):
    __tablename__="Student_Course"
    table_id=Column(Integer,primary_key=True,nullable=False,autoincrement="auto")
    student_id=Column(Integer,nullable=False)
    course_id=Column(Integer,nullable=False)