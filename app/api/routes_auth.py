from fastapi import APIRouter, HTTPException
from app.database.session import db_dependency
from app.schemas.user_schema import UserCreate, UserResponse, TokenResponse
from app.services import auth_service

router = APIRouter()

@router.post("/auth/register", response_model=UserResponse)
def register(user: UserCreate, db: db_dependency):
    return auth_service.register_user(user, db)

@router.post("/auth/login", response_model=TokenResponse)
def login(user: UserCreate, db: db_dependency):
    result = auth_service.login_user(user, db)
    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return result