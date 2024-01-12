from typing import Optional

from pydantic import BaseModel


class NotificationBase(BaseModel):
    data: dict
    student_id: str
    notification_type: str


class NotificationCreate(NotificationBase):
    pass


class NotificationUpdate(NotificationBase):
    pass
