from fastapi import APIRouter

from app.api.endpoint import login
from app.api.endpoint import student
from app.api.endpoint import notification

router = APIRouter()

router.include_router(login.route, tags=["login"])
router.include_router(student.route, tags=["students_course"])
router.include_router(notification.route, tags=["Notification"])