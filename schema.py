# construindo o schema com o pydantic
from pydantic import BaseModel

class Book(BaseModel):
    title: int
    rating: int
    author_id: int

    class config:
        orm_mode = True

class Author(BaseModel):
    name: str
    age: int

    class config:
        orm_true = True
