from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from app.database.session import db_dependency
from app.schemas.user_schema import UserCreate, UserResponse, TokenResponse
from app.services import auth_service

router = APIRouter(tags=["Auth"])

@router.post("/auth/register", response_model=UserResponse)
def register(user: UserCreate, db: db_dependency):
    return auth_service.register_user(user, db)

@router.post("/auth/login", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: db_dependency = None):
    user = UserCreate(email=form_data.username, password=form_data.password)
    result = auth_service.login_user(user, db)
    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return result