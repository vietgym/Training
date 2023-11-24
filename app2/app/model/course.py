from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Course(Base):
    __tablename__ = "courses"
    id_cou = Column(String, primary_key=True, index=True)
    name_cou = Column(String)
    des_cou = Column(String)

    student_id = Column(String, ForeignKey("students.id", ondelete="CASCADE"))
    student = relationship("Student", back_populates="courses")