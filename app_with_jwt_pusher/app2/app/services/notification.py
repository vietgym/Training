import uuid

from sqlalchemy.orm import Session

# from app.constant.app_status import AppStatus
# from app.core.exceptions import error_exception_handler
from app.core.pusher.pusher_client import PusherClient
from app.core.settings import settings

# from ..crud.notification import crud_notification
# from ..model import User
from ..schemas.notification import NotificationCreate
# from ..model.base import NotificationType
# from app.utils.pagination import calc_skip_record_query, make_response_pagination


class NotificationService:
    def __init__(self, db: Session):
        self.db = db

    async def create_notification(self, request_data: NotificationCreate):
        client = PusherClient()
        client.push_notification(settings.GENERAL_CHANNEL, "Pusher: ID Student", "data_push=request_data")


