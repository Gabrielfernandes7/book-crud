from sqlalchemy import Column, Integer, String
from config.database import Base

class Pizza(Base):
    __tablename__ = "pizzas"
    id = Column(Integer, primary_key=True)
    sabor = Column(String(255))
    preco = Column(Integer)
