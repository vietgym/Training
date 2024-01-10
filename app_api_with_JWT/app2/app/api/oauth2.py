from datetime import datetime, timedelta
from sqlalchemy.orm import Session
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.constant.app_status import AppStatus
from app.core.settings import settings
from app.crud import crud_std
from app.db.database import SessionLocal, engine

token_info = {}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_token(data: dict, token_type: str):
    to_encode = data.copy()
    if token_type == "access":
        expire = datetime.utcnow() + timedelta(days=settings.ACCESS_TOKEN_EXPIRES_IN_DAYS)
    else:
        expire = datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRES_IN_DAYS)
    to_encode.update({"token_type": token_type, "exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

    return encoded_jwt


def create_access_token(data: dict):
    return create_token(data, token_type="access")


def create_refresh_token(data: dict):
    return create_token(data, token_type="refresh")


def verify_token(credentials: HTTPAuthorizationCredentials):
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=AppStatus.ERROR_MISSING_TOKEN_ERROR.meta
        )
    try:
        decoded_token = jwt.decode(credentials.credentials,
                                   settings.JWT_SECRET_KEY,
                                   algorithms=settings.JWT_ALGORITHM)
    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=AppStatus.ERROR_INVALID_TOKEN.meta
        )
    return decoded_token


def get_decode_token(
        credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False))
):
    decoded_token = verify_token(credentials)
    if decoded_token['token_type'] != "access" and decoded_token['token_type'] != "refresh":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=AppStatus.ERROR_INVALID_TOKEN.meta
        )
    return decoded_token


def verify_access_token(
        credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False))
):
    decoded_token = verify_token(credentials)
    if decoded_token['token_type'] != "access":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=AppStatus.ERROR_INVALID_TOKEN.meta
        )
    return decoded_token


def verify_refresh_token(
        credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False))
):
    decoded_token = verify_token(credentials)
    if decoded_token['token_type'] != "refresh":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=AppStatus.ERROR_INVALID_TOKEN.meta
        )
    return decoded_token


def get_current_user(
        token: dict = Depends(verify_access_token),
        db: Session = Depends(get_db)
):
    std_id = token['uid']
    student = crud_std.get_student_and_course(db=db, student_id=std_id)
    return student
