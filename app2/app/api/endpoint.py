from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app.db.database import SessionLocal, engine
from app.crud import crud_std
from app.schemas import schemas_std
from app.services.service_std import StdService
from app.utils.response import make_response_object

route = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@route.post("/create_student/", response_model=schemas_std.Student)
async def create_student(student: schemas_std.StudentParam, db: Session = Depends(get_db)):
    std_service = StdService(db=db)
    std_response = await std_service.creat_student(student=student)
    return std_response


@route.post("/update_course_student/{student_id}", response_model=schemas_std.Course)
async def create_student(student_id: str, course: schemas_std.CourseBase, db: Session = Depends(get_db)):
    std_service = StdService(db=db)
    std_response = await std_service.creat_course(student_id=student_id, course=course)
    return std_response


# @route.get("/get_student_by_id/{student_id}")
# async def get_student_byid(student_id: str, db: Session = Depends(get_db)):
#     std_service = StdService(db=db)
#     std_response = await std_service.get_student_by_id(student_id=student_id)
#     result = dict(std_response=std_response)
#     #breakpoint()
#     return result


@route.get("/get_student_by_id/{student_id}")
def get_student_byid(student_id: str, db: Session = Depends(get_db)):
    return crud_std.get_student_and_course(db=db, student_id=student_id)


@route.put("/edit_student_by_id/{student_id}", response_model=schemas_std.Student)
async def edit_student_by_id(student_id: str, student_update: schemas_std.StudentBase, course_update: schemas_std.CourseBase, db: Session = Depends(get_db)):
    std_service = StdService(db=db)
    std_response = await std_service.update_student_by_id(student_id=student_id, student_update=student_update, course_update=course_update)
    return std_response


@route.delete("/delete_student_by_id/{student_id}", response_model=schemas_std.Student)
async def delete_student_endpoint(student_id: str, db: Session = Depends(get_db)):
    students_connect = StdService(db=db)
    del_student = await students_connect.del_student_id(student_id=student_id)
    return del_student


@route.get("/get_all_student/get_students")
async def get_students(skip: int, limit: int, db: Session = Depends(get_db)):
    students_connect = StdService(db=db)
    students_all = await students_connect.get_all_students(skip=skip, limit=limit)
    return students_all


# thêm 1 bảng Couser, PK student_id
# có các thông tin cơ bản như: id, name, description, ..
# khi xóa 1 User thì bảng Course phải được xóa
#
# listing Course thì phải phải list được cả User tạo ra nó
# vd:
# {
# Course: id, name, ...
# Student: id, username,...
# }


#@route.put("/update_couser_to_student_by_id/{student_id}" )

# @route.put("/edit_student_by_id/{student_id}", response_model=schemas_std.Student)
# def edit_student_byid(student_id: str, updated_student: schemas_std.StudentBase, db: Session = Depends(get_db)):
#     db_student = crud_std.get_student(db, student_id=student_id)
#     if db_student is None:
#         raise HTTPException(status_code=404, detail="Student not found")
#     for field, value in updated_student.dict().items():
#         setattr(db_student, field, value)
#     db.commit()
#     db.refresh(db_student)
#     return db_student