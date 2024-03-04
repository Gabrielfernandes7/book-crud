from app import app
from config.database import SessionLocal
from model.user_model import User

@app.post("/users/")
async def create_user(name: str, email: str):
    db = SessionLocal()
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}")
async def read_item(item_id: int):
    db = SessionLocal()
    item = db.query(User).filter(User.id == item_id).first()
    return item