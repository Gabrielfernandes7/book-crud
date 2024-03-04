from sqlalchemy import Integer, String, Column
from ..config.database import Base, engine

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), index=True)
    email = Column(String, index=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

Base.metadata.create_all(bind = engine)
