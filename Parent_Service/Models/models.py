from Database.mysql_database_Config import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey

class Mentor(Base):
    __tablename__="Parent"
    first_name=Column(String(50),nullable=False)
    last_name=Column(String(50),nullable=False)
    parent_id=Column(Integer,primary_key=True,nullable=False,autoincrement="auto")
    email_id=Column(String(100),nullable=False)