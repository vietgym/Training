import uuid
import smtplib
import logging
from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..schemas.schemas_std import StudentResponse, StudentParam, StudentBase, CourseBase
from ..crud import crud_std

logger = logging.getLogger(__name__)

class StdService:
    def __init__(self, db: Session):
        self.db = db

    async def creat_student(self, student: StudentParam):
        crt_student = crud_std.create_student(db=self.db, student=student)
        if not crt_student:
            return "LOi"
        return crt_student

    async def creat_course(self, student_id: str, course: CourseBase):
        crt_course = crud_std.create_course(db=self.db, student_id=student_id, course=course)
        if not crt_course:
            return "LOi"
        return crt_course

    async def get_student_by_id(self, student_id: str):
        current_std = crud_std.get_student_and_course(db=self.db, student_id=student_id)
        if not current_std:
            return "LOI"
        return current_std

    async def update_student_by_id(self, student_id: str, student_update: StudentBase, course_update: CourseBase):
        current_std = crud_std.update_student(db=self.db, student_id=student_id, student_update=student_update, course_update=course_update)
        if not current_std:
            return "LOi"
        return current_std

    async def get_all_students(self, skip: int, limit: int):
        current_stds = crud_std.get_students(db=self.db, skip=skip, limit=limit)
        return dict(users=current_stds)

    async def del_student_id(self, student_id: str):
        current_std = crud_std.delete_student(db=self.db, student_id=student_id)
        if not current_std:
            return "LOI"
        return current_std
