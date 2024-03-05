from app.model import User

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
        return db.query(User).filter(
            User.id == user_id
        ).first()
