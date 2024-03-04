from pydantic import BaseModel
from config.database import engine, SessionLocal
class User(BaseModel):
    name: str
    email: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()