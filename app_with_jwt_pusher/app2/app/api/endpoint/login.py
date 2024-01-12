from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.services.service_std import StdService
from app.api.depend import oauth2
from app.utils.response import make_response_object
from app.api.depend.oauth2 import create_access_token, create_refresh_token

route = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@route.post("/auth/login/")
async def login(login_id: str, db: Session = Depends(get_db)):
    std_service = StdService(db=db)
    std_response = await std_service.login(login_id=login_id)
    if std_response == True:
        created_access_token = create_access_token(data={"uid": login_id})
        created_refresh_token = create_refresh_token(data={"uid": login_id})
        return make_response_object(data=dict(access_token=created_access_token,
                                              refresh_token=created_refresh_token))
    return std_response


@route.post("/auth/decode_token/")
async def decode_token(decoded_token=Depends(oauth2.get_decode_token)):
    return decoded_token


@route.post("/auth/refresh_token/")
async def refresh_token(decode_refresh_token=Depends(oauth2.verify_refresh_token),
                        db: Session = Depends(get_db)):
    std_service = StdService(db=db)
    current_std = await std_service.get_student_by_id(decode_refresh_token['uid'])
    if not current_std:
        return "loi"
    created_access_token = create_access_token(data={"uid": decode_refresh_token['uid']})
    created_refresh_token = create_refresh_token(data={"uid": decode_refresh_token['uid']})
    return make_response_object(data=dict(access_token=created_access_token,
                                          refresh_token=created_refresh_token))
