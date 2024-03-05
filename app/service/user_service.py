from app.model import User
from fastapi import HTTPException

class UserService:

    # construtor vazio
    def __init__(self):
        pass

    def create_user(self, db, user: User):
        db.add(user)
        db.commit() # persistir a mudança no banco de dados
        db.refresh(user)

        return user
    
    def get_user(self, db, user_id: int):
        user = db.query(User).filter(
            User.id == user_id
        ).first()

        if user is None:
            raise HTTPException(status_code=404, detail="user not found")
        
        return user
