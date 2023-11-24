from datetime import datetime
from pydantic import BaseModel


class StudentBase(BaseModel):
    name: str
    email: str
    gpa: str


class StudentParam(BaseModel):
    name: str
    email: str
    gpa: str


class Student(StudentBase):
    id: str
    class Config:
        orm_mode = True


class CourseBase(BaseModel):
    name_cou: str
    des_cou: str


class Course(CourseBase):
    id_cou: str
    student_id: str
    class Config:
        orm_mode = True


class StudentResponse(StudentBase):
    courses: Course  # Thêm một trường courses
    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: int(v.timestamp())
        }
