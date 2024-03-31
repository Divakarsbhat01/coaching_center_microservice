in order to make this application work
Mongo DB
    create a database in mongo db with name users
    port: 27017
    create collection with name user_login
    data has to be in format:
        user_name:"ram@gmail.com"
        user_password: "$2b$12$kI4W/FRwZgLlhHECHict0OvbiagU8WKADnXLyezBzjbfMbu517BVm"
        user_role:"admin"
        user_id:1
    create collection with name user_id_counter
    data has to be in format:
        user_id_counter:6
        counter_name:"user_id_counter"
MysqlDB
    create a databases in mysql db with names
    port: 3306
	coacen_fastapi_micro_course
	coacen_fastapi_micro_course_material
	coacen_fastapi_micro_parent
	coacen_fastapi_micro_student
	coacen_fastapi_micro_student_course
	coacen_fastapi_micro_teacher
	coacen_fastapi_micro_teacher_course

Service ports:
user_service :8000
security Service:8001
student_service:8002
mentor_service:8003
teacher_service:8006
course_service:8004
course_material_service:8005
student_course_service:8007
teacher_course_service:8008

Commands to run:
    python has to be installed in computer
    requirements in requirements.txt has to be installed for each service
    uvicorn main:app --port ABCD --reload
    
