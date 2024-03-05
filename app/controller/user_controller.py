from fastapi import APIRouter, HTTPException
from app.service.user_service import UserService
from config.database import SessionLocal
from model.user_model import User

router = APIRouter()
user_service = UserService()

@router.post("/users/")
async def create_user(name: str, email: str):
    db = SessionLocal()
    user = User(name=name, email=email)
    created_user = user_service.create_user(db, name, email)
    return user

@router.get("/users/{user_id}")
async def read_user(user_id: int):
    db = SessionLocal()
    user = user_service.get_user(db, user_id)
    return user