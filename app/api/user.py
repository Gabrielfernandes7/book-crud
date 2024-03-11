from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.model.user_model import User

app = FastAPI()

@app.post("/user", response_model=User)
def create_person(person: User, db: Session = Depends(get_db)):
    db.add(person)
    db.commit()
    db.refresh(person)
    return person

@app.get("/user/{user_id}", response_model=User)
def get_person(user_id: int, db: Session = Depends(get_db)):
    person = db.query(User).filter(User.id == user_id).first()
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
    return person

# @app.put("/user/{user_id}", response_model=Person)
# def update_person(user_id: int, person: Person, db: Session = Depends(get_db)):
#     existing_person = db.query(Person).filter(Person.id == user_id).first()
#     if not existing_person:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
#     existing_person.name = person.name
#     existing_person.email = person.email  # Update email if provided
#     db.commit()
#     return existing_person

# @app.delete("/user/{person_id}")
# def delete_person(person_id: int, db: Session = Depends(get_db)):
#     person = db.query(Person).filter(Person.id == person_id).first()
#     if not person:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
#     db.delete(person)
#     db.commit()
#     return JSONResponse(status_code=status)
