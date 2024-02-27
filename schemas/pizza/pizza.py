from pydantic import BaseModel

class Pizza(BaseModel):
    sabor: str
    preco: int
