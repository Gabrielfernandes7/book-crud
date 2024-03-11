import uvicorn
from fastapi import FastAPI
from app.api import user

app = FastAPI()

app.include_router(user, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app)