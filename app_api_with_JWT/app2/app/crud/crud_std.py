import uuid
from sqlalchemy.orm import Session
from sqlalchemy.orm import Session
# from app.model.models import Student, Course
from app.model.student import Student
from app.model.course import Course
from app.schemas import schemas_std


class StudentAndCourseResponse:
    def __init__(self, student, course):
        self.student = student
        self.course = course


def check_exits_id(db: Session, login_id: str) -> bool:
    exits_id = db.query(Student).filter(Student.id == login_id).first()
    return exits_id is not None


def create_student(db: Session, student: schemas_std.StudentParam):
    id_tmp = str(uuid.uuid4())
    db_student = Student(id=id_tmp, name=student.name, email=student.email, gpa=student.gpa)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def create_course(db: Session, student_id: str, course: schemas_std.CourseBase):
    id_cou = str(uuid.uuid4())
    db_course = Course(student_id=student_id, id_cou=id_cou, name_cou=course.name_cou, des_cou=course.des_cou)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def get_student(db: Session, student_id: str):
    student_response = db.query(Student).filter(Student.id == student_id).first()
    return student_response


def get_course(db: Session, student_id: str):
    course_response = db.query(Course).filter(Course.student_id == student_id).first()
    return course_response


def get_student_and_course(db: Session, student_id: str):
    student_tbl = (db.query(Student, Course)
                   .outerjoin(Course, Student.id == Course.student_id)
                   .filter(Student.id == student_id).all())
    student_response = [StudentAndCourseResponse(student=student, course=course) for student, course in student_tbl]
    return student_response


def get_students(db: Session, skip: int, limit: int):
    stmt = (db.query(Student, Course)
            .outerjoin(Course, Student.id == Course.student_id)
            .offset(skip)
            .limit(limit)
            .all())
    student_courses_map = {}
    for student, course in stmt:
        if student.id not in student_courses_map:
            student_courses_map[student.id] = {
                "student": student,
                "courses": [course] if course is not None else None
            }
        elif course is not None:
            student_courses_map[student.id]["courses"].append(course)
    response_data = [StudentAndCourseResponse(student=data["student"], course=data["courses"]) for data in
                     student_courses_map.values()]
    return response_data


def update_student(db: Session, student_id: str, student_update: schemas_std.StudentBase, course_update: schemas_std.CourseBase):
    db_student = get_student(db=db, student_id=student_id)
    if db_student is None:
        return "LOI"
    db_course = db.query(Course).filter(Course.student_id == student_id).first()
    for field, value in student_update.dict().items():
        setattr(db_student, field, value)
    for field, value in course_update.dict().items():
        setattr(db_course, field, value)
    db.commit()
    db.refresh(db_student)
    db.refresh(db_course)
    return db_student, db_course


def delete_student(db: Session, student_id: str):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student:
        db_course = db.query(Course).filter(Course.student_id == student_id).first()
        db.delete(db_student)
        if db_course:
            db.delete(db_course)
        db.commit()
    return db_student


# def create_course(db: Session, student_id: str, course: schemas_std.CourseBase):
#     id_cou = str(uuid.uuid4())
#     db_course = Course(student_id=student_id, id_cou=id_cou, name_cou=course.name_cou, des_cou=course.des_cou)
#     db.add(db_course)
#     db.commit()
#     db.refresh(db_course)
#     return db_course


# def get_students(db: Session, skip: int, limit: int):
#     return db.query(Student).offset(skip).limit(limit).all()


# def delete_student(db: Session, student_id: str):
#     db_student = db.query(Student).filter(Student.id == student_id).first()
#     db_course = db.query(Course).filter(Course.student_id == student_id).first()
#     if db_student and db_course:
#         db.delete(db_student)
#         db.delete(db_course)
#         db.commit()
#     return db_student
