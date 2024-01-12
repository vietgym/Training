from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.notification import NotificationService
from app.utils.response import make_response_object
from app.schemas.notification import NotificationCreate
from app.db.database import SessionLocal

route = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@route.post("/notifications/", response_model=dict)
async def create_notification(request_data: NotificationCreate, db: Session = Depends(get_db)):
    notification_service = NotificationService(db=db)
    a = await notification_service.create_notification(request_data)
    return NotificationCreate



